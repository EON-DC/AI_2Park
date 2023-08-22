import os

if __name__ == '__main__':
    # qrc 써야하면 쓸 예정
    os.system(f"pyrcc5 src/my_qrc.qrc -o compiled/my_qrc_rc.py")

    # 디렉터리 파일 리스트 조회 및 변환
    ui_file_list = os.listdir(r"ui_files")
    for file_name in ui_file_list:
        os.system(f'python -m PyQt5.uic.pyuic --import=gui.compiled ui_files/{file_name} -o compiled/compiled_{file_name[:-3]}.py')
