import pickle
import time
from io import BytesIO

import PIL.Image
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from database.db_connector import DBConnector

# 원형 약 목록
circle_list = ['K-011845', 'K-012080', 'K-012137', 'K-012192', 'K-012207', 'K-012256', 'K-012266', 'K-012416',
               'K-012420', 'K-012775', 'K-013020', 'K-013135', 'K-013390', 'K-013536', 'K-013829', 'K-013833',
               'K-013905', 'K-014102', 'K-014205', 'K-014224', 'K-014279', 'K-014567', 'K-014733', 'K-015257',
               'K-015499', 'K-015524', 'K-015530', 'K-015759', 'K-015989', 'K-016193', 'K-016222', 'K-016233',
               'K-016251', 'K-016394', 'K-016645', 'K-016722', 'K-016804', 'K-017057', 'K-017220', 'K-017312',
               'K-017479', 'K-017525', 'K-017574', 'K-017714', 'K-018109', 'K-018110', 'K-018114', 'K-018224',
               'K-018641', 'K-018718']
# 타원형 약 목록
ellipse_list = ['K-011982', 'K-012187', 'K-012447', 'K-012501', 'K-012502', 'K-012503', 'K-012914', 'K-013543',
                'K-013828', 'K-013900', 'K-013937', 'K-014280', 'K-015258', 'K-015270', 'K-015279', 'K-016223',
                'K-016224', 'K-016235', 'K-016250', 'K-016551', 'K-016554', 'K-016555', 'K-016736', 'K-017258',
                'K-017506', 'K-017713', 'K-018119', 'K-018203', 'K-018757', 'K-019156', 'K-019299', 'K-019469',
                'K-019699', 'K-019700', 'K-020378', 'K-020379', 'K-020805', 'K-020834', 'K-020877', 'K-021118',
                'K-021426', 'K-022095', 'K-022318', 'K-022319', 'K-022712', 'K-022713', 'K-023092', 'K-023424',
                'K-023425', 'K-023779']
# 장방향형 약 목록
rectangle_list = ['K-011833', 'K-011846', 'K-011942', 'K-012003', 'K-012081', 'K-012212', 'K-012244', 'K-012246',
                  'K-012249', 'K-012564', 'K-012758', 'K-012767', 'K-012769', 'K-012865', 'K-013007', 'K-013105',
                  'K-013256', 'K-013259', 'K-013263', 'K-013326', 'K-013332', 'K-013378', 'K-013395', 'K-013403',
                  'K-013450', 'K-013470', 'K-013474', 'K-013592', 'K-013684', 'K-014180', 'K-014251', 'K-014317',
                  'K-014409', 'K-014587', 'K-014729', 'K-014986', 'K-015230', 'K-015236', 'K-015537', 'K-016302',
                  'K-016799', 'K-016912', 'K-017008', 'K-017040', 'K-017108', 'K-017482', 'K-017517', 'K-017522',
                  'K-017587', 'K-017668']


def main():
    with open("circle_name_list.pickle", "rb") as file:
        circle_name_list = pickle.load(file)

    conn = DBConnector()

    for code in circle_list:
        image = conn.find_image_by_mapping_code(code)
        image.show()

    with open("ellipse_name_list.pickle", "rb") as file:
        ellipse_name_list = pickle.load(file)
    for name in ellipse_list:
        save_image(name)
def save_image(name):
    origin_folder_path = r"drug_images"
    conn = DBConnector()
    medi_df = conn.find_medication_by_mapping_code(name)
    print(medi_df)
    medication_id = int(medi_df["medication_id"][0])
    conn.db_connect()
    file_name = name + ".jpg"
    path = origin_folder_path + "//" + file_name
    with open(path, "rb") as f:
        binary_data = f.read()
    query = """insert into "tb_medication_image"(medication_id, image) values (%s, %s) """
    conn.cursor.execute(query, (medication_id, binary_data,))
    conn.conn.commit()
    conn.db_disconnect()

def save_name_list():
    connector = DBConnector()
    circle_name_list = get_name_list_by_mapping_code(connector, circle_list)
    ellipse_name_list = get_name_list_by_mapping_code(connector, ellipse_list)
    rectangle_name_list = get_name_list_by_mapping_code(connector, rectangle_list)

    with open("circle_name_list.pickle", "wb") as file:
        pickle.dump(circle_name_list, file)
    with open("ellipse_name_list.pickle", "wb") as file:
        pickle.dump(ellipse_name_list, file)
    with open("rectangle_name_list.pickle", "wb") as file:
        pickle.dump(rectangle_name_list, file)


def get_name_list_by_mapping_code(conn, mapping_code_list: list[str]) -> list[str]:
    name_list = list()
    for i in mapping_code_list:
        conn.db_connect()
        query = """
            select "dl_name" from "tb_medication" where "dl_mapping_code"=%s 
        """
        conn.cursor.execute(query, (i,))
        dl_name = conn.cursor.fetchone()[0]
        name_list.append(dl_name)
    return name_list


if __name__ == '__main__':
    main()
