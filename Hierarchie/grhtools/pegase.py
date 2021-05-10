# -*- coding: utf-8 -*-
from loguru import logger
import pyodbc


def execute_and_format_query(query, cursor, debug=False, fetchone=False):
    if debug:
        logger.debug(query)
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    rows = []
    if fetchone:
        row = cursor.fetchone()
        return dict(zip(columns, row)) if row else None
    else:
        for row in cursor.fetchall():
            data = dict(zip(columns, row))
            rows.append(data)
        return rows


def get_sections(cursor, codsociete):
    query = f"""
    SELECT CODRUBRIQUE, NOM, IDSOCIETE
    FROM [Pegase3prod].[dbo].[RUBRIQUES]
    where
        (IDSOCIETE = (select top 1 IDSOCIETE FROM SOCIETE WHERE CODSOCIETE = '{codsociete}') or IDSOCIETE = 0)
        and DATFINVALIDITE > GETDATE()
    group by CODRUBRIQUE, NOM, IDSOCIETE
    """
    cursor.execute(query)
    # logger.debug(query)
    socs = dict()
    sections_labels = dict()
    for row in cursor.fetchall():
        if row[0] not in socs:
            socs[row[0]] = row[2]
        if row[0] not in sections_labels or socs[row[0]] == 0:
            sections_labels[row[0]] = row[1]
    return sections_labels


def get_import_masks(config, name, codsociete, exclude_names=None):
    if exclude_names is None:
        exclude_names = []
    cstring = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + config['login_p3']['server'] + ';DATABASE=' + \
              config['login_p3']['database'] + ';UID=' + config['login_p3']['username'] + ';PWD=' + \
              config['login_p3']['password']
    cnxn = pyodbc.connect(cstring)
    cursor = cnxn.cursor()
    exclude = ' '.join([f"and nom not like '%{name}%'" for name in exclude_names])

    sections_labels = get_sections(cursor, codsociete)
    imports = dict()
    rubriques = dict()

    head = ['IMPORT', 'CODIMPORT', 'NOM', 'POSITIONETA', 'FLGCODETAB', 'POSITIONSAL', 'FLGCODSALARIE',
            'POSITIONSOCIETE', 'FLGCODSOCIETE']
    query = f"""
    Select {', '.join(head)}
    FROM IMPORTSELEMENTS
    WHERE nom like '%{name}%' {exclude}
    """
    # logger.debug(query)
    cursor.execute(query)

    for row in cursor.fetchall():
        row = dict(zip(head, row))
        for rubrique in row['IMPORT'].split('\r\n'):
            if rubrique:
                rubrique = rubrique.split('|')
                if rubrique[0] not in rubriques:
                    rubriques[rubrique[0]] = {
                        'code': rubrique[0],
                        'values': [{
                            'type': config['column_type'][rubrique[1]],
                            'insert_mode': config['insert_mode'][rubrique[2]],
                            'position': rubrique[3]
                        }],
                        'label': sections_labels[rubrique[0]],
                        'import_name': row['NOM']
                    }
                else:
                    rubriques[rubrique[0]]['values'].append({
                        'type': config['column_type'][rubrique[1]],
                        'insert_mode': config['insert_mode'][rubrique[2]],
                        'position': rubrique[3]
                    })
        if row['NOM'] not in imports:
            imports[row['NOM']] = {
                'eta': (row['FLGCODETAB'], row['POSITIONETA']),
                'sal': (row['FLGCODSALARIE'], row['POSITIONSAL']),
                'soc': (row['FLGCODSOCIETE'], row['POSITIONSOCIETE']),
            }
    return rubriques
