import os
import librosa
import soundfile as sf
from data_tools import audio_files_to_numpy
from data_tools import blend_noise_randomly, numpy_audio_to_matrix_spectrogram
import numpy as np

# 
def synthesis(noise_dir, voice_dir,path_save_sound, frame_length,sample_rate,hop_length_frame_noise,
              hop_length_frame,nb_samples):
    """this function make 3 files that synthesis noise files and clean voice files"""

    list_noise_files = os.listdir(noise_dir)
    list_voice_files = os.listdir(voice_dir)
    
    # remove ipynb_checkpoints
    def remove_ipynb_checkpoints(ipc):
        """remove mac specific file if present"""
        if '.ipynb_checkpoints' in ipc:
            ipc.remove('.ipynb_checkpoints')
        return ipc

    # remove ds_store from Mac
    def remove_ds_store(lst):
        """remove mac specific file if present"""
        if '.DS_Store' in lst:
            lst.remove('.DS_Store')
        return lst

    
    list_noise_files = remove_ipynb_checkpoints(list_noise_files)
    list_voice_files = remove_ipynb_checkpoints(list_voice_files)
    list_noise_files = remove_ds_store(list_noise_files)
    list_voice_files = remove_ds_store(list_voice_files)

    nb_voice_files = len(list_voice_files) # return length of voice files
    nb_noise_files = len(list_noise_files) # return length of noise files


    # Extracting noise and voice from folder and convert to numpy
    noise = audio_files_to_numpy(noise_dir, list_noise_files, sample_rate,
                                     frame_length, hop_length_frame_noise)

    voice = audio_files_to_numpy(voice_dir, list_voice_files, sample_rate, 
                                     frame_length, hop_length_frame)

    # Blend some clean voices with random selected noises (and a random level of noise)
    prod_voice, prod_noise, prod_noisy_voice = blend_noise_randomly(
            voice, noise, nb_samples, frame_length)
    print("prod_voice:{}, prod_noise:{}, prod_noisy_voice:{}"
          .format(np.shape(prod_voice),np.shape(prod_noise),np.shape(prod_noisy_voice)))
    # To save the long audio generated to disk to QC:
    noisy_voice_long = prod_noisy_voice.reshape(1, nb_samples * frame_length)
    sf.write(path_save_sound + 'noisy_voice_long.wav', noisy_voice_long[0, :], sample_rate)
    voice_long = prod_voice.reshape(1, nb_samples * frame_length)
    sf.write(path_save_sound + 'voice_long.wav', voice_long[0, :], sample_rate)
    noise_long = prod_noise.reshape(1, nb_samples * frame_length)
    sf.write(path_save_sound + 'noise_long.wav',noise_long[0, :], sample_rate)

