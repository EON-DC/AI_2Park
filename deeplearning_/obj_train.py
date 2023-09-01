from ultralytics import YOLO

# import torch.optim as optim
# from apex import amp
model = YOLO("yolov8n.pt")
model = model.to("cuda")
model.train(data="../data_folder/yaml_folder/obj.yaml", epochs=20, imgsz=320, batch=4)
