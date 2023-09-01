import queue
import sys
import threading

import PIL.Image
import cv2
import numpy
import numpy as np
from ultralytics import YOLO

data_queue = queue.Queue()
send_data_queue = queue.Queue()
# circle_model = YOLO("./runs/detect/train/weights/best.pt")
# ellipsis_model = YOLO("./runs/detect/train2/weights/best.pt")
# rectangle_model = YOLO("./runs/detect/ObjectDetection/weights/best.pt")
# model_list = [circle_model, ellipsis_model, rectangle_model]
model_list = []

numpy.set_printoptions(threshold=sys.maxsize)
def cam_start():
    detection_model = YOLO("runs/detect/ObjectDetection/weights/best.pt")
    results = detection_model.predict(source="0", show=True, stream=True, conf=0.3, verbose=False)
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        print(boxes.cls)
        if len(boxes.cls) > 0:
            img_array = r.orig_img.copy()
            # data_list = [boxes.data, img_array]
            # data_queue.put(data_list)


def read_data(pretrained_model):
    while True:
        try:
            boxes_data, orig_img = data_queue.get(timeout=3)  # 큐에서 데이터를 가져옴 (1초 대기)
            while not data_queue.empty():
                data_queue.get()
            fix_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)
            _, crop_img = draw_boxes_and_crop(fix_img, boxes_data)
            for idx, cropped_img in enumerate(crop_img):
                # alpha_channel = np.ones(cropped_img.shape[:2], dtype=cropped_img.dtype)
                # four_channel_img = cv2.merge([cropped_img, alpha_channel])
                # cropped_img = PIL.Image.fromarray(four_channel_img)
                from img_resize import classification_img
                cropped_img = PIL.Image.fromarray(cropped_img)
                preproccessed_img = classification_img(cropped_img, 128)
                image_as_np = np.array(preproccessed_img)
                img_list = [image_as_np]
                img_list_as_np = np.array(img_list)
                print(pretrained_model)
                # result = pretrained_model.predict(np.array(img_list_as_np))
                # print("result: ", *result)
                #
                # if np.argmax(result) > 0.9:
                #     predict_result = np.round(result)
                #     predict_classes = predict_result.argmax(axis=1)
                #     with open(r"labelencoder.pickle", "rb") as file:
                #         encoder = pickle.load(file)
                #         orgin_label = encoder.inverse_transform(predict_classes)
                #         print(orgin_label)
        except queue.Empty:
            pass

def draw_boxes_and_crop(image, tensor):
    cropped_images = []
    for detection in tensor:
        x1, y1, x2, y2 = map(int, detection[:4])
        confidence = detection[4]
        class_id = int(detection[5])
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"Class {class_id} : {confidence:.2f}"
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cropped = image[y1:y2, x1:x2]
        cropped_images.append(cropped)
    return image, cropped_images

if __name__ == '__main__':
    cam_start_thread = threading.Thread(target=cam_start)
    read_data_thread = threading.Thread(target=read_data, args=(model_list, ))

    cam_start_thread.start()
    read_data_thread.start()

    cam_start_thread.join()
    read_data_thread.join()