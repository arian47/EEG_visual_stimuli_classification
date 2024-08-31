import pathlib
import scipy

path_to_matlab_files = pathlib.Path("data collected/single trial ersps/unpacked")

def get_mat_files_path():
    # path to directory that will hold images of the subjects ERSP trials
    assert path_to_matlab_files.exists()
    mat_files_path = list(path_to_matlab_files.glob('**/*.mat'))
    return mat_files_path

def get_base_path():
    mat_files_path = get_mat_files_path()
    # file paths which will hold all the ersp data for each muscle or trigger group
    x = '/'.join(mat_files_path[0].parts[1:-4])
    x = mat_files_path[0].parts[0] + x
    x = pathlib.Path(x)
    return x


def create_paths():
    vis_stim_aio_path = get_base_path().joinpath('visual_stimuli_ersps_in_one.npy')
    mus_stim_aio_path = get_base_path().joinpath('muscle_stimuli_ersps_in_one.npy')
    eye_stim_aio_path = get_base_path().joinpath('eyes_stimuli_ersps_in_one.npy')
    vis_stim_aio_labels_path = get_base_path().joinpath('visual_stimuli_ersps_in_one_labels.npy')
    mus_stim_aio_labels_path = get_base_path().joinpath('muscle_stimuli_ersps_in_one_labels.npy')
    eye_stim_aio_labels_path = get_base_path().joinpath('eyes_stimuli_ersps_in_one_labels.npy')

    # file paths which contain the ersps for subjects with strong gamma response only needed for classification later
    vis_stim_strong_gamma_path = get_base_path().joinpath('vis_stim_strong_gamma_response_subjects.npy')
    mus_stim_strong_gamma_path = get_base_path().joinpath('mus_stim_strong_gamma_response_subjects.npy')
    eye_stim_strong_gamma_path = get_base_path().joinpath('eye_stim_strong_gamma_response_subjects.npy')
    vis_stim_strong_gamma_labels_path = get_base_path().joinpath('vis_stim_strong_gamma_response_subjects_labels.npy')
    mus_stim_strong_gamma_labels_path = get_base_path().joinpath('mus_stim_strong_gamma_response_subjects_labels.npy')
    eye_stim_strong_gamma_labels_path = get_base_path().joinpath('eye_stim_strong_gamma_response_subjects_labels.npy')

    ### file paths which will contain ersps for all subjects and average of time domain
    vis_stim_aio_average_td_fh_path = get_base_path().joinpath('visual_stimuli_ersps_in_one_average_td_first_half.npy')
    vis_stim_aio_average_td_sh_path = get_base_path().joinpath('visual_stimuli_ersps_in_one_average_td_second_half.npy')
    vis_stim_aio_average_td_path = get_base_path().joinpath('visual_stimuli_ersps_in_one_average_td.npy')
    mus_stim_aio_average_td_path = get_base_path().joinpath('muscle_stimuli_ersps_in_one_average_td.npy')
    eye_stim_aio_average_td_path = get_base_path().joinpath('eyes_stimuli_ersps_in_one_average_td.npy')


    subjects_path_dict = {}
    mat_files_path = get_mat_files_path()
    for i in range(1, int(len(mat_files_path) / 3) + 1):
        subjects_path_dict['s' + str(i)] = {}

    for i in range(1, int(len(mat_files_path) / 3) + 1):
        temp_pathes = [x for x in mat_files_path if int(x.parts[-2][1:]) == i]
        for j in range(len(temp_pathes)):
            temp_val = temp_pathes.pop()
            if temp_val.parts[-1].find('vis') != -1:
                temp_vis_path = temp_val
            elif temp_val.parts[-1].find('eyes') != -1:
                temp_eye_path = temp_val
            elif temp_val.parts[-1].find('muscle') != -1:
                temp_mus_path = temp_val

        subjects_path_dict['s' + str(i)]['vis_ersp'] = temp_vis_path
        subjects_path_dict['s' + str(i)]['muscle_ersp'] = temp_mus_path
        subjects_path_dict['s' + str(i)]['eyes_ersp'] = temp_eye_path
        

    # defining dict holding the pathes of the selected subjects
    strong_gamma_response_subjects_data_dir_path_dict = {}
    subjects_of_interest = [1, 4, 8, 9, 10, 12, 13, 14, 18, 20, 22, 23, 24, 25, 27, 31,]

    select_mat_files_path = [x for x in mat_files_path if int(x.parent.parts[-1][1:]) in subjects_of_interest]

    for i in range(len(subjects_of_interest)):
        strong_gamma_response_subjects_data_dir_path_dict['s' + str(subjects_of_interest[i])] = {}

    for i in subjects_of_interest:
        temp_pathes = [x for x in select_mat_files_path if int(x.parts[-2][1:]) == i]
        for j in range(len(temp_pathes)):
            temp_val = temp_pathes.pop()
            if temp_val.parts[-1].find('vis') != -1:
                temp_vis_path = temp_val
            elif temp_val.parts[-1].find('eyes') != -1:
                temp_eye_path = temp_val
            elif temp_val.parts[-1].find('muscle') != -1:
                temp_mus_path = temp_val

        strong_gamma_response_subjects_data_dir_path_dict['s' + str(i)]['vis_ersp'] = temp_vis_path
        strong_gamma_response_subjects_data_dir_path_dict['s' + str(i)]['muscle_ersp'] = temp_mus_path
        strong_gamma_response_subjects_data_dir_path_dict['s' + str(i)]['eyes_ersp'] = temp_eye_path
        
    s1_vis = subjects_path_dict['s1']['vis_ersp']
    s1_mus = subjects_path_dict['s1']['muscle_ersp']
    s1_eye = subjects_path_dict['s1']['eyes_ersp']
    s1_vis_shape = scipy.io.loadmat(s1_vis)['mstersp'].shape
    s1_mus_shape = scipy.io.loadmat(s1_mus)['mstersp'].shape
    s1_eye_shape = scipy.io.loadmat(s1_eye)['mstersp'].shape
    del s1_vis, s1_mus, s1_eye

    s1_sgr_vis = strong_gamma_response_subjects_data_dir_path_dict['s1']['vis_ersp']
    s1_sgr_mus = strong_gamma_response_subjects_data_dir_path_dict['s1']['muscle_ersp']
    s1_sgr_eye = strong_gamma_response_subjects_data_dir_path_dict['s1']['eyes_ersp']
    s1_sgr_vis_shape = scipy.io.loadmat(s1_sgr_vis)['mstersp'].shape
    s1_sgr_mus_shape = scipy.io.loadmat(s1_sgr_mus)['mstersp'].shape
    s1_sgr_eye_shape = scipy.io.loadmat(s1_sgr_eye)['mstersp'].shape
    del s1_sgr_vis, s1_sgr_mus, s1_sgr_eye

    ### defining the pathes which will hold the original dataset
    path_to_single_trial_ersps_dataset = pathlib.Path("analyzed data/single_trial_ersps_dataset/")
    path_to_vis_ersp_dataset = pathlib.Path("analyzed data/single_trial_ersps_dataset/visual_stimuli")
    path_to_mus_ersp_dataset = pathlib.Path("analyzed data/single_trial_ersps_dataset/muscle_stimuli")
    path_to_eye_ersp_dataset = pathlib.Path("analyzed data/single_trial_ersps_dataset/eyes_stimuli")

    ### defining the pathes which will hold the selected subjects with strong gamma response dataset
    path_to_selected_subs_single_trial_ersps_dataset = pathlib.Path("analyzed data/selected_subjects_single_trial_ersps_dataset/")
    path_to_selected_subs_vis_ersp_dataset = pathlib.Path("analyzed data/selected_subjects_single_trial_ersps_dataset/visual_stimuli")
    path_to_selected_subs_mus_ersp_dataset = pathlib.Path("analyzed data/selected_subjects_single_trial_ersps_dataset/muscle_stimuli")
    path_to_selected_subs_eye_ersp_dataset = pathlib.Path("analyzed data/selected_subjects_single_trial_ersps_dataset/eyes_stimuli")
    
    paths_to_create = [
        path_to_single_trial_ersps_dataset,
        path_to_vis_ersp_dataset,
        path_to_mus_ersp_dataset,
        path_to_eye_ersp_dataset,
        path_to_selected_subs_single_trial_ersps_dataset,
        path_to_selected_subs_vis_ersp_dataset,
        path_to_selected_subs_mus_ersp_dataset,
        path_to_selected_subs_eye_ersp_dataset,
    ]
    
    for i in paths_to_create:
        if not i.exists():
            i.mkdir()
    
    # if path_to_single_trial_ersps_dataset.exists():
    #     pass
    # else:
    #     path_to_single_trial_ersps_dataset.mkdir()
    # if path_to_vis_ersp_dataset.exists():
    #     pass
    # else:
    #     path_to_vis_ersp_dataset.mkdir()
    # if path_to_mus_ersp_dataset.exists():
    #     pass
    # else:
    #     path_to_mus_ersp_dataset.mkdir()
    # if path_to_eye_ersp_dataset.exists():
    #     pass
    # else:
    #     path_to_eye_ersp_dataset.mkdir()
        
    # if path_to_selected_subs_single_trial_ersps_dataset.exists():
    #     pass
    # else:
    #     path_to_selected_subs_single_trial_ersps_dataset.mkdir()
    # if path_to_selected_subs_vis_ersp_dataset.exists():
    #     pass
    # else:
    #     path_to_selected_subs_vis_ersp_dataset.mkdir()
    # if path_to_selected_subs_mus_ersp_dataset.exists():
    #     pass
    # else:
    #     path_to_selected_subs_mus_ersp_dataset.mkdir()
    # if path_to_selected_subs_eye_ersp_dataset.exists():
    #     pass
    # else:
    #     path_to_selected_subs_eye_ersp_dataset.mkdir()

    paths_info_dict = dict(
        path_to_matlab_files=path_to_matlab_files,
        mat_files_path=mat_files_path,
        vis_stim_aio_path=vis_stim_aio_path,
        mus_stim_aio_path=mus_stim_aio_path,
        eye_stim_aio_path=eye_stim_aio_path,
        vis_stim_aio_labels_path=vis_stim_aio_labels_path,
        mus_stim_aio_labels_path=mus_stim_aio_labels_path,
        eye_stim_aio_labels_path=eye_stim_aio_labels_path,
        vis_stim_strong_gamma_path=vis_stim_strong_gamma_path,
        mus_stim_strong_gamma_path=mus_stim_strong_gamma_path,
        eye_stim_strong_gamma_path=eye_stim_strong_gamma_path,
        vis_stim_strong_gamma_labels_path=vis_stim_strong_gamma_labels_path,
        mus_stim_strong_gamma_labels_path=mus_stim_strong_gamma_labels_path,
        eye_stim_strong_gamma_labels_path=eye_stim_strong_gamma_labels_path,
        vis_stim_aio_average_td_fh_path=vis_stim_aio_average_td_fh_path,
        vis_stim_aio_average_td_sh_path=vis_stim_aio_average_td_sh_path,
        vis_stim_aio_average_td_path=vis_stim_aio_average_td_path,
        mus_stim_aio_average_td_path=mus_stim_aio_average_td_path,
        eye_stim_aio_average_td_path=eye_stim_aio_average_td_path,
        path_to_single_trial_ersps_dataset=path_to_single_trial_ersps_dataset,
        path_to_vis_ersp_dataset=path_to_vis_ersp_dataset,
        path_to_mus_ersp_dataset=path_to_mus_ersp_dataset,
        path_to_eye_ersp_dataset=path_to_eye_ersp_dataset,
        path_to_selected_subs_single_trial_ersps_dataset=path_to_selected_subs_single_trial_ersps_dataset,
        path_to_selected_subs_vis_ersp_dataset=path_to_selected_subs_vis_ersp_dataset,
        path_to_selected_subs_mus_ersp_dataset=path_to_selected_subs_mus_ersp_dataset,
        path_to_selected_subs_eye_ersp_dataset=path_to_selected_subs_eye_ersp_dataset
    )
    shape_info_dict = dict(
        s1_vis_shape=s1_vis_shape,
        s1_mus_shape=s1_mus_shape,
        s1_eye_shape=s1_eye_shape,
        s1_sgr_vis_shape=s1_sgr_vis_shape,
        s1_sgr_mus_shape=s1_sgr_mus_shape,
        s1_sgr_eye_shape=s1_sgr_eye_shape,
    )
    subjects_dict = dict(
        subjects_path_dict=subjects_path_dict,
        strong_gamma_response_subjects_data_dir_path_dict=strong_gamma_response_subjects_data_dir_path_dict,
        subjects_of_interest=subjects_of_interest,
    )
    
    return paths_info_dict, shape_info_dict, subjects_dict