import init_paths
import preprocess

paths_info_dict = init_paths.create_paths()
preprocess.create_arrays(paths_info_dict)
# subjects_path_dict = paths_info_dict.get('subjects_path_dict')
