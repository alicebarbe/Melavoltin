
import numpy as np
from scipy.signal import find_peaks
import basichrv

def calculate_rr(ecg_data, time_elapsed):
    peaks, _ = find_peaks(ecg_data, height=2200, distance=80)
    rr_arr = np.diff(peaks)
    rr_arr = rr_arr * time_elapsed / len(ecg_data)
    print(f"Number of beats: {len(rr_arr)}")
    return rr_arr

def get_hrv(rr):
    tdf, oc = basichrv.gethrv(rr)
    reading = {}
    reading['ectopic'] = oc
    reading['hrstd'] = tdf['std_hr']
    reading['hr'] = tdf['mean_hr']
    reading['hrv'] = tdf['sdnn']

    return reading
