from model_segmentation_class import SegmentationModel
from model_classification_class import ResnetModel


if __name__ == '__main__':
    # tif_path = 'example/177_TIRADS5_cross.tif'
    # model_type = 'cross'
    tif_path = 'example/87_TIRADS4_long.tif'
    model_type = 'long'

    s_model = SegmentationModel(model_type)
    s_model.predict(tif_path)
    s_model.save_tif(tif_path)  # save tif without bboxes & classes

    c_model = ResnetModel(model_type)
    c_model.predict(s_model.rois, s_model.img_type) 
    c_model.save_tif_with_class(tif_path, s_model.result_masks, s_model.bbox_coordinates) # save tif with bboxes & classes
