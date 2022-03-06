# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 12:11:00 2022

@author: Alice
"""

import pandas as pd
import glob

# %% Import sleep data

path = r'C:\Users\Alice\Documents\GitHub\meercat\meercat_data_sleep' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for full_filename in all_files:
    filename = full_filename.split("\\")[-1]
    if filename.split("_")[0] == "ecg":
        print(filename)
        df = pd.read_csv(full_filename, index_col=None, names=['ecg'])
        li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

# %%
from sleepecg import detect_heartbeats

test_ecg = list(li[0]['ecg'])
fs = len(test_ecg)/45
detection = detect_heartbeats(test_ecg, fs)

# %%
from sleepecg import load_classifier
clf = load_classifier('ws-gru-mesa', r'C:\Users\Alice\Documents\Github\Melavoltin\classifier')

# %%
from sleepecg import load_classifier, plot_hypnogram, read_slpdb, stage

# %% Load record
# `ws-gru-mesa` performs poorly for most SLPDB records. It does however
# work well for slp03.
rec = next(read_slpdb('slp03'))

# %% Predict stages and plot hypnogram
import sleepecg
import datetime
import matplotlib.pyplot as plt
from sleepecg import detect_heartbeats
import numpy as np

test_ecg = list(li[0]['ecg'])
fs = len(test_ecg)/70
detection = detect_heartbeats(df['ecg'], fs)
print("average: " + str(np.mean(np.diff(detection))))
plt.plot(np.diff(detection))

# %%

from scipy.signal import find_peaks
ecg_data = df['ecg']
peaks, _ = find_peaks(ecg_data, height=2200, distance=80)
peaks = peaks/100
plt.plot(np.diff(peaks))

# %%
ecg_data = np.loadtxt(r"C:\Users\Alice\Desktop\ecg_data.txt", delimiter=',')
peaks, _ = find_peaks(ecg_data, height=2200, distance=80)
peaks = peaks/100

# %%

start_time = datetime.time(hour=0, minute=0, second=0, microsecond=0)
rec = sleepecg.SleepRecord(heartbeat_times=peaks,
                           recording_start_time=start_time)
stages_pred = stage(clf, rec, return_mode='prob')

plot_hypnogram(
    rec,
    stages_pred,
    stages_mode=clf.stages_mode,
    merge_annotations=True,
)