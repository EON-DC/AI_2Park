import datetime
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
        self.cursor = None
        self.config_path = self.set_up_config_path()
        self.config = self.read_config()

    def set_up_config_path(self):
        """외부에서 해당 파일 호출할 경우 경로 꼬임 해결하기 위한 함수"""
        if __name__ == "__main__":
            return self.current_config_path
        else:
            return self.module_config_path

    def db_connect(self):
        if self.conn is None:
            # 메인 db 연결
            self.conn = psycopg2.connect(host=self.config["host"],
                                         database=self.config["main_database_name"],
                                         user=self.config["user"],
                                         port=self.config["port"],
                                         password=self.config["password"])
            self.cursor = self.conn.cursor()
            engine_param = f'postgresql://{self.config["user"]}:{self.config["password"]}@{self.config["host"]}' \
                           f':{self.config["port"]}/{self.config["main_database_name"]}'
            self.engine = create_engine(engine_param)

    def db_disconnect(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    ################################################################################
    #
    #  Health tip
    #
    ################################################################################

    def find_all_health_tip(self):
        self.db_connect()
        query = """select * from "tb_health_tip" """
        df = pd.read_sql(query, self.engine)
        self.db_disconnect()
        return df

    ################################################################################
    #
    #  User
    #
    ################################################################################
    def access_login(self, username, password):
        self.db_connect()
        query = f"""select * from "tb_user" where "username"='{username}' and "user_pw"='{password}' """
        df = pd.read_sql(query, self.engine)
        self.db_disconnect()
        if len(df) == 0:
            return False
        else:
            return df

    def join(self, username, password, name, email):
        self.db_connect()
        user_dict = dict()
        user_dict.update({"username": username,
                          "user_pw": password,
                          "name": name,
                          "email": email,
                          "join_timestamp": datetime.datetime.now()})
        df = pd.DataFrame([user_dict])
        try:
            df.to_sql("tb_user", self.engine, if_exists="append", index=False, index_label=False)
            has_success = True
        except Exception:
            has_success = False
        self.db_disconnect()
        return has_success

    def check_duplicate_username(self, username):
        self.db_connect()
        query = f"""select * from "tb_user" where "username"='{username}'"""
        df = pd.read_sql(query, self.engine)
        self.db_disconnect()
        if len(df) == 0:
            has_same_name = False
        else:
            has_same_name = True
        return has_same_name

    ################################################################################
    #
    #  Medication
    #
    ################################################################################

    def find_medication_by_mapping_code(self, mapping_code):
        self.db_connect()
        converted_mapping_code = f"K-{mapping_code:06d}"
        query = f"""select * from "tb_medication" where "dl_mapping_code"='{converted_mapping_code}' """
        df = pd.read_sql(query, self.engine)
        self.db_disconnect()
        return df

    def find_medication_by_medication_id(self, medication_id):
        self.db_connect()
        query = f"""select * from "tb_medication" where "medication_id"='{medication_id}' """
        df = pd.read_sql(query, self.engine)
        self.db_disconnect()
        return df

    ################################################################################
    #
    #  prescription
    #
    ################################################################################

    def find_all_prescriptions_by_user_id(self, user_id):
        self.db_connect()
        query = f"""select * from "tb_prescription" where prescription_id in  
        (select "prescription_id" from "tb_prescription_user" where "user_id"={user_id})"""
        df = pd.read_sql(query, self.engine)
        if not df.empty:
            df = df.dropna(subset=['saved_timestamp'])
            df['saved_timestamp'] = df['saved_timestamp'].dt.tz_convert(tz="Asia/Seoul")
            df['taking_start_timestamp'] = df['taking_start_timestamp'].dt.tz_convert(tz="Asia/Seoul")
        self.db_disconnect()
        return df

    def create_prescription_with_medication_mapping_id(self,
                                                       user_id,
                                                       medication_mapping_id,
                                                       day_duration,
                                                       eat_amount,
                                                       daily_eat_count,
                                                       taking_start_timestamp=None):
        self.db_connect()
        # medication mapping id로 medication id 알아오기
        medi_df = self.find_medication_by_mapping_code(medication_mapping_id)
        medication_id = medi_df.to_dict('records')[0]['medication_id']
        saved_timestamp = datetime.datetime.now()
        # prescription 로우 추가
        if taking_start_timestamp is None:
            taking_start_timestamp = saved_timestamp
        prescription_row = {
            'medication_id': medication_id,
            'day_duration': day_duration,
            'eat_amount': eat_amount,
            'daily_eat_count': daily_eat_count,
            'saved_timestamp': saved_timestamp,
            'taking_start_timestamp': taking_start_timestamp,
        }
        data = pd.DataFrame([prescription_row])
        data.to_sql("tb_prescription", self.engine, if_exists="append", index_label=False, index=False)
        self.db_connect()
        self.cursor: psycopg2.cursor
        self.cursor.execute("SELECT prescription_id FROM tb_prescription ORDER BY prescription_id DESC LIMIT 1;")
        prescription_id = int(self.cursor.fetchone()[0])

        # 연관관계 맵핑
        relation_data = {
            'prescription_id': prescription_id,
            'user_id': user_id,
            'saved_timestamp': saved_timestamp
        }
        relation_data = pd.DataFrame([relation_data])
        relation_data.to_sql("tb_prescription_user", self.engine, if_exists="append", index_label=False, index=False)
        self.db_disconnect()
        prescription_df = self.find_prescription_by_prescription_id(prescription_id)
        if not prescription_df.empty:
            prescription_df = prescription_df.dropna(subset=['saved_timestamp'])
            prescription_df['saved_timestamp'] = prescription_df['saved_timestamp'].dt.tz_convert(tz="Asia/Seoul")
            prescription_df['taking_start_timestamp'] = prescription_df['taking_start_timestamp'].dt.tz_convert(tz="Asia/Seoul")
        return prescription_df

    def find_prescription_by_prescription_id(self, prescription_id):
        self.db_connect()
        query = f"""select * from "tb_prescription" where prescription_id={prescription_id}"""
        df = pd.read_sql(query, self.engine)
        if not df.empty:
            df = df.dropna(subset=['saved_timestamp'])
            df['saved_timestamp'] = df['saved_timestamp'].dt.tz_convert(tz="Asia/Seoul")
            df['taking_start_timestamp'] = df['taking_start_timestamp'].dt.tz_convert(tz="Asia/Seoul")
        self.db_disconnect()
        return df

    def delete_prescription_by_prescription_id(self, prescription_id):
        self.db_connect()
        query = """
            delete from "tb_prescription" where prescription_id=%s;
        """
        self.cursor.execute(query, (prescription_id, ))
        self.conn.commit()
        self.db_disconnect()

    ################################################################################
    #
    #  prescription user
    #
    ################################################################################
    ################################################################################
    #
    #  taking schedule
    #
    ################################################################################

    def find_schedule_by_prescription_id(self, prescription_id):
        self.db_connect()
        query = f"""select * from "tb_taking_schedule" where prescription_id={prescription_id}"""
        df = pd.read_sql(query, self.engine)
        df['plan_timestamp'] = df['plan_timestamp'].dt.tz_convert(tz="Asia/Seoul")
        self.db_disconnect()
        return df

    def create_schedule_by_prescription_id_and_taking_index_and_plan_timestamp(self,
                                                                               prescription_id,
                                                                               taking_index,
                                                                               year,
                                                                               month,
                                                                               day,
                                                                               hour,
                                                                               minute):
        plan_timestamp = datetime.datetime(year, month, day, hour, minute)

        schedule_data = {
            "prescription_id": prescription_id,
            "taking_index": taking_index,
            "plan_timestamp": plan_timestamp,
            "has_taken": False,
            "edit_timestamp": None,
        }
        schedule_data = pd.DataFrame([schedule_data])
        self.db_connect()
        result = schedule_data.to_sql("tb_taking_schedule", self.engine, if_exists="append", index_label=False,
                                      index=False)
        self.db_disconnect()
        return result

    def update_schedule_by_has_taken(self):
        pass


if __name__ == '__main__':
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', None)
    conn = DBConnector()
    # result = conn.find_schedule_by_prescription_id(1)
    # conn.create_prescription_with_medication_mapping_id(5, 27733, 3, 1, 2)
    # result = conn.find_all_prescriptions_by_user_id(5)
    # result = conn.find_schedule_by_prescription_id(1)
    result = conn.create_schedule_by_prescription_id_and_taking_index_and_plan_timestamp(2, 1, 2023, 8, 29, 9, 00)
    print(result)
    result = conn.create_schedule_by_prescription_id_and_taking_index_and_plan_timestamp(2, 2, 2023, 8, 29, 13, 00)
    print(result)
    result = conn.create_schedule_by_prescription_id_and_taking_index_and_plan_timestamp(2, 3, 2023, 8, 29, 17, 00)
    print(result)

