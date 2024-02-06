import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

duration = 5  # seconds
fs = 16000  # sampling rate
filename = 'recorded_audio6.wav'
threshold = 0.01  # minimum amplitude to trigger recording

print('Please speak into the microphone...')
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()  # wait for recording to finish

# find start and end indices of audio with amplitude greater than threshold
start = np.argmax(myrecording > threshold)
end = len(myrecording) - np.argmax(myrecording[::-1] > threshold)

print('Recording finished.')
write(filename, fs, myrecording[start:end])  # save the recording to a file
