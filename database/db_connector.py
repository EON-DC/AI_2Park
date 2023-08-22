import json

import pandas as pd
import psycopg2
from sqlalchemy import create_engine


class DBConnector:
    # ===================== BASIC ============================ #
    _instance = None
    current_config_path = r"db_config.json"
    module_config_path = r"database/db_config.json"

    def read_config(self):
        """db 접속 정보는 config file에서 관리함, json으로 읽어서 dictionary 로 반환함 """
        with open(self.config_path, 'r', encoding='utf-8') as config_file:
            config_dict = json.load(config_file)
            return config_dict

    def __new__(cls, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.conn = None
        self.engine = None
        self.origin_conn = None
        self.origin_engine = None
        self.config_path = self.set_up_config_path()
        self.config = self.read_config()

    def set_up_config_path(self):
        """외부에서 해당 파일 호출할 경우 경로 꼬임 해결하기 위한 함수"""
        if __name__ == "__main__":
            return self.current_config_path
        else:
            return self.module_config_path

    def db_connect(self):
        # 메인 db 연결
        self.conn = psycopg2.connect(host=self.config["host"],
                                     database=self.config["main_database_name"],
                                     user=self.config["user"],
                                     port=self.config["port"],
                                     password=self.config["password"])
        engine_param = f'postgresql://{self.config["user"]}:{self.config["password"]}@{self.config["host"]}' \
                       f':{self.config["port"]}/{self.config["main_database_name"]}'
        self.engine = create_engine(engine_param)

    def db_disconnect(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def commit_db(self):
        self.conn.commit()

    def find_all_health_tip(self):
        self.db_connect()
        query = """select * from "tb_health_tip" """
        df = pd.read_sql(query, self.engine)
        self.db_disconnect()
        return df


if __name__ == '__main__':
    conn = DBConnector()
    df = conn.find_all_health_tip()
    print(df)
