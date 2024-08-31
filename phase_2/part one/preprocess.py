import numpy
import scipy

def create_arrays(info_dict, shape_info_dict, subjects_dict):
    subjects_path_dict = subjects_dict.get('subjects_path_dict')
    
    s1_vis_shape = shape_info_dict.get('s1_vis_shape')
    s1_eye_shape = shape_info_dict.get('s1_eye_shape')
    s1_mus_shape = shape_info_dict.get('s1_mus_shape')
    
    subjects_of_interest = subjects_dict.get('subjects_of_interest')
    strong_gamma_response_subjects_data_dir_path_dict = subjects_dict.get('strong_gamma_response_subjects_data_dir_path_dict')
    
    vis_stim_aio_path = info_dict.get('vis_stim_aio_path')
    vis_stim_aio_average_td_path = info_dict.get('vis_stim_aio_average_td_path')
    vis_stim_aio_average_td_fh_path = info_dict.get('vis_stim_aio_average_td_fh_path')
    vis_stim_aio_average_td_sh_path = info_dict.get('vis_stim_aio_average_td_sh_path')
    vis_stim_strong_gamma_path = info_dict.get('vis_stim_strong_gamma_path')
    
    eye_stim_strong_gamma_path = info_dict.get('eye_stim_strong_gamma_path')
    eye_stim_aio_path = info_dict.get('eye_stim_aio_path')
    
    mus_stim_aio_path = info_dict.get('mus_stim_aio_path')
    mus_stim_strong_gamma_path = info_dict.get('mus_stim_strong_gamma_path')
    
    
    if not vis_stim_aio_path.is_file():
        print(f'First time creating {vis_stim_aio_path.parts[-1]}')
        # loading all the visual stimuli in a single numpy.ndarray obj and baseline correcting it
        visual_stimuli_ersps_in_one = numpy.ndarray((len(subjects_path_dict), # 31 subjects
                                                    s1_vis_shape[0], # 6 stimuli
                                                    s1_vis_shape[1], # 135 trials needed
                                                    s1_vis_shape[2], # 60 freqs
                                                    s1_vis_shape[3])) # 350 timepoints
    
        for i in numpy.arange(1, visual_stimuli_ersps_in_one.shape[0] + 1):
            subject_mat_path_vis = subjects_path_dict['s' + str(i)]['vis_ersp']
            subject_ersp_ndarray = scipy.io.loadmat(subject_mat_path_vis)['mstersp']
            subject_ersp_ndarray_mean_over_specific_timepoints = numpy.mean(
                subject_ersp_ndarray[..., 0 : 72], # [:,:,:,0:72]
                axis=3, keepdims=True
            )

            baseline_corrected_ersp_ndarray = subject_ersp_ndarray - \
                subject_ersp_ndarray_mean_over_specific_timepoints
            visual_stimuli_ersps_in_one[i - 1, ...] = baseline_corrected_ersp_ndarray[:, : 135,...]
            
        numpy.save(vis_stim_aio_path, 
                   visual_stimuli_ersps_in_one)
        del (
            visual_stimuli_ersps_in_one, 
            baseline_corrected_ersp_ndarray, 
            subject_ersp_ndarray_mean_over_specific_timepoints, 
            subject_ersp_ndarray, 
            subject_mat_path_vis
            )
    

    if not vis_stim_aio_average_td_path.is_file():
        print(f'First time creating {vis_stim_aio_average_td_path.parts[-1]}')
        # all the visual stimuli but averaged on the time domain
        visual_stimuli_ersps_in_one_average_td = numpy.ndarray((len(subjects_path_dict), # 31 subjects
                                                            s1_vis_shape[0], # 6 stimuli
                                                            s1_vis_shape[1], # 135 trials needed
                                                            s1_vis_shape[2], # 60 freqs
                                                            s1_vis_shape[3] // s1_vis_shape[3])) # 1 timepoint
    
        for i in numpy.arange(1, visual_stimuli_ersps_in_one_average_td.shape[0] + 1):
            subject_mat_path_vis = subjects_path_dict['s' + str(i)]['vis_ersp']
            subject_ersp_ndarray = scipy.io.loadmat(subject_mat_path_vis)['mstersp']
            subject_ersp_ndarray_mean_over_specific_timepoints = numpy.mean(
                subject_ersp_ndarray[..., 0 : 72], # [:,:,:,0:72]
                axis=3, keepdims=True
            )

            baseline_corrected_ersp_ndarray = subject_ersp_ndarray - \
                subject_ersp_ndarray_mean_over_specific_timepoints
            baseline_corrected_ersp_ndarray = numpy.mean(baseline_corrected_ersp_ndarray, axis = -1, keepdims = True)
            visual_stimuli_ersps_in_one_average_td[i - 1, ...] = baseline_corrected_ersp_ndarray[:, : 135,...]
            
        numpy.save(vis_stim_aio_average_td_path, 
                   visual_stimuli_ersps_in_one_average_td)
        del (
            visual_stimuli_ersps_in_one_average_td, 
            baseline_corrected_ersp_ndarray, 
            subject_ersp_ndarray_mean_over_specific_timepoints, 
            subject_ersp_ndarray, 
            subject_mat_path_vis
        )
    
    
    

    if not vis_stim_aio_average_td_fh_path.is_file():
        print(f'First time creating {vis_stim_aio_average_td_fh_path.parts[-1]}')
        # all the visual stimuli but averaged on the time domain first half
        visual_stimuli_ersps_in_one_average_td_fh = numpy.ndarray((len(subjects_path_dict), # 31 subjects
                                                                s1_vis_shape[0], # 6 stimuli
                                                                s1_vis_shape[1], # 135 trials needed
                                                                s1_vis_shape[2], # 60 freqs
                                                                s1_vis_shape[3] // s1_vis_shape[3])) # 1 timepoint
    
        for i in numpy.arange(1, visual_stimuli_ersps_in_one_average_td_fh.shape[0] + 1):
            subject_mat_path_vis = subjects_path_dict['s' + str(i)]['vis_ersp']
            subject_ersp_ndarray = scipy.io.loadmat(subject_mat_path_vis)['mstersp']
            subject_ersp_ndarray_mean_over_specific_timepoints = numpy.mean(
                subject_ersp_ndarray[..., 0 : 72], # [:,:,:,0:72]
                axis=3, keepdims=True
            )

            baseline_corrected_ersp_ndarray = subject_ersp_ndarray - \
                subject_ersp_ndarray_mean_over_specific_timepoints
            baseline_corrected_ersp_ndarray = numpy.mean(baseline_corrected_ersp_ndarray[..., : s1_vis_shape[3]//2], axis = -1, keepdims = True)
            visual_stimuli_ersps_in_one_average_td_fh[i - 1, ...] = baseline_corrected_ersp_ndarray[:, : 135,...]
            
        numpy.save(vis_stim_aio_average_td_fh_path, 
                visual_stimuli_ersps_in_one_average_td_fh)
        del (
            visual_stimuli_ersps_in_one_average_td_fh, 
            baseline_corrected_ersp_ndarray, 
            subject_ersp_ndarray_mean_over_specific_timepoints, 
            subject_ersp_ndarray, 
            subject_mat_path_vis
        )

    if not mus_stim_aio_path.is_file():
        print(f'First time creating {mus_stim_aio_path.parts[-1]}')
        # loading all the muscle stimuli in one numpy.ndarray obj and baseline correcting it
        muscle_stimuli_ersps_in_one = numpy.ndarray((len(subjects_path_dict), # 31 subjects
                                                    s1_mus_shape[0], # 6 stimuli
                                                    s1_mus_shape[1], # 135 trials needed
                                                    s1_mus_shape[2], # 60 freqs
                                                    s1_mus_shape[3])) # 350 timepoints
    
        # load all subjects into allersp (31 subjects, 6 stim types, 135 trials per stim type, 60 freqs, 350 timepoints)
        for i in numpy.arange(1, muscle_stimuli_ersps_in_one.shape[0] + 1):
            # vismat = scipy.io.loadmat('C:/shared/allres/s'+str(i)+'/vis_ersp.mat')
            # ersp = vismat['mstersp']
            subject_mat_path_mus = subjects_path_dict['s' + str(i)]['muscle_ersp']
            subject_ersp_ndarray = scipy.io.loadmat(subject_mat_path_mus)['mstersp']
            subject_ersp_ndarray_mean_over_specific_timepoints = numpy.mean(
                subject_ersp_ndarray[..., 0 : 72], # [:,:,:,0:72]
                axis=3, keepdims=True
            )

            baseline_corrected_ersp_ndarray = subject_ersp_ndarray - \
                subject_ersp_ndarray_mean_over_specific_timepoints
            muscle_stimuli_ersps_in_one[i - 1, ...] = baseline_corrected_ersp_ndarray[:, : 135,...]
            
        numpy.save(mus_stim_aio_path, 
                muscle_stimuli_ersps_in_one)
        del (
            muscle_stimuli_ersps_in_one, 
            baseline_corrected_ersp_ndarray, 
            subject_ersp_ndarray_mean_over_specific_timepoints, 
            subject_ersp_ndarray, 
            subject_mat_path_mus
        )

    if not vis_stim_aio_average_td_sh_path.is_file():
        print(f'First time creating {vis_stim_aio_average_td_sh_path.parts[-1]}')
        # all the visual stimuli but averaged on the time domain second half
        visual_stimuli_ersps_in_one_average_td_sh = numpy.ndarray((len(subjects_path_dict), # 31 subjects
                                                                s1_vis_shape[0], # 6 stimuli
                                                                s1_vis_shape[1], # 135 trials needed
                                                                s1_vis_shape[2], # 60 freqs
                                                                s1_vis_shape[3] // s1_vis_shape[3])) # 1 timepoint
    
        for i in numpy.arange(1, visual_stimuli_ersps_in_one_average_td_sh.shape[0] + 1):
            subject_mat_path_vis = subjects_path_dict['s' + str(i)]['vis_ersp']
            subject_ersp_ndarray = scipy.io.loadmat(subject_mat_path_vis)['mstersp']
            subject_ersp_ndarray_mean_over_specific_timepoints = numpy.mean(
                subject_ersp_ndarray[..., 0 : 72], # [:,:,:,0:72]
                axis=3, keepdims=True
            )

            baseline_corrected_ersp_ndarray = subject_ersp_ndarray - \
                subject_ersp_ndarray_mean_over_specific_timepoints
            baseline_corrected_ersp_ndarray = numpy.mean(baseline_corrected_ersp_ndarray[..., s1_vis_shape[3]//2 : ], axis = -1, keepdims = True)
            visual_stimuli_ersps_in_one_average_td_sh[i - 1, ...] = baseline_corrected_ersp_ndarray[:, : 135,...]
        
        numpy.save(vis_stim_aio_average_td_sh_path, 
                   visual_stimuli_ersps_in_one_average_td_sh)
        del (
            visual_stimuli_ersps_in_one_average_td_sh, 
            baseline_corrected_ersp_ndarray, 
            subject_ersp_ndarray_mean_over_specific_timepoints, 
            subject_ersp_ndarray, 
            subject_mat_path_vis
        )

    if not eye_stim_aio_path.is_file():
        print(f'First time creating {eye_stim_aio_path.parts[-1]}')
        # loading all the eye stimuli in one numpy.ndarray obj and baseline correcting it
        eyes_stimuli_ersps_in_one = numpy.ndarray((len(subjects_path_dict), # 31 subjects
                                                s1_eye_shape[0], # 6 stimuli
                                                s1_eye_shape[1], # 135 trials needed
                                                s1_eye_shape[2], # 60 freqs
                                                s1_eye_shape[3])) # 350 timepoints
    
        # load all subjects into allersp (31 subjects, 6 stim types, 135 trials per stim type, 60 freqs, 350 timepoints)
        for i in numpy.arange(1, eyes_stimuli_ersps_in_one.shape[0] + 1):
            subject_mat_path_eye = subjects_path_dict['s' + str(i)]['eyes_ersp']
            subject_ersp_ndarray = scipy.io.loadmat(subject_mat_path_eye)['mstersp']
            subject_ersp_ndarray_mean_over_specific_timepoints = numpy.mean(
                subject_ersp_ndarray[..., 0 : 72], # [:,:,:,0:72]
                axis=3, keepdims=True
            )

            baseline_corrected_ersp_ndarray = subject_ersp_ndarray - \
                subject_ersp_ndarray_mean_over_specific_timepoints
            eyes_stimuli_ersps_in_one[i - 1, ...] = baseline_corrected_ersp_ndarray[:, : 135,...]
        
        numpy.save(eye_stim_aio_path, 
                   eyes_stimuli_ersps_in_one)
        del (
            eyes_stimuli_ersps_in_one, 
            baseline_corrected_ersp_ndarray, 
            subject_ersp_ndarray_mean_over_specific_timepoints, 
            subject_ersp_ndarray, 
            subject_mat_path_eye
        )

    


    if not vis_stim_strong_gamma_path.is_file():
        print(f'First time creating {vis_stim_strong_gamma_path.parts[-1]}')
        # loading only the subjects which have strong gamma response to the numpy.ndarray obj and baseline correcting it
        visual_stimuli_ersps_aio_strong_gamma_subjects = numpy.ndarray((len(strong_gamma_response_subjects_data_dir_path_dict), # subjects with strong gamma response
                                                                        s1_vis_shape[0] - 4, # only 5% and 100% contrast
                                                                        s1_vis_shape[1], # 135 trials needed
                                                                        s1_vis_shape[2], # 60 freqs
                                                                        s1_vis_shape[3],)) # 350 timepoints
        
        for i in numpy.arange(1, visual_stimuli_ersps_aio_strong_gamma_subjects.shape[0] + 1):
            subject_mat_path_vis = strong_gamma_response_subjects_data_dir_path_dict['s' + str(subjects_of_interest[i - 1])]['vis_ersp']
            subject_ersp_ndarray = scipy.io.loadmat(subject_mat_path_vis)['mstersp'] # its shape is (6, 135, 60, 350)
            subject_ersp_ndarray_mean_over_specific_timepoints = numpy.mean(
                subject_ersp_ndarray[:2, :, :, 0 : 72], # [:,:,:,0:72]
                axis = 3, keepdims = True,
            ) # shape would be (2, 135, 60, 1)

            baseline_corrected_ersp_ndarray = subject_ersp_ndarray[:2, ...] - \
                subject_ersp_ndarray_mean_over_specific_timepoints
            visual_stimuli_ersps_aio_strong_gamma_subjects[i - 1, ...] = baseline_corrected_ersp_ndarray[:, : 135,...]
        numpy.save(vis_stim_strong_gamma_path, 
                   visual_stimuli_ersps_aio_strong_gamma_subjects)
        del (
            visual_stimuli_ersps_aio_strong_gamma_subjects, 
            subject_mat_path_vis, subject_ersp_ndarray, 
            subject_ersp_ndarray_mean_over_specific_timepoints, 
            baseline_corrected_ersp_ndarray
        )

    

    if not mus_stim_strong_gamma_path.is_file():
        print(f'First time creating {mus_stim_strong_gamma_path.parts[-1]}')
        # loading only the muscle stimuli of the subjects with strong gamma response in one numpy.ndarray obj
        muscle_stimuli_ersps_aio_strong_gamma_subjects = numpy.ndarray((len(strong_gamma_response_subjects_data_dir_path_dict), # subjects with strong gamma response
                                                                        s1_mus_shape[0] - 4, # only 5% and 100% contrast
                                                                        s1_mus_shape[1], # 135 trials needed
                                                                        s1_mus_shape[2], # 60 freqs
                                                                        s1_mus_shape[3],)) # 350 timepoints
        
        for i in numpy.arange(1, muscle_stimuli_ersps_aio_strong_gamma_subjects.shape[0] + 1):
            subject_mat_path_mus = strong_gamma_response_subjects_data_dir_path_dict['s' + str(subjects_of_interest[i - 1])]['muscle_ersp']
            subject_ersp_ndarray = scipy.io.loadmat(subject_mat_path_mus)['mstersp'] # its shape is (6, 135, 60, 350)
            subject_ersp_ndarray_mean_over_specific_timepoints = numpy.mean(
                subject_ersp_ndarray[:2, :, :, 0 : 72], # [:,:,:,0:72]
                axis=3, keepdims=True
            ) # shape would be (2, 135, 60, 1)

            baseline_corrected_ersp_ndarray = subject_ersp_ndarray[:2, ...] - \
                subject_ersp_ndarray_mean_over_specific_timepoints
            muscle_stimuli_ersps_aio_strong_gamma_subjects[i - 1, ...] = baseline_corrected_ersp_ndarray[:, : 135,...]
        numpy.save(mus_stim_strong_gamma_path, 
                   muscle_stimuli_ersps_aio_strong_gamma_subjects)
        del (
            muscle_stimuli_ersps_aio_strong_gamma_subjects, 
            subject_mat_path_mus, subject_ersp_ndarray, 
            subject_ersp_ndarray_mean_over_specific_timepoints, 
            baseline_corrected_ersp_ndarray
        ) 


    if not eye_stim_strong_gamma_path.is_file():
        print(f'First time creating {eye_stim_strong_gamma_path.parts[-1]}')
        # loading only the eyes stimuli of the subjects with strong gamma response in one numpy.ndarray obj
        eyes_stimuli_ersps_aio_strong_gamma_subjects = numpy.ndarray((len(strong_gamma_response_subjects_data_dir_path_dict), # subjects with strong gamma response
                                                                    s1_eye_shape[0] - 4, # only 5% and 100% contrast
                                                                    s1_eye_shape[1], # 135 trials needed
                                                                    s1_eye_shape[2], # 60 freqs
                                                                    s1_eye_shape[3])) # 350 timepoints
        
        for i in numpy.arange(1, eyes_stimuli_ersps_aio_strong_gamma_subjects.shape[0] + 1):
            subject_mat_path_eye = strong_gamma_response_subjects_data_dir_path_dict['s' + str(subjects_of_interest[i - 1])]['eyes_ersp']
            subject_ersp_ndarray = scipy.io.loadmat(subject_mat_path_eye)['mstersp'] # its shape is (6, 135, 60, 350)
            subject_ersp_ndarray_mean_over_specific_timepoints = numpy.mean(
                subject_ersp_ndarray[:2, :, :, 0 : 72], # [:,:,:,0:72]
                axis=3, keepdims=True
            ) # shape would be (2, 135, 60, 1)

            baseline_corrected_ersp_ndarray = subject_ersp_ndarray[:2, ...] - \
                subject_ersp_ndarray_mean_over_specific_timepoints
            eyes_stimuli_ersps_aio_strong_gamma_subjects[i - 1, ...] = baseline_corrected_ersp_ndarray[:, : 135,...]
        
        numpy.save(eye_stim_strong_gamma_path, 
                   eyes_stimuli_ersps_aio_strong_gamma_subjects)
        del (
            eyes_stimuli_ersps_aio_strong_gamma_subjects, 
            subject_mat_path_eye, 
            subject_ersp_ndarray, 
            subject_ersp_ndarray_mean_over_specific_timepoints, 
            baseline_corrected_ersp_ndarray
        )
    
    









































