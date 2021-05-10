# -*- coding: utf-8 -*-
from os import getenv
import json

#from mysql import connector
import pymysql


class Config(object):
    def __init__(self, project_name=None, _type='json'):
        # super(Config, self).__init__(dict())
        for env_var in [
            'grh_config_manager.user',
            'grh_config_manager.password',
            'grh_config_manager.database',
            'grh_config_manager.host',
        ]:
            if getenv(env_var) is None:
                raise EnvironmentError(f'{env_var} is not set')
        self._reload_config(project_name, _type=_type)

    def _reload_config(self, project_name, _type='json'):
        connect = pymysql.connect(user=getenv('grh_config_manager.user'),
                                    password=getenv('grh_config_manager.password'),
                                    database=getenv('grh_config_manager.database'),
                                    host=getenv('grh_config_manager.host'),
                                    #auth_plugin='mysql_native_password'
                                    )

        cursor = connect.cursor()

        cursor.execute(f'SELECT configuration_files.{_type} FROM configuration_files '
                       f'where project_name="{project_name}"')
        connect.close()
        ret = cursor.fetchall()
        if len(ret) == 0:
            raise ValueError('No configuration for this value', project_name)
        else:
            raw = ret[0][0]
            raw = raw.replace('\\', '\\\\')
        j = json.loads(raw)
        self.config = j
        # for key in j:
        #
        #     if isinstance(j[key], str):
        #         pass
        #     #     setattr(self, key, j[key])
        #     elif isinstance(j[key], dict):
        #         setattr(self, key, object)
        #         for k in j[key]:
        #             attr = getattr(self, key)
        #             setattr(attr, k, j[key][k])
        #
        #     else:
        #         print('STOP')

    def save_config(self, project_name, _type="json"):
        data = str(self.config)
        data = data.replace('"', '\\"')
        data = data.replace("'", "\\'")
        data = data.replace("\\'", '\\"')
        data = data.replace('d\\"e', "d\\'e")
        data = data.replace('l\\"a', "l\\'a")
        connect = pymysql.connect(user=getenv('grh_config_manager.user'),
                                  password=getenv('grh_config_manager.password'),
                                  database=getenv('grh_config_manager.database'),
                                  host=getenv('grh_config_manager.host'),
                                  # auth_plugin='mysql_native_password'
                                  )
        cursor = connect.cursor()

        cursor.execute(f'''UPDATE configuration_files set configuration_files.{_type} = '{data}' '''
                       f'''where project_name='{project_name}' ''')
        connect.commit()
        connect.close()

    @staticmethod
    def new_config(project_name, data, _type="json"):
        connect = connector.connect(user=getenv('grh_config_manager.user'),
                                    password=getenv('grh_config_manager.password'),
                                    database=getenv('grh_config_manager.database'),
                                    host=getenv('grh_config_manager.host'),
                                    auth_plugin='mysql_native_password')
        cursor = connect.cursor()

        cursor.execute(f'''insert into configuration_files (project_name, {_type}) '''
                       f'''values ('{project_name}', '{data}')''')
        connect.commit()
        connect.close()
