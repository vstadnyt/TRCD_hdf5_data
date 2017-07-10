def smooth(y, box_pts):
    #This is a box smoothing function
    #Created by Valentyn Stadnytskyi (v.stadnytskyi@gmail.com) and tested on Python 2.7. for TRCD data processing
    ####
    
    import numpy as np
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth
