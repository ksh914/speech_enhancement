```
3.30

data_tools 의 audio_files_to_numpy와 audio_to_audio_frame_stack 가 어떻게 작동하는지에 대해서

My_test.py에 프로그래밍을 돌려 보았다.

4.4 
Check scaling and acknowledge the statistical number of files from stats.describe()
and must scaled between -1 and 1(not yet)

4.5
코딩 과정에서 나온 scipy.io.wavfile.read 와 librosa.load의 차이점에서의 오류를 찾아냈다.

librosa는 데이터의 범위가 -1 에서 1 사이지만, 

scipy.io.wavfile.read는 numpy.int16 즉 정수형으로 numpy array를 반환한다.

scipy_wav[0].type : <class 'numpy.int16>

librosa_wav[0].type : <class 'numpy.float32>

따라서 fft를 하고 난 뒤, wav파일을 load할 때 type을 맞추거나 librosa or scipy 둘 중에 하나만 써야할 것 같다는 판단을 했다.
```