import json
import os
import pandas as pd
class BboxToCoco:
    rectangle_list = ['K-011833', 'K-011846', 'K-011942', 'K-012003', 'K-012081', 'K-012212', 'K-012244',
                      'K-012246',
                      'K-012249', 'K-012564', 'K-012758', 'K-012767', 'K-012769', 'K-012865', 'K-013007',
                      'K-013105',
                      'K-013256', 'K-013259', 'K-013263', 'K-013326', 'K-013332', 'K-013378', 'K-013395',
                      'K-013403',
                      'K-013450', 'K-013470', 'K-013474', 'K-013592', 'K-013684', 'K-014180', 'K-014251',
                      'K-014317',
                      'K-014409', 'K-014587', 'K-014729', 'K-014986', 'K-015230', 'K-015236', 'K-015537',
                      'K-016302',
                      'K-016799', 'K-016912', 'K-017008', 'K-017040', 'K-017108', 'K-017482', 'K-017517',
                      'K-017522',
                      'K-017587', 'K-017668']
    def __init__(self, origin_path, save_path):
        super().__init__()
        self.origin_path = origin_path
        self.save_path = save_path
        self.convert_to_coco()


    def convert_to_coco(self):
        cnt_ = 1
        folder_list = os.walk(self.origin_path)
        shape_dic = {"원형": 0, "타원형": 1, "장방형": 2}
        # self.progress_bar(0, 323784)
        for root, dir, files in folder_list:
            for file in files:
                _name = file.split("_")[0]
                if _name in self.rectangle_list:
                    # self.progress_bar(cnt_, 323784)
                    file_path = os.path.join(root, file)
                    save_ = self.save_path + "\\" + file[:-5] + ".txt"
                    cnt_ += 1
                    try:
                        with open(save_, 'r', encoding='utf-8'):
                            continue
                    except:
                        with open(file_path, 'r', encoding='utf-8') as file_json:
                            data = json.load(file_json)

                            drug_type = data['images'][0]['drug_shape']
                            if drug_type in shape_dic.keys():
                                class_num = shape_dic[drug_type]
                                bbox = data['annotations'][0]['bbox']
                                img_width = data['images'][0]['width']
                                img_height = data['images'][0]['height']
                                try:
                                    x_center = bbox[0] + (bbox[2] / 2)
                                    y_center = bbox[1] + (bbox[3] / 2)
                                except:
                                    continue
                                x_center_normalized = f"{(x_center / img_width):.6f}"
                                y_center_normalized = f"{(y_center / img_height):.6f}"
                                width_normalized = f"{(bbox[2] / img_width):.6f}"
                                height_normalized = f"{(bbox[3] / img_height):.6f}"

                                normalized_bbox = [x_center_normalized, y_center_normalized, width_normalized, height_normalized]

                                result = f"{class_num} {' '.join(normalized_bbox)}"

                                with open(save_, "w", encoding="utf-8") as file_txt:
                                    file_txt.write(f"{result}")

    def progress_bar(self, progress, total):
        percent = 100 * (progress / float(total))
        bar = '■' * int(percent) + '-' * (100 - int(percent))
        print(f"\r┃{bar}┃ {percent:.2f}%", end="\r")




if __name__ == "__main__":
    orig_path = r"D:\166.약품식별 인공지능 개발을 위한 경구약제 이미지 데이터\01.데이터\1.Training\라벨링데이터\단일경구약제 5000종\label_all"
    save_path = r"D:\data_folder\obj_main\data\labels\train"
    btc = BboxToCoco(orig_path, save_path)