import numpy
import tensorflow



def create_datasets(paths_info_dict, 
                    labels_shape_info,
                    dataset_name):
    
    if dataset_name == 'all_subs':
        # train dataset for all the subjects
        vis_stim_aio_labels_path = paths_info_dict.get('vis_stim_aio_labels_path')
        path_to_vis_ersp_dataset = paths_info_dict.get('path_to_vis_ersp_dataset')
        visual_stimuli_ersps_in_one_shape = labels_shape_info.get('visual_stimuli_ersps_in_one_shape')
        vis_labels = numpy.load(vis_stim_aio_labels_path)
        # vis_labels_one_hot = tensorflow.keras.utils.to_categorical(vis_labels, 
                                                                #    num_classes=6)
        # vis_labels_selected_subs_one_hot = tensorflow.keras.utils.to_categorical(selected_subs_vis_labels, 
                                                                                #  num_classes=2)
        
        train_dataset = tensorflow.keras.utils.image_dataset_from_directory(path_to_vis_ersp_dataset,
                                                                            vis_labels.tolist(),
                                                                            color_mode='grayscale',
                                                                            image_size=(visual_stimuli_ersps_in_one_shape[3],
                                                                                        visual_stimuli_ersps_in_one_shape[4]),
                                                                            validation_split=0.3,
                                                                            subset='training',
                                                                            shuffle=True,
                                                                            seed=101)

        validation_dataset = tensorflow.keras.utils.image_dataset_from_directory(path_to_vis_ersp_dataset,
                                                                                 vis_labels.tolist(),
                                                                                 color_mode='grayscale',
                                                                                 image_size=(visual_stimuli_ersps_in_one_shape[3],
                                                                                             visual_stimuli_ersps_in_one_shape[4]),
                                                                                 validation_split=0.3,
                                                                                 subset='validation',
                                                                                 shuffle=True,
                                                                                 seed=101)

        # val_dataset = tensorflow.keras.utils.image_dataset_from_directory(path_to_mus_ersp_dataset,
                                                                    #   mus_labels,
                                                                    #   color_mode='grayscale',
                                                                    #   image_size=(muscle_stimuli_ersps_in_one_shape[3],
                                                                                # muscle_stimuli_ersps_in_one_shape[4]),
                                                                    #   shuffle=True)


        # test_dataset = tensorflow.keras.utils.image_dataset_from_directory(path_to_eye_ersp_dataset,
                                                                    #   eye_labels,
                                                                    #   color_mode='grayscale',
                                                                    #   image_size=(eyes_stimuli_ersps_in_one_shape[3],
                                                                                # eyes_stimuli_ersps_in_one_shape[4]),
                                                                    #   shuffle=True)
        train_dataset = train_dataset.map(lambda x, y: (x, tensorflow.one_hot(y, 6)))
        validation_dataset = validation_dataset.map(lambda x, y: (x, tensorflow.one_hot(y, 6)))
        # val_dataset = val_dataset.map(lambda x, y: (x, tensorflow.one_hot(y, 6)))
        # test_dataset = test_dataset.map(lambda x, y: (x, tensorflow.one_hot(y, 6)))
        return train_dataset, validation_dataset

    elif dataset_name == 'select_subs':
        # train dataset for selected subjects
        vis_stim_strong_gamma_labels_path = paths_info_dict.get('vis_stim_strong_gamma_labels_path')
        selected_subs_vis_labels = numpy.load(vis_stim_strong_gamma_labels_path)
        path_to_selected_subs_vis_ersp_dataset = paths_info_dict.get('path_to_selected_subs_vis_ersp_dataset')
        visual_stimuli_selected_subjects_ersps_shape = labels_shape_info.get('visual_stimuli_selected_subjects_ersps_shape')
        train_dataset_selected_subs = tensorflow.keras.utils.image_dataset_from_directory(path_to_selected_subs_vis_ersp_dataset,
                                                                                        selected_subs_vis_labels.tolist(),
                                                                                        color_mode='grayscale',
                                                                                        image_size=(visual_stimuli_selected_subjects_ersps_shape[3],
                                                                                                    visual_stimuli_selected_subjects_ersps_shape[4]),
                                                                                        validation_split=0.3,
                                                                                        subset='training',
                                                                                        shuffle=True,
                                                                                        seed=123)

        validation_dataset_selected_subs = tensorflow.keras.utils.image_dataset_from_directory(path_to_selected_subs_vis_ersp_dataset,
                                                                                            selected_subs_vis_labels.tolist(),
                                                                                            color_mode='grayscale',
                                                                                            image_size=(visual_stimuli_selected_subjects_ersps_shape[3],
                                                                                                        visual_stimuli_selected_subjects_ersps_shape[4]),
                                                                                            validation_split=0.3,
                                                                                            subset='validation',
                                                                                            shuffle=True,
                                                                                            seed=123)

        # val_dataset = tensorflow.keras.utils.image_dataset_from_directory(path_to_mus_ersp_dataset,
                                                                    #   mus_labels,
                                                                    #   color_mode='grayscale',
                                                                    #   image_size=(muscle_stimuli_ersps_in_one_shape[3],
                                                                                # muscle_stimuli_ersps_in_one_shape[4]),
                                                                    #   shuffle=True)


        # test_dataset = tensorflow.keras.utils.image_dataset_from_directory(path_to_eye_ersp_dataset,
                                                                    #   eye_labels,
                                                                    #   color_mode='grayscale',
                                                                    #   image_size=(eyes_stimuli_ersps_in_one_shape[3],
                                                                                # eyes_stimuli_ersps_in_one_shape[4]),
                                                                    #   shuffle=True)
        train_dataset_selected_subs = train_dataset_selected_subs.map(lambda x, y: (x, tensorflow.one_hot(y, 2)))
        validation_dataset_selected_subs = validation_dataset_selected_subs.map(lambda x, y: (x, tensorflow.one_hot(y, 2)))

        return train_dataset_selected_subs, validation_dataset_selected_subs

                                                            
                                                            
                                                            
                                                            

