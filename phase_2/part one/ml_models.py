import numpy
import sklearn
import sklearn.ensemble

def initialize_mappings(paths_info_dict):
    mapping_dict = dict(
        psatfs=dict(
            description='per subject, all time domain, all freqs, all stims',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        pszotatfs=dict(
            description='per subject, stims [0, 1, 2], all freqs, all time points',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        pstffatfs=dict(
            description='per subject, stims [3, 4, 5], all freqs, all time points',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        psatpfzot=dict(
            description='per subject, per frequency, [0, 1, 2] stims, all time points',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        psatpftff=dict(
            description='per subject, per frequency, [3, 4, 5] stims, all time points',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        pstdpfzot=dict(
            description='per subject, per frequency, stims [0, 1, 2], time divisions',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        pstdpftff=dict(
            description='per subject, time division, per frequency, stims [3, 4, 5]',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        pfasatst=dict(
            description='per frequency, all subjects, all time points, all stims',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        avg_td=dict(
            description='per frequency and average of all time points predictions accuracy',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        avg_td_fh=dict(
            description='per frequency and average of first half of time points',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_fh_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        avg_td_sh=dict(
            description='per frequency and average of second half of time points',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_sh_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        vis_zot=dict(
            description='All subjects, all time points, and vis labels 100% 5% 33% contrast, per each frequency basis',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        vis_tff=dict(
            description='All subjects, all time points, and vis labels 10% 60% plaid random, per each frequency basis',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        vis_zot_td=dict(
            description='All subjects, time points divided to 3 parts, and vis labels vis labels 100% 5% 33% contrast, per each frequency basis',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        vis_tff_td=dict(
            description='All subjects, time points divided to 3 parts, and vis labels 10% 60% plaid random, per each frequency basis',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        afatasas=dict(
            description='all the freqs all the timepoints, all subjects, all stimuli',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        afataszos=dict(
            description='all time points, all freqs, all subjects, 0 & 1 visual stimuli',
            data_path=paths_info_dict.get('vis_stim_aio_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        afavgtaszos=dict(
            description='### average of time points, 0 & 1 visual stimuli, all subjects, all freqs',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        afavgtasas=dict(
            description='### average of time points, all stims, all freqs, all subjects',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        fhfavgtaszos=dict(
            description='stimuli 0 & 1, first half of frequencies, all subjects, average of time points',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        shfataszos=dict(
            description='vis stimuli 0 & 1, second half of frequencies, all subjects, all time points average',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        fhffhavgtaszos=dict(
            description='visual stimuli 0 & 1, first half of frequencies, first half of time domain average, all subjects',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_fh_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        shffhavgtaszos=dict(
            description='first half of time points average, vis stimuli 0 & 1, second half of freqs, all subjects',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_fh_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        fhfshavgtaszos=dict(
            description='second half of time domain average, vis stims 0 & 1, first half of freqs, all subjects',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_sh_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
        shfshavgtaszos=dict(
            description='second half of time points average, vis stimuli 0 & 1, second half of freqs, all subjects',
            data_path=paths_info_dict.get('vis_stim_aio_average_td_sh_path'),
            labels_path=paths_info_dict.get('vis_stim_aio_labels_path')
        ),
    )
    for i in mapping_dict:
        data_shape = numpy.load(i['data_path'])
        

def create_dataset(data, labels, test_size=.3, random_state=13):
    (train_data, 
    validation_data, 
    train_labels, 
    validation_labels) = sklearn.model_selection.train_test_split(data, 
                                                                  labels, 
                                                                  test_size=0.3, 
                                                                  random_state=13)
    return (train_data, 
            validation_data, 
            train_labels, 
            validation_labels)


def get_data_labels(model_name, mapping_dict, only_paths=False):
    # vis_stim_aio_path = paths_info_dict.get('vis_stim_aio_path')
    # vis_stim_aio_labels_path = paths_info_dict.get('vis_stim_aio_labels_path')
    # data = numpy.load(vis_stim_aio_path)
    # labels = numpy.load(vis_stim_aio_labels_path)
    tmp_dict = mapping_dict.get(model_name)
    if not only_paths:
        data = numpy.load(tmp_dict.get('data_path'))
        labels = numpy.load(tmp_dict.get('labels_path'))
        data_shape = data.shape
        labels = labels.reshape((data_shape[0], 
                                data_shape[1], 
                                data_shape[2]))
        return (data, 
                labels,
                data_shape)
    else:
        data_path = tmp_dict.get('data_path')
        labels_path = tmp_dict.get('labels_path')
        data = numpy.load(tmp_dict.get('data_path'))
        data_shape = data.shape
        del data
        return (data_path, 
                labels_path,
                data_shape)
    
    
def train_model(train_data, train_labels, validation_data, validation_labels,
                classifier=sklearn.ensemble.RandomForestClassifier, **kwargs):
    n_estimators = kwargs.get('n_estimators', 100)
    random_state = kwargs.get('random_state', 42)
    n_jobs = kwargs.get('n_jobs', -1)
    clf = sklearn.ensemble.RandomForestClassifier(n_estimators=n_estimators, 
                                                  random_state=random_state, 
                                                  n_jobs=n_jobs)
    clf.fit(train_data, train_labels)
    predictions = clf.predict(validation_data)
    accuracy = sklearn.metrics.accuracy_score(validation_labels, 
                                              predictions)
    
    return (
        clf,
        predictions,
        accuracy
    )

def process_model(model_name, data, labels, data_shape, paths_info_dict):
    mapping_dict = initialize_mappings(paths_info_dict)
    if model_name == 'psatfs':
        predictions_res_psatfs = {}
        for x in range(data_shape[0]):
            data, labels, data_shape = get_data_labels(model_name, mapping_dict)
            labels_modified = labels[x, ...].flatten().tolist()
            data = data[x, ...]
            data_reshaped = data.reshape(data_shape[1] * data_shape[2], 
                                        data_shape[-1] * data_shape[-2])
            del data
            
            (train_data, 
            validation_data, 
            train_labels, 
            validation_labels) = create_dataset(data_reshaped,
                                                labels_modified,
                                                test_size=0.3,
                                                random_state=13)
            (clf,
             predictions,
             accuracy) = train_model(train_data, train_labels, validation_data,
                                     validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                     n_estimators=100, random_state=42, n_jobs=-1)
            predictions_res_psatfs[x + 1] = accuracy
        return predictions_res_psatfs
    
    elif model_name == 'pszotatfs':
        predictions_res_pszotatfs = {}
        for x in range(data_shape[0]):
            labels_modified = labels[x, :3, ...]
            labels_modified = labels_modified.flatten()
            data, labels, data_shape = get_data_labels(model_name, mapping_dict)
            data = data[x, :3, ...]
            data_reshaped = data.reshape((data.shape[0] * data_shape[2], 
                                          data_shape[-1] * data_shape[-2]))
            del data
            (train_data, 
            validation_data, 
            train_labels, 
            validation_labels) = create_dataset(data_reshaped,
                                                labels_modified,
                                                test_size=0.3,
                                                random_state=13)
            (clf,
             predictions,
             accuracy) = train_model(train_data, train_labels, validation_data,
                                     validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                     n_estimators=100, random_state=42, n_jobs=-1)
            predictions_res_pszotatfs[x + 1] = accuracy
        return predictions_res_pszotatfs
    
    elif model_name == 'pstffatfs':
        predictions_res_pstffatfs = {}
        for x in range(data_shape[0]):
            data, labels, data_shape = get_data_labels(model_name, mapping_dict)
            labels_modified = labels[x, 3:, ...]
            labels_modified = labels_modified.flatten()
            data = data[x, 3:, ...]
            data_reshaped = data.reshape((data.shape[0] * data_shape[2], 
                                        data_shape[-1] * data_shape[-2]))
            del data
            (train_data, 
            validation_data, 
            train_labels, 
            validation_labels) = create_dataset(data_reshaped,
                                                labels_modified,
                                                test_size=0.3,
                                                random_state=13)
            (clf,
             predictions,
             accuracy) = train_model(train_data, train_labels, validation_data,
                                     validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                     n_estimators=100, random_state=42, n_jobs=-1)
            predictions_res_pstffatfs[x + 1] = accuracy
        return predictions_res_pstffatfs
    
    elif model_name == 'psatpfzot':
        predictions_res_psatpfzot = {}

        for i in range(data_shape[0]):
            predictions_res_psatpfzot[i+1] = {}
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        labels = numpy.load(labels_path)
        labels = labels.reshape((data_shape[0], 
                                data_shape[1], 
                                data_shape[2]))
        for x in range(data_shape[0]):
            labels_modified = labels[x, :3, ...]
            for z in range(data_shape[-2]):
                labels_modified = labels_modified.flatten()
                data = numpy.load(data_path)
                data = data[x, :3, :, z, :]
            
                data_reshaped = data.reshape((data.shape[0] * data_shape[2], 
                                            data_shape[-1]))
                del data
                (train_data, 
                 validation_data, 
                 train_labels, 
                 validation_labels) = create_dataset(data_reshaped,
                                                     labels_modified,
                                                     test_size=0.3,
                                                     random_state=13)
                (clf,
                 predictions,
                 accuracy) = train_model(train_data, train_labels, validation_data,
                                         validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                         n_estimators=100, random_state=42, n_jobs=-1)
                predictions_res_psatpfzot[x + 1][z + 1] = accuracy
        return predictions_res_psatpfzot
    
    elif model_name == 'psatpftff':
        predictions_res_psatpftff = {}
        for i in range(data_shape[0]):
            predictions_res_psatpftff[i + 1] = {}
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        labels = numpy.load(labels_path)
        labels = labels.reshape((data_shape[0], 
                                data_shape[1], 
                                data_shape[2]))
        for x in range(data_shape[0]):
            labels_modified = labels[x, 3:, ...]
            for z in range(data_shape[-2]):
                labels_modified = labels_modified.flatten()
                data = numpy.load(data_path)
                data = data[x, 3:, :, z, :]
            
                data_reshaped = data.reshape((data.shape[0] * data_shape[2], 
                                            data_shape[-1]))
                del data
                (train_data, 
                 validation_data, 
                 train_labels, 
                 validation_labels) = create_dataset(data_reshaped,
                                                     labels_modified,
                                                     test_size=0.3,
                                                     random_state=13)
                (clf,
                 predictions,
                 accuracy) = train_model(train_data, train_labels, validation_data,
                                         validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                         n_estimators=100, random_state=42, n_jobs=-1)
                predictions_res_psatpftff[x + 1][z + 1] = accuracy
        return predictions_res_psatpftff
    
    elif model_name == 'pstdpfzot':
        temp_dict = {
            '0-0.33t' : {},
            '0.33-0.66t' : {},
            '0.66-1.t' : {},
        }
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        labels = numpy.load(labels_path)
        labels = labels.reshape((data_shape[0], 
                                data_shape[1], 
                                data_shape[2]))
        predictions_res_pstdpfzot = {}
        ind_prvzt = {i[0] : i[1] for i in list(enumerate(temp_dict))}
        for i in range(data_shape[0]):
            predictions_res_pstdpfzot[i + 1] = temp_dict
            for w in ind_prvzt:
                for j in range(data_shape[-2]):
                    predictions_res_pstdpfzot[i + 1][ind_prvzt[w]][j + 1] = 0

        timepoint_div_vals = []
        for i in range(1):
            t_val = data_shape[-1] // 3
            for _ in range(len(temp_dict)):
                timepoint_div_vals.append(t_val)
            timepoint_div_vals[-1] += data_shape[-1] % 3

        for x in range(data_shape[0]):
            labels_modified = labels[x, :3, ...]
            labels_modified = labels_modified.flatten()
            for w in range(len(timepoint_div_vals)):
                for z in range(data_shape[-2]):
                    data = numpy.load(data_path)
                    if w == 0:
                        data = data[x, :3, :, z, 0 : sum(timepoint_div_vals[:1])]
                    else:
                        data = data[x, :3, :, z, sum(timepoint_div_vals[:w]) : sum(timepoint_div_vals[:w]) + timepoint_div_vals[w]]

                    data_reshaped = data.reshape((data.shape[0] * data_shape[2], 
                                                data.shape[-1]))
                    del data
                    (train_data, 
                     validation_data, 
                     train_labels, 
                     validation_labels) = create_dataset(data_reshaped,
                                                         labels_modified,
                                                         test_size=0.3,
                                                         random_state=13)
                    (clf,
                     predictions,
                     accuracy) = train_model(train_data, train_labels, validation_data,
                                             validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                             n_estimators=100, random_state=42, n_jobs=-1)
                    predictions_res_pstdpfzot[x + 1][ind_prvzt[w]][z + 1] = accuracy
        return predictions_res_pstdpfzot
    
    elif model_name == 'pstdpftff':
        temp_dict = {
            '0-0.33t' : {},
            '0.33-0.66t' : {},
            '0.66-1.t' : {},
        }
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        labels = numpy.load(labels_path)
        labels = labels.reshape((data_shape[0], 
                                data_shape[1], 
                                data_shape[2]))
        predictions_res_pstdpftff = {}
        ind_prvzt = {i[0] : i[1] for i in list(enumerate(temp_dict))}
        for i in range(data_shape[0]):
            predictions_res_pstdpftff[i + 1] = temp_dict
            for w in ind_prvzt:
                for j in range(data_shape[-2]):
                    predictions_res_pstdpftff[i + 1][ind_prvzt[w]][j + 1] = 0

        timepoint_div_vals = []
        for i in range(1):
            t_val = data_shape[-1] // 3
            for _ in range(len(temp_dict)):
                timepoint_div_vals.append(t_val)
            timepoint_div_vals[-1] += data_shape[-1] % 3

        for x in range(data_shape[0]):
            labels_modified = labels[x, 3:, ...]
            labels_modified = labels_modified.flatten()
            for w in range(len(timepoint_div_vals)):
                for z in range(data_shape[-2]):
                    # data = numpy.load(vis_stim_aio_path)
                    data = numpy.load(data_path)
                    if w == 0:
                        data = data[x, 3:, :, z, 0 : sum(timepoint_div_vals[:1])]
                    else:
                        data = data[x, 3:, :, z, sum(timepoint_div_vals[:w]) : sum(timepoint_div_vals[:w]) + timepoint_div_vals[w]]

                    data_reshaped = data.reshape((data.shape[0] * data_shape[2], data.shape[-1]))
                    del data
                    (train_data, 
                     validation_data, 
                     train_labels, 
                     validation_labels) = create_dataset(data_reshaped,
                                                         labels_modified,
                                                         test_size=0.3,
                                                         random_state=13)
                    (clf,
                     predictions,
                     accuracy) = train_model(train_data, train_labels, validation_data,
                                             validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                             n_estimators=100, random_state=42, n_jobs=-1)
                    predictions_res_pstdpftff[x + 1][ind_prvzt[w]][z + 1] = accuracy
        return predictions_res_pstdpftff
    
    ## per frequency analysis
    elif model_name == 'pfasatst':
        pfasatst = {}
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        for i in range(data_shape[-2]):
            data, labels, data_shape = get_data_labels(model_name, mapping_dict)
            data = data[:, :, :, i, :]
            data_reshaped = data.reshape(data.shape[0] * data.shape[1] * data.shape[2], 
                                        data.shape[-1])
            del data
            (train_data, 
            validation_data, 
            train_labels, 
            validation_labels) = create_dataset(data_reshaped,
                                                labels_modified,
                                                test_size=0.3,
                                                random_state=13)
            (clf,
             predictions,
             accuracy) = train_model(train_data, train_labels, validation_data,
                                     validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                     n_estimators=100, random_state=42, n_jobs=-1)
            pfasatst[i + 1] = accuracy
        return pfasatst
    
    elif model_name == 'avg_td':
        predictions_res_avg_td = {}
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        for i in range(data_shape[-2]):
            data, labels, data_shape = get_data_labels(model_name, mapping_dict)
            data = data[:, :, :, i, :]
            data_reshaped = data.reshape(data.shape[0] * data.shape[1] * data.shape[2], 
                                         data.shape[-1])
            del data
            (train_data, 
            validation_data, 
            train_labels, 
            validation_labels) = create_dataset(data_reshaped,
                                                labels,
                                                test_size=0.3,
                                                random_state=13)
            (clf,
             predictions,
             accuracy) = train_model(train_data, train_labels, validation_data,
                                     validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                     n_estimators=100, random_state=42, n_jobs=-1)
            predictions_res_avg_td[i + 1] = accuracy
        return predictions_res_avg_td
    
    elif model_name == 'avg_td_fh':
        predictions_res_avg_td_fh = {}
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        for i in range(data_shape[-2]):
            data, labels, data_shape = get_data_labels(model_name, mapping_dict)
            data = data[:, :, :, i, :]
            data_reshaped = data.reshape(data.shape[0] * data.shape[1] * data.shape[2], 
                                        data.shape[-1])
            del data
            (train_data, 
             validation_data, 
             train_labels, 
             validation_labels) = create_dataset(data_reshaped,
                                                 labels,
                                                 test_size=0.3,
                                                 random_state=13)
            (clf,
             predictions,
             accuracy) = train_model(train_data, train_labels, validation_data,
                                     validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                     n_estimators=100, random_state=42, n_jobs=-1)
            predictions_res_avg_td_fh[i + 1] = accuracy
    
    elif model_name == 'avg_td_sh':
        predictions_res_avg_td_sh = {}
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        for i in range(data_shape[-2]):
            data, labels, data_shape = get_data_labels(model_name, mapping_dict)
            data = data[:, :, :, i, :]
            data_reshaped = data.reshape(data.shape[0] * data.shape[1] * data.shape[2], data.shape[-1])
            del data
            (train_data, 
            validation_data, 
            train_labels, 
            validation_labels) = create_dataset(data_reshaped,
                                                labels,
                                                test_size=0.3,
                                                random_state=13)
            (clf,
             predictions,
             accuracy) = train_model(train_data, train_labels, validation_data,
                                     validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                     n_estimators=100, random_state=42, n_jobs=-1)
            predictions_res_avg_td_sh[i + 1] = accuracy
            
        return predictions_res_avg_td_sh
    
    elif model_name == 'vis_zot':
        predictions_res_vis_zot = {}
        labels_modified = []
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        labels = numpy.load(labels_path)
        labels = labels.reshape((data_shape[0], 
                                data_shape[1], 
                                data_shape[2]))
        for q in range(data_shape[-2]):
            labels_modified = []
            for i in range(labels.shape[0]):
                for j in range(labels.shape[1]):
                    for x in range(labels.shape[2]):
                        if j <= 2:
                            labels_modified.append(labels[i, j, x])
            labels_modified = numpy.array(labels_modified)
            data, labels, data_shape = get_data_labels(model_name, mapping_dict)
            data = data[:, :3, :, q, :]
            data_reshaped = data.reshape(data.shape[0] * data.shape[1] * data.shape[2], 
                                        data.shape[-1])
            del data
            (train_data, 
            validation_data, 
            train_labels, 
            validation_labels) = create_dataset(data_reshaped,
                                                labels_modified,
                                                test_size=0.3,
                                                random_state=13)
            (clf,
             predictions,
             accuracy) = train_model(train_data, train_labels, validation_data,
                                     validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                     n_estimators=100, random_state=42, n_jobs=-1)
            predictions_res_vis_zot[q + 1] = accuracy
        return predictions_res_vis_zot
    
    elif model_name == 'vis_tff':
        predictions_res_vis_tff = {}
        labels_modified = []
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        labels = numpy.load(labels_path)
        labels = labels.reshape((data_shape[0], 
                                data_shape[1], 
                                data_shape[2]))

        for q in range(data_shape[-2]):
            labels_modified = []
            for i in range(labels.shape[0]):
                for j in range(labels.shape[1]):
                    for x in range(labels.shape[2]):
                        if j >= 3:
                            labels_modified.append(labels[i, j, x])
            labels_modified = numpy.array(labels_modified)
            data, labels, data_shape = get_data_labels(model_name, mapping_dict)
            data = data[:, 3:, :, q, :]
            data_reshaped = data.reshape(data.shape[0] * data.shape[1] * data.shape[2], 
                                        data.shape[-1])
            del data
            (train_data, 
            validation_data, 
            train_labels, 
            validation_labels) = create_dataset(data_reshaped,
                                                labels_modified,
                                                test_size=0.3,
                                                random_state=13)
            (clf,
             predictions,
             accuracy) = train_model(train_data, train_labels, validation_data,
                                     validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                     n_estimators=100, random_state=42, n_jobs=-1)
            predictions_res_vis_tff[q + 1] = accuracy
        return predictions_res_vis_tff
    
    elif model_name == 'vis_zot_td':
        predictions_res_vis_zot_td = {
            '0-0.33t' : {},
            '0.33-0.66t' : {},
            '0.66-1.t' : {},
        }

        ind_prvzt = {i[0] : i[1] for i in list(enumerate(predictions_res_vis_zot_td))}
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        labels = numpy.load(labels_path)
        labels = labels.reshape((data_shape[0], data_shape[1], data_shape[2]))
        labels_modified = []
        timepoint_div_vals = []
        for i in range(1):
            t_val = data_shape[-1] // 3
            for _ in range(len(predictions_res_vis_zot_td)):
                timepoint_div_vals.append(t_val)
            timepoint_div_vals[-1] += data_shape[-1] % 3

        for w in range(len(timepoint_div_vals)):
            for q in range(data_shape[-2]):
                labels_modified = []
                for i in range(labels.shape[0]):
                    for j in range(labels.shape[1]):
                        for x in range(labels.shape[2]):
                            if j <= 2:
                                labels_modified.append(labels[i, j, x])
                labels_modified = numpy.array(labels_modified)
                data, labels, data_shape = get_data_labels(model_name, mapping_dict)
                if w == 0:
                    data = data[:, :3, :, q, 0 : sum(timepoint_div_vals[:1])]
                else:
                    data = data[:, :3, :, q, sum(timepoint_div_vals[:w]) : sum(timepoint_div_vals[:w]) + timepoint_div_vals[w]]
                data_reshaped = data.reshape(data.shape[0] * data.shape[1] * data.shape[2], 
                                            data.shape[-1])
                del data
                (train_data, 
                 validation_data, 
                 train_labels, 
                 validation_labels) = create_dataset(data_reshaped,
                                                     labels_modified,
                                                     test_size=0.3,
                                                     random_state=13)
                (clf,
                 predictions,
                 accuracy) = train_model(train_data, train_labels, validation_data,
                                         validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                         n_estimators=100, random_state=42, n_jobs=-1)
                predictions_res_vis_zot_td[ind_prvzt[w]][q + 1] = accuracy
            
    elif model_name == 'vis_tff_td':
        predictions_res_vis_tff_td = {
            '0-0.33t' : {},
            '0.33-0.66t' : {},
            '0.66-1.t' : {},
        }

        ind_prvzt = {i[0] : i[1] for i in list(enumerate(predictions_res_vis_tff_td))}
        data_path, labels_path, data_shape = get_data_labels(model_name, mapping_dict,
                                                             only_paths=True)
        labels = numpy.load(labels_path)
        labels = labels.reshape((data_shape[0], data_shape[1], data_shape[2]))
        labels_modified = []
        timepoint_div_vals = []
        for i in range(1):
            t_val = data_shape[-1] // 3
            for _ in range(len(predictions_res_vis_tff_td)):
                timepoint_div_vals.append(t_val)
            timepoint_div_vals[-1] += data_shape[-1] % 3

        print(timepoint_div_vals)

        for w in range(len(timepoint_div_vals)):
            for q in range(data_shape[-2]):
                labels_modified = []
                for i in range(labels.shape[0]):
                    for j in range(labels.shape[1]):
                        for x in range(labels.shape[2]):
                            if j >= 3:
                                labels_modified.append(labels[i, j, x])
                labels_modified = numpy.array(labels_modified)
                data, labels, data_shape = get_data_labels(model_name, mapping_dict)
                if w == 0:
                    data = data[:, 3:, :, q, 0 : sum(timepoint_div_vals[:1])]
                else:
                    data = data[:, 3:, :, q, sum(timepoint_div_vals[:w]) : sum(timepoint_div_vals[:w]) + timepoint_div_vals[w]]
                data_reshaped = data.reshape(data.shape[0] * data.shape[1] * data.shape[2], data.shape[-1])
                del data
                (train_data, 
                 validation_data, 
                 train_labels, 
                 validation_labels) = create_dataset(data_reshaped,
                                                     labels_modified,
                                                     test_size=0.3,
                                                     random_state=13)
                (clf,
                 predictions,
                 accuracy) = train_model(train_data, train_labels, validation_data,
                                          validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                          n_estimators=100, random_state=42, n_jobs=-1)
                predictions_res_vis_tff_td[ind_prvzt[w]][q + 1] = accuracy
                
        return predictions_res_vis_tff_td
    
    elif model_name == 'afatasas':
        data, labels, data_shape = get_data_labels(model_name, mapping_dict)
        data_reshaped = data.reshape(-1, data.shape[-1] * data.shape[-2])

        (train_data, 
        validation_data, 
        train_labels, 
        validation_labels) = create_dataset(data_reshaped,
                                            labels,
                                            test_size=0.3,
                                            random_state=13)
        (clf,
         predictions,
         accuracy) = train_model(train_data, train_labels, validation_data,
                                 validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                 n_estimators=100, random_state=42, n_jobs=-1)
        return accuracy
    
    elif model_name == 'afatasas':
        data, labels, data_shape = get_data_labels(model_name, mapping_dict)
        labels_modified = []
        for i in range(labels.shape[0]):
            for j in range(labels.shape[1]):
                for x in range(labels.shape[2]):
                    if j <= 1:
                        labels_modified.append(labels[i, j, x])
        labels_modified = numpy.array(labels_modified)
        data = data[:, :2, :, :, :]
        data_reshaped = data.reshape(data_shape[0] * 2 * data.shape[2], 
                                    data_shape[-1] * data_shape[-2])
        del data, labels

        (train_data, 
        validation_data, 
        train_labels, 
        validation_labels) = create_dataset(data_reshaped,
                                            labels_modified,
                                            test_size=0.3,
                                            random_state=13)
        (clf,
         predictions,
         accuracy) = train_model(train_data, train_labels, validation_data,
                                 validation_labels, classifier=sklearn.ensemble.RandomForestClassifier,
                                 n_estimators=100, random_state=42, n_jobs=-1)
        print(accuracy)



