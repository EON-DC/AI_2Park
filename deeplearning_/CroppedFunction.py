import os

from PIL import Image


class CroppedFunction():
    def __init__(self):
        super().__init__()
        self.slice_ = '\\'

    def run(self, orig_path, img_show=False, bbox_path=None, crop_show=False, save_path=None):
        """
        :param orig_path: 오리지널 이미지를 포함한 폴더 경로
        :param img_show: 이미지 확인 여부
        :param bbox_path: bbox데이터가 담긴 json 폴더 경로
        :param crop_show: 잘린 이미지 확인 여부
        :param save_path: 저장 경로
        :return: None, 없음
        """
        img_list, name = self.img_open(orig_path, img_show)
        self.save_cropped_images(bbox_path, save_path, name, img_list, crop_show)

    def img_open(self, orig_path, show=False):
        """
        :param orig_path: imgfolder path / 이미지를 포함하고있는 디렉터리 경로
        :param show: 이미지 확인 여부 default=False
        :return: img_list = [img1_path, img2_path....] / 이미지 경로를 포함하는 리스트
        """
        print("Start...ImageRead..")

        orig_img_file, name = self.foler_walk(orig_path)  # 해당 폴더 오픈(폴더 내부 파일 읽어오기)
        if show:
            for img_path in orig_img_file:
                img_ = Image.open(img_path)
                img_.show()
        return orig_img_file, name

    def image_check(self, img_list=type[list], show_cnt=1):
        """
        :param img_list: [img_1_path, img_2_path...] 이미지를 담아주는 리스트
        :param show_cnt: img_list[index], show_count 몇 개의 이미지를 확인하는지 카운트
        :return:
        """
        for img in img_list[:show_cnt]:
            img.show()

    def save_cropped_images(self, bbox_path, save_path, save_name, orig_img_list=type[list], crop_show=False):
        """
        :parameter
        bbox_path: bbox 데이터를 포함하는 json 폴더 경로
        orig_img: 오리지널 이미지
        crop_show: 잘린 이미지 확인하기 Default=False
        :return crop_img_list = [crop_img1, crop_img2...]
        """
        crop_size_list, name = self.foler_walk(bbox_path)
        print("Start saving the cropped image")
        total_img_number = len(orig_img_list)
        cnt_img = 1
        os.system('cls')
        self.progress_bar(0, total_img_number)
        for orig_img_path, cr_size, sv_nm in zip(orig_img_list, crop_size_list, save_name):
            self.progress_bar(cnt_img, total_img_number)
            orig_img = Image.open(orig_img_path)
            crop_img = orig_img.crop(cr_size)  # left, upper, right, lower
            self.image_save(save_path, crop_img, sv_nm)
            if crop_show:
                self.image_check(crop_img)
            cnt_img += 1
        print("Save_completed")

    def image_save(self, save_path, cropped_img, save_name):
        """
        :param save_path: 저장 경로
        :param cropped_img: 자른 이미지
        :return: None: 리턴값 없음
        """
        save_img_path = save_path + self.slice_ + save_name
        cropped_img.save(save_img_path)

    def foler_walk(self, path):
        """
        :param path: 하위 디렉터리 파일 을 포함하는 디렉터리 경로
        :return: 'png' or 'json' 데이터 리스트 리턴
        """
        list_ = list()
        name_ = list()
        # folder_list = os.walk(path)
        folder_list = os.listdir(path)
        print("reading", folder_list)
        for folde in folder_list:
            fol_path = path + self.slice_ + folde
            folde = os.walk(fol_path)
            for root, dirs, files in folde:
                # files: 하위 폴더
                for file in files:
                    # file: 하위 폴더 내 파일
                    file_path = os.path.join(root, file)
                    # file_path: 파일 경로
                    if "json" in file_path:
                        with open(file_path, 'r', encoding='utf-8') as file_json:
                            import json
                            data = json.load(file_json)
                            bbox = data['annotations'][0]['bbox']
                            left = bbox[0]
                            upper = bbox[1]
                            right = bbox[2] + left
                            lower = bbox[3] + upper
                            crop_size = (left, upper, right, lower)
                            print(f"read->{file}:{crop_size}")
                            list_.append(crop_size)
                    elif "png" in file_path:
                        list_.append(file_path)
                        name_.append(file)
            if "png" in list_[0]:
                print("Image read Clear")
            else:
                print("Json read Clear")
        return list_, name_

    def progress_bar(self, progress, total):
        percent = 100 * (progress / float(total))
        bar = '■' * int(percent) + '-' * (100 - int(percent))
        print(f"\r┃{bar}┃ {percent:.2f}%", end="\r")



if __name__ == '__main__':
    # orig_path_ = r"D:\166.약품식별 인공지능 개발을 위한 경구약제 이미지 데이터\01.데이터\1.Training\원천데이터\단일경구약제 5000종\TS_7_단일"
    orig_path_ = r"D:\166.약품식별 인공지능 개발을 위한 경구약제 이미지 데이터\01.데이터\1.Training\원천데이터\단일경구약제 5000종\새 폴더"
    # bbox_path_ = r"D:\166.약품식별 인공지능 개발을 위한 경구약제 이미지 데이터\01.데이터\1.Training\라벨링데이터\단일경구약제 5000종\TL_7_단일"
    bbox_path_ = r"D:\166.약품식별 인공지능 개발을 위한 경구약제 이미지 데이터\01.데이터\1.Training\라벨링데이터\단일경구약제 5000종\새 폴더"
    save_path_ = r"D:\166.약품식별 인공지능 개발을 위한 경구약제 이미지 데이터\01.데이터\1.Training\테스트데이터\단일경구약제 5000종\all_crop_img"
    crop_test = CroppedFunction()
    crop_test.run(orig_path_, bbox_path=bbox_path_, save_path=save_path_)
