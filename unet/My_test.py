import librosa
import os
import numpy as np

y,sr = librosa.load('./unet/data/Train/clean_voice/p257_139.wav',sr=16000)
voice_dir = './unet/data/Train/clean_voice'

list_voice_files = os.listdir(voice_dir)

def remove_ipynb_checkpoints(ipc):
    """remove mac specific file if present"""
    if '.ipynb_checkpoints' in ipc:
        ipc.remove('.ipynb_checkpoints')
    return ipc


def remove_ds_store(lst):
    """remove mac specific file if present"""
    if '.DS_Store' in lst:
        lst.remove('.DS_Store')
    return lst

#remove ds_store, ipynb_checkpoints
list_voice_files = remove_ipynb_checkpoints(list_voice_files)
list_voice_files = remove_ds_store(list_voice_files)

nb_voice_files = len(list_voice_files)
    
def audio_to_audio_frame_stack(sound_data, frame_length, hop_length_frame):
    """This function take an audio and split into several frame
       in a numpy matrix of size (nb_frame,frame_length)"""

    sequence_sample_length = sound_data.shape[0] # total_duration * sample_rate

    sound_data_list = [sound_data[start:start + frame_length] for start in range(
    0, sequence_sample_length - frame_length + 1, hop_length_frame) ]# get sliding windows
    
    for start in range(0, sequence_sample_length - frame_length + 1, hop_length_frame):
        print(start)
        
    sound_data_array = np.vstack(sound_data_list)

    return sound_data_array

def audio_files_to_numpy(audio_dir, list_audio_files, sample_rate, frame_length, hop_length_frame):
    """This function take audio files of a directory and merge them
    in a numpy matrix of size (nb_frame,frame_length) for a sliding window of size hop_length_frame"""

    list_sound_array = []

    for file in list_audio_files:
        # open the audio file
        y, sr = librosa.load(os.path.join(audio_dir, file), sr=sample_rate)
        total_duration = librosa.get_duration(y=y, sr=sr)

        list_sound_array.append(audio_to_audio_frame_stack(
            y, frame_length, hop_length_frame))
        

    return np.vstack(list_sound_array)


voice = audio_files_to_numpy(voice_dir, list_voice_files, 16000, 
                                     16128, 16128)

print(np.shape(voice))