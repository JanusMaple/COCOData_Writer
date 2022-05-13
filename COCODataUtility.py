import json
import numpy as np

class COCODataCategories():
    def __init__(self) -> None:
        self.num_categories = 0
        self.categories = []

    def add_category(self, category_name, super_category_name = ""):
        category_dcit = {}
        category_dcit['id'] = self.num_categories
        category_dcit['name'] = category_name
        if super_category_name == "": category_dcit['supercategory'] = category_name
        else: category_dcit['supercategory'] = super_category_name
        self.categories.append(category_dcit)

        self.num_categories += 1

class COCODataImage():
    def __init__(self, height, width, file_name) -> None:
        self.height = height
        self.width = width
        self.file_name = file_name

class COCODataAnnotation():
    def __init__(self, iscrowd, file_name, segmentation, category) -> None:
        if iscrowd: self.iscrowd = 1
        else: self.iscrowd = 0
        self.file_name = file_name
        self.segmentation = segmentation
        self.category = category

class COCODataWriter():
    def __init__(self, categories: COCODataCategories) -> None:
        self.num_images = 0
        self.num_annotations = 0
        self.images = []
        self.annotations = []
        self.categories = categories.categories

        self.__file_name_to_image_id = {}

        self.__category_name_to_category_id = {}
        for category in self.categories:
            self.__category_name_to_category_id[category['name']] = category['id']
    
    def add_image(self, image: COCODataImage):
        self.num_images += 1

        image_dict = {}
        image_dict['height'] = image.height
        image_dict['width'] = image.width
        image_dict['id'] = self.num_images
        image_dict['file_name'] = image.file_name
        self.__file_name_to_image_id[image.file_name] = self.num_images
        self.images.append(image_dict)

    def add_annotation(self, annotation: COCODataAnnotation):
        self.num_annotations += 1

        annotation_dict = {}
        annotation_dict['iscrowd'] = annotation.iscrowd
        annotation_dict['image_id'] = self.__file_name_to_image_id[annotation.file_name]
        bbox_x_min = int(np.min(annotation.segmentation[::2]))
        bbox_x_max = int(np.max(annotation.segmentation[::2]))
        bbox_y_min = int(np.min(annotation.segmentation[1::2]))
        bbox_y_max = int(np.max(annotation.segmentation[1::2]))
        annotation_dict['bbox'] = [bbox_x_min, bbox_y_min, bbox_x_max - bbox_x_min, bbox_y_max - bbox_y_min]
        annotation_dict['segmentation'] = [annotation.segmentation]
        annotation_dict['category_id'] = self.__category_name_to_category_id[annotation.category]
        annotation_dict['id'] = self.num_annotations
        point_num = int(len(annotation.segmentation) / 2)
        area = annotation.segmentation[point_num * 2 - 2] * annotation.segmentation[1] - annotation.segmentation[0] * annotation.segmentation[point_num * 2 - 1]
        for i in range(1, point_num):
            area += annotation.segmentation[i * 2 - 2] * annotation.segmentation[(i + 1)  * 2 - 1] - annotation.segmentation[i * 2 - 1] * annotation.segmentation[(i + 1) * 2 - 2]
        annotation_dict['area'] = int(abs(area / 2.0))
        self.annotations.append(annotation_dict)

    def write_data(self, file_name):
        data_file = open(file_name, "w")
        data = {}
        data['images'] = self.images
        data['annotations'] = self.annotations
        data['categories'] = self.categories
        data_file.write(json.dumps(data))
        data_file.close()