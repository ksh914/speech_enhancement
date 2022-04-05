import scipy
from scipy.io.wavfile import read,write
from IPython import display as IPD
import numpy as np
from matplotlib import pyplot as plt

from scipy.fft import fft, fftfreq,ifft
from scipy.signal import stft,istft

def fft(N,sr_input,audio_input,cutoff_f, low_pass=True):
  sr_noisy, noisy = read('./data/Train/sound/noisy_voice_long.wav')
  sr_input, audio_input= read('./data/Train/sound/voice_long.wav')
  fft_x = fft(audio_input)
  T = 1.0 / sr_input
  xf = fftfreq(N, T) 
  mask=np.ones(audio_input.shape[0])
  
  if low_pass:
      mask = np.abs(xf)<cutoff_f
  else:
      mask = np.abs(xf)>cutoff_f
  
  fft_y = fft_x*mask
  answer = ifft(fft_y)
