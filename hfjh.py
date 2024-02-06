import sounddevice as sd
from scipy.io.wavfile import write

duration = 1  # seconds
fs = 16000  # sampling rate
filename = 'recorded_audio2.wav'

print('Please speak into the microphone...')
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()  # wait for recording to finish
print('Recording finished.')

write(filename, fs, myrecording)  # save the recording to a file
