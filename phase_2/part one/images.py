import numpy
import models_layers
import PIL

def create_images(paths_info_dict):
    vis_stim_aio_path = paths_info_dict.get('vis_stim_aio_path')
    eye_stim_aio_path = paths_info_dict.get('eye_stim_aio_path')
    mus_stim_aio_path = paths_info_dict.get('mus_stim_aio_path')
    path_to_vis_ersp_dataset = paths_info_dict.get('path_to_vis_ersp_dataset')
    path_to_eye_ersp_dataset = paths_info_dict.get('path_to_eye_ersp_dataset')
    path_to_mus_ersp_dataset = paths_info_dict.get('path_to_mus_ersp_dataset')
    vis_stim_strong_gamma_path = paths_info_dict.get('vis_stim_strong_gamma_path')
    eye_stim_strong_gamma_path = paths_info_dict.get('eye_stim_strong_gamma_path')
    mus_stim_strong_gamma_path = paths_info_dict.get('mus_stim_strong_gamma_path')
    path_to_selected_subs_vis_ersp_dataset = paths_info_dict.get('path_to_selected_subs_vis_ersp_dataset')
    path_to_selected_subs_eye_ersp_dataset = paths_info_dict.get('path_to_selected_subs_eye_ersp_dataset')
    path_to_selected_subs_mus_ersp_dataset = paths_info_dict.get('path_to_selected_subs_mus_ersp_dataset')
    
    
    
    ### saving the images of all the stimuluses for all the subjects
    aio_ndarray_pathes = [vis_stim_aio_path,
                          eye_stim_aio_path,
                          mus_stim_aio_path,]

    datasets_path = [path_to_vis_ersp_dataset,
                     path_to_eye_ersp_dataset,
                     path_to_mus_ersp_dataset,]

    for st in range(len(aio_ndarray_pathes)):
        temp_aio_ndarray = numpy.load(aio_ndarray_pathes[st])
        for i in range(temp_aio_ndarray.shape[0]):
            path_to_dir = datasets_path[st].joinpath(f's{i + 1}')
            if path_to_dir.exists():
                pass
            else:
                path_to_dir.mkdir()
            for j in range(temp_aio_ndarray.shape[1]):

                path_to_sub_dir = path_to_dir.joinpath(f'stimuli_type_{j + 1}')
                if path_to_sub_dir.exists():
                    pass
                else:    
                    path_to_sub_dir.mkdir()
                for x in range(temp_aio_ndarray.shape[2]):

                    path_to_file = path_to_sub_dir.joinpath(f'trial_{x + 1}.jpg')
                    img = models_layers.rescaling_layer(temp_aio_ndarray[i, j, x, ...])

                    PIL.Image.fromarray(img.numpy()).convert('L').save(path_to_file)

    del temp_aio_ndarray, aio_ndarray_pathes, datasets_path, path_to_dir, path_to_sub_dir, path_to_file
    
    
    ### saving the images of the selected stimuluses for the selected subjects
    strong_gamma_subs_ndarray_pathes = [vis_stim_strong_gamma_path,
                                        eye_stim_strong_gamma_path,
                                        mus_stim_strong_gamma_path,]

    strong_gamma_subs_datasets_path = [path_to_selected_subs_vis_ersp_dataset,
                                       path_to_selected_subs_eye_ersp_dataset,
                                       path_to_selected_subs_mus_ersp_dataset,]

    for st in range(len(strong_gamma_subs_ndarray_pathes)):
        temp_sgs_ndarray = numpy.load(strong_gamma_subs_ndarray_pathes[st])
        for i in range(temp_sgs_ndarray.shape[0]):
            path_to_dir = strong_gamma_subs_datasets_path[st].joinpath(f's{i + 1}')
            if path_to_dir.exists():
                pass
            else:
                path_to_dir.mkdir()
            for j in range(temp_sgs_ndarray.shape[1]):

                path_to_sub_dir = path_to_dir.joinpath(f'stimuli_type_{j + 1}')
                if path_to_sub_dir.exists():
                    pass
                else:    
                    path_to_sub_dir.mkdir()
                for x in range(temp_sgs_ndarray.shape[2]):

                    path_to_file = path_to_sub_dir.joinpath(f'trial_{x + 1}.jpg')
                    img = models_layers.rescaling_layer(temp_sgs_ndarray[i, j, x, ...])

                    PIL.Image.fromarray(img.numpy()).convert('L').save(path_to_file)
                
    del temp_sgs_ndarray, strong_gamma_subs_ndarray_pathes, strong_gamma_subs_datasets_path, path_to_dir, path_to_sub_dir, path_to_file            







