import numpy
import matplotlib.pyplot as plt

def plot_res(name, predictions):
    if name == 'psatfs':
        # psatfs = list(predictions_res_psatfs.copy().values())
        psatfs = list(predictions.copy().values())
        psatfs = numpy.asarray(psatfs)
        psatfs = psatfs[:, numpy.newaxis]

        print(numpy.amin(psatfs),
            numpy.amax(psatfs))

        extent = [0, 1, 0, 31]

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(psatfs, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower', extent=extent)


        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks([])

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/psatfs.png')
    elif name == 'pszotatfs':
        # tb = list(predictions_res_pszotatfs.copy().items())
        tb = list(predictions.copy().items())
        tc = numpy.asarray(tb)
        # display the average for each  stimuli across all subjects
        # plt.subplot()
        # plt.imshow(tc, aspect="auto", cmap='jet', vmin=0., vmax=1.,
        #         interpolation='none', origin='lower')
        
        # pszotatfs = list(predictions_res_pszotatfs.copy().values())
        pszotatfs = list(predictions.copy().values())
        pszotatfs = numpy.asarray(pszotatfs)
        pszotatfs = pszotatfs[:, numpy.newaxis]

        print(numpy.amin(pszotatfs),
            numpy.amax(pszotatfs))

        extent = [0, 1, 0, 31]

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(pszotatfs, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower', extent=extent)


        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks([])

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/pszotatfs.png')
    elif name == 'pstffatfs':
        # pstffatfs = list(predictions_res_pstffatfs.copy().values())
        pstffatfs = list(predictions.copy().values())
        pstffatfs = numpy.asarray(pstffatfs)
        print(pstffatfs.shape)
        pstffatfs = pstffatfs[:, numpy.newaxis]
        print(pstffatfs.shape)

        print(numpy.amin(pstffatfs),
            numpy.amax(pstffatfs))

        extent = [0, 1, 0, 31]

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(pstffatfs, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower', extent=extent)


        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks([])

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        
        axs.figure.savefig('analyzed data/figures/pstffatfs.png')
        
    elif name == 'psatpfzot':
        # psatpfzot = list(predictions_res_psatpfzot.copy().items())
        psatpfzot = list(predictions.copy().items())
        psatpfzot = list(list(i[1].values()) for i in psatpfzot)
        psatpfzot = numpy.asarray(psatpfzot)


        print(psatpfzot.shape)

        print(numpy.amin(psatpfzot),
            numpy.amax(psatpfzot))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(psatpfzot, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks(numpy.arange(0, 61, 5))

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/psatpfzot.png')
    
    elif name == 'psatpftff':
        # psatpftff = list(predictions_res_psatpftff.copy().items())
        psatpftff = list(predictions.copy().items())
        psatpftff = list(list(i[1].values()) for i in psatpftff)
        psatpftff = numpy.asarray(psatpftff)

        print(psatpftff.shape)

        print(numpy.amin(psatpftff),
            numpy.amax(psatpftff))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(psatpftff, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks(numpy.arange(0, 61, 5))
        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/psatpftff.png')
    
    elif name == 'pstdpfzot':
        # pstdpfzot = list(predictions_res_pstdpfzot.copy().items())
        pstdpfzot = list(predictions.copy().items())
        pstdpfzot = list(list(list(z for z in i.values())for i in j[1].values()) for j in pstdpfzot)
        pstdpfzot_t1 = numpy.asarray(list(i[0] for i in pstdpfzot))
        pstdpfzot_t2 = numpy.asarray(list(i[1] for i in pstdpfzot))
        pstdpfzot_t3 = numpy.asarray(list(i[2] for i in pstdpfzot))
        
        axs = plt.subplot()
        image = axs.imshow(pstdpfzot_t1, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')


        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks(numpy.arange(0, 61, 5))

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        
        axs.figure.savefig('analyzed data/figures/pstdpfzot_t1.png')
        
        axs = plt.subplot()
        image = axs.imshow(pstdpfzot_t2, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')


        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks(numpy.arange(0, 61, 5))
        axs.figure.savefig('analyzed data/figures/pstdpfzot_t2.png')
        
        axs = plt.subplot()
        image = axs.imshow(pstdpfzot_t3, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')


        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks(numpy.arange(0, 61, 5))
        axs.figure.savefig('analyzed data/figures/pstdpfzot_t3.png')
        
        # display the average for each  stimuli across all subjects
        fig, axes = plt.subplots(1, 3)
        image = axes[0].imshow(pstdpfzot_t1, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')
        image2 = axes[1].imshow(pstdpfzot_t2, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')
        image3 = axes[2].imshow(pstdpfzot_t3, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')
        
    elif name == 'pstdpftff':
        # pstdpftff = list(predictions_res_pstdpftff.copy().items())
        pstdpftff = list(predictions.copy().items())
        pstdpftff = list(list(list(z for z in i.values())for i in j[1].values()) for j in pstdpftff)
        pstdpftff_t1 = numpy.asarray(list(i[0] for i in pstdpftff))
        pstdpftff_t2 = numpy.asarray(list(i[1] for i in pstdpftff))
        pstdpftff_t3 = numpy.asarray(list(i[2] for i in pstdpftff))

        axs = plt.subplot()
        image = axs.imshow(pstdpftff_t1, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')


        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks(numpy.arange(0, 61, 5))

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/pstdpftff_t1.png')
        
        axs = plt.subplot()
        image = axs.imshow(pstdpftff_t2, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')


        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks(numpy.arange(0, 61, 5))
        axs.figure.savefig('analyzed data/figures/pstdpftff_t2.png')
        
        axs = plt.subplot()
        image = axs.imshow(pstdpftff_t3, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')


        _ = axs.set_yticks(list(i for i in range(0, 31)))
        _ = axs.set_xticks(numpy.arange(0, 61, 5))
        axs.figure.savefig('analyzed data/figures/pstdpftff_t3.png')
    
    elif name == 'pfasatst':
        # pfasatst = list(pfasatst.copy().values())
        pfasatst = list(predictions.copy().values())
        pfasatst = numpy.asarray(pfasatst)

        pfasatst = pfasatst[:, numpy.newaxis]
        print(pfasatst.shape)

        print(numpy.amin(pfasatst),
            numpy.amax(pfasatst))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(pfasatst.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/pfasatst.png')
        
    elif name == 'avg_td':
        # res_avg_td = list(predictions_res_avg_td.copy().values())
        res_avg_td = list(predictions.copy().values())
        res_avg_td = numpy.asarray(res_avg_td)

        res_avg_td = res_avg_td[:, numpy.newaxis]
        print(res_avg_td.shape)

        print(numpy.amin(res_avg_td),
            numpy.amax(res_avg_td))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_avg_td.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/res_avg_td.png')
    
    elif name == 'avg_td_fh':
        # res_avg_td_fh = list(predictions_res_avg_td_fh.copy().values())
        res_avg_td_fh = list(predictions.copy().values())
        res_avg_td_fh = numpy.asarray(res_avg_td_fh)

        res_avg_td_fh = res_avg_td_fh[:, numpy.newaxis]
        print(res_avg_td_fh.shape)

        print(numpy.amin(res_avg_td_fh),
            numpy.amax(res_avg_td_fh))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_avg_td_fh.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/res_avg_td_fh.png')
        
    elif name == 'avg_td_sh':
        # res_avg_td_sh = list(predictions_res_avg_td_sh.copy().values())
        res_avg_td_sh = list(predictions.copy().values())
        res_avg_td_sh = numpy.asarray(res_avg_td_sh)

        res_avg_td_sh = res_avg_td_sh[:, numpy.newaxis]
        print(res_avg_td_sh.shape)

        print(numpy.amin(res_avg_td_sh),
            numpy.amax(res_avg_td_sh))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_avg_td_sh.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/res_avg_td_sh.png')

    elif name == 'vis_zot':
        # res_vis_zot = list(predictions_res_vis_zot.copy().values())
        res_vis_zot = list(predictions.copy().values())
        res_vis_zot = numpy.asarray(res_vis_zot)

        res_vis_zot = res_vis_zot[:, numpy.newaxis]
        print(res_vis_zot.shape)

        print(numpy.amin(res_vis_zot),
            numpy.amax(res_vis_zot))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_vis_zot.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')


        _ = axs.set_yticks([])
        _ = axs.set_xticks(numpy.arange(0, 61, 5))

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/res_vis_zot.png')

    elif name == 'vis_tff':
        # res_vis_tff = list(predictions_res_vis_tff.copy().values())
        res_vis_tff = list(predictions.copy().values())
        res_vis_tff = numpy.asarray(res_vis_tff)

        res_vis_tff = res_vis_tff[:, numpy.newaxis]
        print(res_vis_tff.shape)

        print(numpy.amin(res_vis_tff),
            numpy.amax(res_vis_tff))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_vis_tff.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')


        _ = axs.set_yticks([])
        _ = axs.set_xticks(numpy.arange(0, 61, 5))
        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/res_vis_tff.png')

    elif name == 'vis_zot_td':
        # res_vis_zot_td = list(predictions_res_vis_zot_td.copy().values())
        res_vis_zot_td = list(predictions.copy().values())
        res_vis_zot_td = list(list(i.values()) for i in res_vis_zot_td)
        res_vis_zot_td_1 = res_vis_zot_td[0]
        res_vis_zot_td_2 = res_vis_zot_td[1]
        res_vis_zot_td_3 = res_vis_zot_td[2]

        res_vis_zot_td = numpy.asarray(res_vis_zot_td_1)

        res_vis_zot_td = res_vis_zot_td[:, numpy.newaxis]
        print(res_vis_zot_td.shape)

        print(numpy.amin(res_vis_zot_td),
            numpy.amax(res_vis_zot_td))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_vis_zot_td.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())

        _ = axs.set_xticks(numpy.arange(0, 61, 10))
        _ = axs.set_yticks([])
        axs.figure.savefig('analyzed data/figures/res_vis_zot_td_1.png')

        res_vis_zot_td_2 = numpy.asarray(res_vis_zot_td_2)

        res_vis_zot_td_2 = res_vis_zot_td_2[:, numpy.newaxis]
        print(res_vis_zot_td_2.shape)

        print(numpy.amin(res_vis_zot_td_2),
            numpy.amax(res_vis_zot_td_2))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_vis_zot_td_2.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        _ = axs.set_xticks(numpy.arange(0, 61, 10))
        _ = axs.set_yticks([])
        axs.figure.savefig('analyzed data/figures/res_vis_zot_td_2.png')

        res_vis_zot_td_3 = numpy.asarray(res_vis_zot_td_3)

        res_vis_zot_td_3 = res_vis_zot_td_3[:, numpy.newaxis]
        print(res_vis_zot_td_3.shape)

        print(numpy.amin(res_vis_zot_td_3),
            numpy.amax(res_vis_zot_td_3))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_vis_zot_td_3.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        _ = axs.set_xticks(numpy.arange(0, 61, 10))
        _ = axs.set_yticks([])

        axs.figure.savefig('analyzed data/figures/res_vis_zot_td_3.png')
        
    elif name == 'vis_tff_td':
        # res_vis_tff_td = list(predictions_res_vis_tff_td.copy().values())
        res_vis_tff_td = list(predictions.copy().values())
        res_vis_tff_td = list(list(i.values()) for i in res_vis_tff_td)
        res_vis_tff_td_1 = res_vis_tff_td[0]
        res_vis_tff_td_2 = res_vis_tff_td[1]
        res_vis_tff_td_3 = res_vis_tff_td[2]

        res_vis_tff_td_1 = numpy.asarray(res_vis_tff_td_1)

        res_vis_tff_td_1 = res_vis_tff_td_1[:, numpy.newaxis]
        print(res_vis_tff_td_1.shape)

        print(numpy.amin(res_vis_tff_td_1),
            numpy.amax(res_vis_tff_td_1))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_vis_tff_td_1.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        _ = axs.set_xticks(numpy.arange(0, 61, 10))
        _ = axs.set_yticks([])

        axs.set_adjustable('datalim')
        print(image.get_extent(),
            image.get_window_extent(),
            image.get_window_extent(),
            axs.viewLim,
            axs.artists,
            axs.get_adjustable(),
            axs.get_aspect(),
            axs.get_data_ratio(),
            axs.get_xscale())
        axs.figure.savefig('analyzed data/figures/res_vis_tff_td_1.png')

        res_vis_tff_td_2 = numpy.asarray(res_vis_tff_td_2)

        res_vis_tff_td_2 = res_vis_tff_td_2[:, numpy.newaxis]
        print(res_vis_tff_td_2.shape)

        print(numpy.amin(res_vis_tff_td_2),
            numpy.amax(res_vis_tff_td_2))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_vis_tff_td_2.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')

        _ = axs.set_xticks(numpy.arange(0, 61, 10))
        _ = axs.set_yticks([])
        axs.figure.savefig('analyzed data/figures/res_vis_tff_td_2.png')

        res_vis_tff_td_3 = numpy.asarray(res_vis_tff_td_3)

        res_vis_tff_td_3 = res_vis_tff_td_3[:, numpy.newaxis]
        print(res_vis_tff_td_3.shape)

        print(numpy.amin(res_vis_tff_td_3),
            numpy.amax(res_vis_tff_td_3))

        # display the average for each  stimuli across all subjects
        axs = plt.subplot()
        image = axs.imshow(res_vis_tff_td_3.T, aspect='auto', cmap='jet', vmin=0., vmax=1.,
                        interpolation='none', origin='lower')
        _ = axs.set_xticks(numpy.arange(0, 61, 10))
        _ = axs.set_yticks([])                
        axs.figure.savefig('analyzed data/figures/res_vis_tff_td_3.png')
        
                
        
    
        