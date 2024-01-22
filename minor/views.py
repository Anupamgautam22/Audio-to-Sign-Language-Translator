
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import nltk
from nltk.stem import WordNetLemmatizer 
import string
import re
from nltk.stem.porter import PorterStemmer
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import numpy as np
from scipy.io import wavfile
from scipy import signal
import IPython.display as ipd




def home_view(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def create(request):
    if request.method == 'POST':
        text = request.POST['textarea']
        
        nltk.download('averaged_perceptron_tagger')
        
        text=text.lower()
        text = re.sub(" \d+", " ", text)
        # print(text)

        nltk.download('stopwords')
        nltk.download('punkt')
        text= re.sub(r'[^\w\s]', '', text)
        # print(text)

        
          
        stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",
                      'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', 
                      "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])
        # word_tokens = word_tokenize(text)
        
        # filtered_words= [w for w in word_tokens if not w in stop_words] 
        # porter = PorterStemmer()
        # text = [porter.stem(word) for word in filtered_words]
        # # text=filtered_words
        # # print(filtered_sentence)
        
        # nltk.download('wordnet')
        # nltk.download('omw-1.4')
        
        
        # wordnet_lemmatizer = WordNetLemmatizer()
        # for w in text:
        #    w = nltk.word_tokenize(w)
        # for w in text:
                    
        #             w = w.format(w, wordnet_lemmatizer.lemmatize(w,pos='v'))
        
        # print(text)
        word_tokens = word_tokenize(text)
        filtered_words = [w for w in word_tokens if not w in stop_words]
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        wordnet_lemmatizer = WordNetLemmatizer()
        text = [wordnet_lemmatizer.lemmatize(word, pos='v') for word in filtered_words]

        print(text)
        return render(request, "home.html", { 'text': text})
    else:
        return render(request, 'home.html')


def speak(request):
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Say something!")
      audio = r.listen(source)
    try:

        text = r.recognize_google(audio)
       
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    
    text=text.lower()
    text = re.sub(" \d+", " ", text)
    
    

    nltk.download('stopwords')
    nltk.download('punkt')
    text= re.sub(r'[^\w\s]', '', text)
    

    
        
    # stop_words = set(stopwords.words('english')) 
    stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",
                      'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', 
                      "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])
    # word_tokens = word_tokenize(text)
    
    # filtered_words= [w for w in word_tokens if not w in stop_words] 
    # # porter = PorterStemmer()
    # # text = [porter.stem(word) for word in filtered_words]
    # text=filtered_words
    # # print(filtered_sentence)
    
    # nltk.download('wordnet')
    # nltk.download('omw-1.4')
    
    
    # wordnet_lemmatizer = WordNetLemmatizer()
    # for w in text:
    #     w = nltk.word_tokenize(w)
    # for w in text:
                
    #             w = w.format(w, wordnet_lemmatizer.lemmatize(w,pos='v'))
    
    # print(text)
    word_tokens = word_tokenize(text)
    filtered_words = [w for w in word_tokens if not w in stop_words]
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    wordnet_lemmatizer = WordNetLemmatizer()
    text = [wordnet_lemmatizer.lemmatize(word, pos='v') for word in filtered_words]

    print(text)
    return render(request, "home.html", { 'text': text})
    
# return render(request, 'speak.html')
def speakmodel(request):
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
    
    
            
    from keras.models import load_model
    # model.save("SpeechRecogModel.h5")
    model=load_model('minor\SpeechRecogModel.h5')

    # Set file path and sampling rate
    filepath = "./"
    filename = "recorded_audio6.wav"
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

    classes =['down', 'go', 'left', 'no', 'off', 'on', 'right', 'stop', 'up', 'yes',]

    def predict(audio):
        prob = model.predict(audio.reshape(1, target_sr, 1))
        index = np.argmax(prob[0])
        return classes[index]

    #converting voice commands to text
    # predict(samples)
    text = predict(samples)
    
    text = nltk.word_tokenize(text)
    print("Predicted text: ", text)
    return render(request, "home.html", { 'text': text})

    