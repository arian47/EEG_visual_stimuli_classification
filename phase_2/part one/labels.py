import numpy


def create_labels(paths_info_dict):
    vis_stim_aio_labels_path = paths_info_dict.get('vis_stim_aio_labels_path')
    vis_stim_aio_path = paths_info_dict.get('vis_stim_aio_path')
    mus_stim_aio_path = paths_info_dict.get('mus_stim_aio_path')
    mus_stim_aio_labels_path = paths_info_dict.get('mus_stim_aio_labels_path')
    eye_stim_aio_path = paths_info_dict.get('eye_stim_aio_path')
    eye_stim_aio_labels_path = paths_info_dict.get('eye_stim_aio_labels_path')
    vis_stim_strong_gamma_path = paths_info_dict.get('vis_stim_strong_gamma_path')
    vis_stim_strong_gamma_labels_path = paths_info_dict.get('vis_stim_strong_gamma_labels_path')
    mus_stim_strong_gamma_path = paths_info_dict.get('mus_stim_strong_gamma_path')
    mus_stim_strong_gamma_labels_path = paths_info_dict.get('mus_stim_strong_gamma_labels_path')
    eye_stim_strong_gamma_path = paths_info_dict.get('eye_stim_strong_gamma_path')
    eye_stim_strong_gamma_labels_path = paths_info_dict.get('eye_stim_strong_gamma_labels_path')
    
    ### creating labels for all of the subjects numpy.ndarray objs
    vis_stim_aio_file_flag = False
    vis_stim_aio_labels_file_flag = False
    
    if vis_stim_aio_path.is_file():
        visual_stimuli_ersps_in_one = numpy.load(vis_stim_aio_path)
        vis_stim_aio_file_flag = True
        
    if vis_stim_aio_labels_path.is_file():
        vis_stim_aio_labels_file_flag = True
        
    if not vis_stim_aio_file_flag:
        raise FileNotFoundError('The visual stimuli file was not found!')
    
    if not vis_stim_aio_labels_file_flag:
        print('first time creating labels for visual stimuli')

        vis_labels = []

        for i in range(visual_stimuli_ersps_in_one.shape[0]): # run 31 times
            for j in range(visual_stimuli_ersps_in_one.shape[1]): # run 6 times
                for x in range(visual_stimuli_ersps_in_one.shape[2]): # run 135 times
                    if j == 0:
                        vis_labels.append(0) # 100% contrast
                    elif j == 1:
                        vis_labels.append(1) # 5% contrast
                    elif j == 2:
                        vis_labels.append(2) # '33% contrast'
                    elif j == 3:
                        vis_labels.append(3) # 'plaid'
                    elif j == 4:
                        vis_labels.append(4) # '10% random'
                    elif j == 5:
                        vis_labels.append(5) # '60% random'
                    else:
                        raise Exception("not possible!")

        vis_labels = numpy.array(vis_labels)
        numpy.save(vis_stim_aio_labels_path, 
                   vis_labels)
        del vis_labels
        
    visual_stimuli_ersps_in_one_shape = visual_stimuli_ersps_in_one.shape
    del visual_stimuli_ersps_in_one, vis_stim_aio_labels_file_flag, vis_stim_aio_file_flag

    mus_stim_aio_file_flag = False
    mus_stim_aio_labels_file_flag = False
    if mus_stim_aio_path.is_file():
        muscle_stimuli_ersps_in_one = numpy.load(mus_stim_aio_path)
        mus_stim_aio_file_flag = True
    if mus_stim_aio_labels_path.is_file():
        mus_stim_aio_labels_file_flag = True
    if not mus_stim_aio_file_flag:
        raise FileNotFoundError('The muscle stimuli file was not found!')
    if not mus_stim_aio_labels_file_flag:
        print('first time creating labels for muscle stimuli')
        mus_labels = []
        for i in range(muscle_stimuli_ersps_in_one.shape[0]): # run 31 times
            for j in range(muscle_stimuli_ersps_in_one.shape[1]): # run 6 times
                for x in range(muscle_stimuli_ersps_in_one.shape[2]): # run 135 times
                    if j == 0:
                        mus_labels.append(0) # 100% contrast
                    elif j == 1:
                        mus_labels.append(1) # 5% contrast
                    elif j == 2:
                        mus_labels.append(2) # '33% contrast'
                    elif j == 3:
                        mus_labels.append(3) # 'plaid'
                    elif j == 4:
                        mus_labels.append(4) # '10% random'
                    elif j == 5:
                        mus_labels.append(5) # '60% random'
                    else:
                        raise Exception("not possible!")
        mus_labels = numpy.array(mus_labels)
        numpy.save(mus_stim_aio_labels_path,
                   mus_labels)
        del mus_labels

    muscle_stimuli_ersps_in_one_shape = muscle_stimuli_ersps_in_one.shape    
    del muscle_stimuli_ersps_in_one, mus_stim_aio_labels_file_flag, mus_stim_aio_file_flag

    eye_stim_aio_file_flag = False
    eye_stim_aio_labels_file_flag = False
    if eye_stim_aio_path.is_file():
        eyes_stimuli_ersps_in_one = numpy.load(eye_stim_aio_path)
        eye_stim_aio_file_flag = True
    if eye_stim_aio_labels_path.is_file():
        eye_stim_aio_labels_file_flag = True
    if not eye_stim_aio_file_flag:
        raise FileNotFoundError('The eyes stimuli file was not found!')
    if not eye_stim_aio_labels_file_flag:
        print('first time creating labels for eyes stimuli') 
        eye_labels = []
        for i in range(eyes_stimuli_ersps_in_one.shape[0]): # run 31 times
            for j in range(eyes_stimuli_ersps_in_one.shape[1]): # run 6 times
                for x in range(eyes_stimuli_ersps_in_one.shape[2]): # run 135 times
                    if j == 0:
                        eye_labels.append(0) # 100% contrast
                    elif j == 1:
                        eye_labels.append(1) # 5% contrast
                    elif j == 2:
                        eye_labels.append(2) # '33% contrast'
                    elif j == 3:
                        eye_labels.append(3) # 'plaid'
                    elif j == 4:
                        eye_labels.append(4) # '10% random'
                    elif j == 5:
                        eye_labels.append(5) # '60% random'
                    else:
                        raise Exception("not possible!")
        eye_labels = numpy.array(eye_labels)
        numpy.save(eye_stim_aio_labels_path, 
                   eye_labels)
        del eye_labels

    eyes_stimuli_ersps_in_one_shape = eyes_stimuli_ersps_in_one.shape
    del eyes_stimuli_ersps_in_one, eye_stim_aio_file_flag, eye_stim_aio_labels_file_flag
    
    ### creating labels only for the selected subjects
    vis_stim_strong_gamma_file_flag = False
    vis_stim_strong_gamma_labels_file_flag = False
    if vis_stim_strong_gamma_path.is_file():
        visual_stimuli_selected_subjects_ersps = numpy.load(vis_stim_strong_gamma_path)
        vis_stim_strong_gamma_file_flag = True
    if vis_stim_strong_gamma_labels_path.is_file():
        vis_stim_strong_gamma_labels_file_flag = True
    if not vis_stim_strong_gamma_file_flag:
        raise FileNotFoundError('The visual stimuli for strong gamma response subjects file was not found!')
    if not vis_stim_strong_gamma_labels_file_flag:
        print('first time creating labels for visual stimuli for strong gamma response subjects')

        selected_subs_vis_labels = []
        for i in range(visual_stimuli_selected_subjects_ersps.shape[0]): # 16 selected subjects
            for j in range(visual_stimuli_selected_subjects_ersps.shape[1]): # two stimuli
                for x in range(visual_stimuli_selected_subjects_ersps.shape[2]): # 135 trials
                    if j == 0:
                        selected_subs_vis_labels.append(0) # 100% contrast
                    elif j == 1:
                        selected_subs_vis_labels.append(1) # 5% contrast
                    else:
                        raise Exception("not possible!")
        selected_subs_vis_labels = numpy.array(selected_subs_vis_labels)
        numpy.save(vis_stim_strong_gamma_labels_path, 
                   selected_subs_vis_labels)
        del selected_subs_vis_labels

    visual_stimuli_selected_subjects_ersps_shape = visual_stimuli_selected_subjects_ersps.shape
    del visual_stimuli_selected_subjects_ersps, vis_stim_strong_gamma_file_flag, vis_stim_strong_gamma_labels_file_flag

    mus_stim_strong_gamma_file_flag = False
    mus_stim_strong_gamma_labels_file_flag = False
    if mus_stim_strong_gamma_path.is_file():
        muscle_stimuli_selected_subjects_ersps = numpy.load(mus_stim_strong_gamma_path)
        mus_stim_strong_gamma_file_flag = True
    if mus_stim_strong_gamma_labels_path.is_file():
        # selected_subs_mus_labels = numpy.load(mus_stim_strong_gamma_labels_path)
        mus_stim_strong_gamma_labels_file_flag = True
    if not mus_stim_strong_gamma_file_flag:
        raise FileNotFoundError('The muscle stimuli for strong gamma response subjects file was not found!')
    if not mus_stim_strong_gamma_labels_file_flag:
        print('first time creating labels for muscle stimuli for strong gamma response subjects')
        
        selected_subs_mus_labels = []
        for i in range(muscle_stimuli_selected_subjects_ersps.shape[0]): # 16 selected subjects
            for j in range(muscle_stimuli_selected_subjects_ersps.shape[1]): # two stimuli
                for x in range(muscle_stimuli_selected_subjects_ersps.shape[2]): # 135 trials
                    if j == 0:
                        selected_subs_mus_labels.append(0) # 100% contrast
                    elif j == 1:
                        selected_subs_mus_labels.append(1) # 5% contrast
                    else:
                        raise Exception("not possible!")
        selected_subs_mus_labels = numpy.array(selected_subs_mus_labels)
        numpy.save(mus_stim_strong_gamma_labels_path, 
                   selected_subs_mus_labels)
        del selected_subs_mus_labels

    muscle_stimuli_selected_subjects_ersps_shape = muscle_stimuli_selected_subjects_ersps.shape    
    del muscle_stimuli_selected_subjects_ersps, mus_stim_strong_gamma_file_flag, mus_stim_strong_gamma_labels_file_flag


    eye_stim_strong_gamma_file_flag = False
    eye_stim_strong_gamma_labels_file_flag = False
    if eye_stim_strong_gamma_path.is_file():
        eyes_stimuli_selected_subjects_ersps = numpy.load(eye_stim_strong_gamma_path)
        eye_stim_strong_gamma_file_flag = True
    if eye_stim_strong_gamma_labels_path.is_file():
        # selected_subs_eye_labels = numpy.load(eye_stim_strong_gamma_labels_path)
        eye_stim_strong_gamma_labels_file_flag = True
    if not eye_stim_strong_gamma_file_flag:
        raise FileNotFoundError('The eyes stimuli for strong gamma response subjects file was not found!')
    if not eye_stim_strong_gamma_labels_file_flag:
        print('first time creating labels for eyes stimuli for strong gamma response subjects')
        
        selected_subs_eye_labels = []
        for i in range(eyes_stimuli_selected_subjects_ersps.shape[0]): # 16 selected subjects
            for j in range(eyes_stimuli_selected_subjects_ersps.shape[1]): # two stimuli
                for x in range(eyes_stimuli_selected_subjects_ersps.shape[2]): # 135 trials
                    if j == 0:
                        selected_subs_eye_labels.append(0) # 100% contrast
                    elif j == 1:
                        selected_subs_eye_labels.append(1) # 5% contrast
                    else:
                        raise Exception("not possible!")
        selected_subs_eye_labels = numpy.array(selected_subs_eye_labels)
        numpy.save(eye_stim_strong_gamma_labels_path, 
                   selected_subs_eye_labels)
        del selected_subs_eye_labels

    eyes_stimuli_selected_subjects_ersps_shape = eyes_stimuli_selected_subjects_ersps.shape
    del eyes_stimuli_selected_subjects_ersps, eye_stim_strong_gamma_file_flag, eye_stim_strong_gamma_labels_file_flag

    labels_shape_info = dict(
        visual_stimuli_ersps_in_one_shape=visual_stimuli_ersps_in_one_shape,
        muscle_stimuli_ersps_in_one_shape=muscle_stimuli_ersps_in_one_shape,
        eyes_stimuli_ersps_in_one_shape=eyes_stimuli_ersps_in_one_shape,
        visual_stimuli_selected_subjects_ersps_shape=visual_stimuli_selected_subjects_ersps_shape,
        muscle_stimuli_selected_subjects_ersps_shape=muscle_stimuli_selected_subjects_ersps_shape,
        eyes_stimuli_selected_subjects_ersps_shape=eyes_stimuli_selected_subjects_ersps_shape
    )
    return labels_shape_info





