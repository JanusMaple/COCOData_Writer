from COCODataUtility import COCODataCategories, COCODataImage, COCODataAnnotation, COCODataWriter

categories = COCODataCategories()
categories.add_category("Cabinet_Handle")
categories.add_category("Cabinet_Door")

data_writer = COCODataWriter(categories)

image = COCODataImage(360, 640, 'angle13_Color.png')
segmentation = [221,70,241,72,239,76,232,78,236,107,245,108,244,114,236,116,228,115,228,110,233,109,228,77,221,78]
annotation = COCODataAnnotation(False, 'angle13_Color.png', segmentation, 'Cabinet_Handle')
data_writer.add_image(image)
data_writer.add_annotation(annotation)

segmentation = [209,25,415,17,402,139,224,151]
annotation = COCODataAnnotation(False, 'angle13_Color.png', segmentation, 'Cabinet_Door')
data_writer.add_annotation(annotation)

segmentation = [232,151,402,147,392,239,237,231]
annotation = COCODataAnnotation(False, 'angle13_Color.png', segmentation, 'Cabinet_Door')
data_writer.add_annotation(annotation)

image = COCODataImage(360, 640, 'angle10_Color.png')
segmentation = [229,82,247,80,249,86,244,87,247,94,250,119,253,123,250,129,244,129,237,129,234,126,237,121,246,120,243,98,241,92,237,88,232,90,228,87]
annotation = COCODataAnnotation(False, 'angle10_Color.png', segmentation, 'Cabinet_Handle')
data_writer.add_image(image)
data_writer.add_annotation(annotation)

segmentation = [215,35,406,14,393,131,231,169]
annotation = COCODataAnnotation(False, 'angle10_Color.png', segmentation, 'Cabinet_Door')
data_writer.add_annotation(annotation)

segmentation = [221,152,393,139,385,230,232,246]
annotation = COCODataAnnotation(False, 'angle10_Color.png', segmentation, 'Cabinet_Door')
data_writer.add_annotation(annotation)

data_writer.write_data('output.json')