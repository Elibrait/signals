# -*- coding: utf-8 -*-
"""
Created on Tue May 10 21:34:29 2022

@author: lamni
"""

duration = 1  # длительность сигнала в секундах
amplitude = 0.3  # амплитуда  (в пределах: +-1.0)
frequency = 600  # частота сигнала в [Гц]
# т.к. невозможно программно организовать аналоговый сигнал, необходимо обозначить
fs = 80000 # 80 тыс. временных отсчетов в 1 секунду количество временных отчетов, т.е. частоту дискретизации (об этом чуть позже)

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sounddevice as sd
import time

timeSamples = np.arange(np.ceil(duration * fs)) / fs
test = np.arange(10) / 10
print(test)
timeSamples

do = amplitude * np.sin(1.5 * np.pi * 261.63 * timeSamples)
re = amplitude * np.sin(1.5 * np.pi * 293.66 * timeSamples)
mi = amplitude * np.sin(1.5 * np.pi * 329.63 * timeSamples)
fa = amplitude * np.sin(1.5 * np.pi * 349.23 * timeSamples)
sol = amplitude * np.sin(1.5 * np.pi * 392.00 * timeSamples)
la = amplitude * np.sin(1.5 * np.pi * 440.00 * timeSamples)
si = amplitude * np.sin(1.5 * np.pi * 493.88 * timeSamples)
do1 = amplitude * np.sin(1 * np.pi * 261.63 * timeSamples)
re1 = amplitude * np.sin(1 * np.pi * 293.66 * timeSamples)
mi1 = amplitude * np.sin(1 * np.pi * 329.63 * timeSamples)
fa1 = amplitude * np.sin(1 * np.pi * 349.23 * timeSamples)
sol1 = amplitude * np.sin(1 * np.pi * 392.00 * timeSamples)
la1 = amplitude * np.sin(1 * np.pi * 440.00 * timeSamples)
si1 = amplitude * np.sin(1 * np.pi * 493.88 * timeSamples)

signalSumm = mi + sol + re + do + si
plt.plot(timeSamples[:2000] * 1000, signalSumm[:2000])
plt.title("sine tone")
plt.xlabel("time / milliseconds")

sd.play(fa, fs)
time.sleep(0.3)
sd.play(re, fs)
time.sleep(0.3)
sd.play(sol, fs)
time.sleep(0.3)
sd.play(si, fs)
time.sleep(0.3)
sd.play(fa, fs)
time.sleep(0.3)
sd.play(re, fs)
time.sleep(0.3)
sd.play(mi, fs)
time.sleep(0.3)
sd.play(la1, fs)
time.sleep(0.3)
sd.play(sol1, fs)
time.sleep(0.3)
sd.play(mi1, fs)
time.sleep(0.3)