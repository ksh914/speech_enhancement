import os
import librosa
import soundfile as sf
from data_tools import audio_files_to_numpy
from data_tools import blend_noise_randomly, numpy_audio_to_matrix_spectrogram
import numpy as np


def detach(path_save_time_serie, path_save_sound, path_save_sound2,path_save_spectrogram, 
sample_rate, frame_length, nb_samples, n_fft, hop_length_fft):
    """read 3 files from create_data.py and make spectrogram and time series """
    
        prod_noisy_voice,sr1 = librosa.load(path_save_sound+'noisy_voice_long',sr=16000)
        prod_noisy_voice = prod_noisy_voice.reshape(nb_samples,frame_length)
        prod_voice,sr2 = librosa.load(path_save_sound+'voice_long',sr=16000)
        prod_voice = prod_voice.reshape(nb_samples,frame_length)
        prod_noise,sr3 = librosa.load(path_save_sound+'noise_long',sr=16000)
        prod_noise = prod_noise.reshape(nb_samples,frame_length)
        
        # Squared spectrogram dimensions
        dim_square_spec = int(n_fft / 2)+1  #256

        # Create Amplitude and phase of the sounds
        m_amp_db_voice,  m_pha_voice = numpy_audio_to_matrix_spectrogram(
                prod_voice, dim_square_spec, n_fft, hop_length_fft)
        m_amp_db_noise,  m_pha_noise = numpy_audio_to_matrix_spectrogram(
                prod_noise, dim_square_spec, n_fft, hop_length_fft)
        m_amp_db_noisy_voice,  m_pha_noisy_voice = numpy_audio_to_matrix_spectrogram(
                prod_noisy_voice, dim_square_spec, n_fft, hop_length_fft)

        # Save to disk for Training / QC
        np.save(path_save_time_serie + 'voice_timeserie', prod_voice)
        np.save(path_save_time_serie + 'noise_timeserie', prod_noise)
        np.save('./fft/time_serie/' + 'voice_timeserie', prod_voice)
        np.save('./fft/time_serie/' + 'noise_timeserie', prod_noise)
        np.save(path_save_time_serie + 'noisy_voice_timeserie', prod_noisy_voice)


        np.save(path_save_spectrogram + 'voice_amp_db', m_amp_db_voice)
        np.save(path_save_spectrogram + 'noise_amp_db', m_amp_db_noise)
        np.save('./fft/spectrogram/' + 'voice_amp_db', m_amp_db_voice)
        np.save('./fft/spectrogram/' + 'noise_amp_db', m_amp_db_noise)
        np.save(path_save_spectrogram + 'noisy_voice_amp_db', m_amp_db_noisy_voice)

        np.save(path_save_spectrogram + 'voice_pha_db', m_pha_voice)
        np.save(path_save_spectrogram + 'noise_pha_db', m_pha_noise)
        np.save('./fft/spectrogram/' + 'voice_pha_db', m_pha_voice)
        np.save('./fft/spectrogram/' + 'noise_pha_db', m_pha_noise)
        np.save(path_save_spectrogram + 'noisy_voice_pha_db', m_pha_noisy_voice)
