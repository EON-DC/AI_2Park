import yaml

with open("../model/cls_circle.yaml", 'r', encoding='utf-8') as file:
    circle_dict = yaml.safe_load(file, )

with open("../model/cls_ellipse.yaml", 'r', encoding='utf-8') as file:
    ellipse_dict = yaml.safe_load(file, )


def get_mapping_code_from_yaml(cls_num, shape_type):
    if shape_type == "ellipse":
        return "K-0" + ellipse_dict["names"][cls_num]
    elif shape_type == "circle":
        return "K-0" + circle_dict["names"][cls_num]
