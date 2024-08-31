import init_paths
import preprocess
import images
import labels
import dataset
import ml_models

paths_info_dict, shape_info_dict, subjects_dict = init_paths.create_paths()
preprocess.create_arrays(paths_info_dict, shape_info_dict, subjects_dict)
# subjects_path_dict = paths_info_dict.get('subjects_path_dict')
# images.create_images(paths_info_dict)
labels_shape_info = labels.create_labels(paths_info_dict)
dataset = dataset.create_dataset(paths_info_dict, labels_shape_info, 'all_subs')
ml_model = ml_models.get_model(paths_info_dict)