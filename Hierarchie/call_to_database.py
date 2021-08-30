from loguru import logger
import pyodbc


def call_to_dict(cursor) -> dict:
    columns = [desc[0] for desc in cursor.description]
    formatted = dict()
    for row in cursor:
        formatted[row[0]] = dict()
        for c in columns:
            if columns.index(c) != 0:
                formatted[row[0]][c] = row[columns.index(c)]
    return formatted


def get_society(cursor, black_list: list) -> dict:
    query = f'''
    SELECT idDossier, idGroupe, NomSociete
    FROM Dossier
    '''
    cursor.execute(query)
    societies = call_to_dict(cursor=cursor)
    for bl in black_list:
        if bl in societies.keys():
            societies.pop(bl)
    return societies


def get_groups(cursor, black_list: list) -> dict:
    query = f'''
    SELECT Libelle, idGroupe 
    FROM Groupe
    ORDER BY Libelle
    '''
    cursor.execute(query)
    groups = call_to_dict(cursor=cursor)
    for bl in black_list:
        if bl in groups.keys():
            groups.pop(bl)
    return groups


def get_enterprise_from_group(cursor, group: int) -> list:
    query = f'''
    SELECT idDossier
    FROM Dossier
    WHERE idGroupe = {group}
    '''
    cursor.execute(query)
    id_dossier = list()
    for row in cursor:
        id_dossier.append(row[0])
    return id_dossier


def get_employees(cursor, id_dossier: list) -> dict:
    """
    Calls the database to get the employees of the enterprise thanks to the idDossier field
    :return: dict containing the employees with LIST as keys
    """
    count = 0
    id_dossier_str = "idDossier = "
    for id_d in id_dossier:
        if count > 0:
            id_dossier_str += " or idDossier = "
        id_dossier_str += str(id_d)
        count += 1
    query = f'''
    SELECT idSalarie, idDossier, CodMatricule, Nom, Prenom, idDecideur, idEmploi
    FROM PWA.dbo.Salarie
    WHERE ({id_dossier_str})
    AND flgActif = 1
    '''
    cursor.execute(query)
    return call_to_dict(cursor=cursor)


def update_employee_decision_maker(cursor, decision_maker_id: str, employee_id: str, id_dossier: list):
    count = 0
    id_dossier_str = "idDossier = "
    for id_d in id_dossier:
        if count > 0:
            id_dossier_str += " or idDossier = "
        id_dossier_str += str(id_d)
        count += 1
    if len(decision_maker_id) > 0:
        query = f'''
        UPDATE Salarie
        SET idDecideur = {decision_maker_id}
        WHERE CodMatricule = '{employee_id}'
        AND ({id_dossier_str})
        '''
    else:
        query = f'''
        UPDATE Salarie
        SET idDecideur = NULL
        WHERE CodMatricule = '{employee_id}'
        AND ({id_dossier_str})
        '''
    logger.debug(query)
    cursor.execute(query)
