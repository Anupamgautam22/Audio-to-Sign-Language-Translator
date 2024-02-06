# import sounddevice as sd
# import soundfile as sf
import numpy as np
from scipy.io import wavfile
from scipy import signal
import IPython.display as ipd

from keras.models import load_model
# model.save("SpeechRecogModel.h5")
model=load_model('SpeechRecogModel.h5')

# Set file path and sampling rate
filepath = "./"
filename = "recorded_audio2.wav"
sr = 16000
target_sr = 8000

# Load audio file and resample to target_sr Hz
_, samples = wavfile.read(filepath + filename)
samples = signal.resample(samples, int(len(samples) * float(target_sr) / sr))

# Pad or truncate audio to be exactly target_sr samples long
if len(samples) < target_sr:
    samples = np.pad(samples, (0, target_sr - len(samples)), 'constant')
else:
    samples = samples[:target_sr]

# Play audio using IPython.display
ipd.Audio(samples, rate=target_sr)

classes =['down', 'go', 'left', 'no', 'off', 'on', 'right', 'stop', 'up', 'yes']

def predict(audio):
    prob = model.predict(audio.reshape(1, target_sr, 1))
    index = np.argmax(prob[0])
    return classes[index]

#converting voice commands to text
# predict(samples)
text = predict(samples)
print("Predicted text: ", text)
