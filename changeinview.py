 stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",
                      'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', 
                      "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])
        # word_tokens = word_tokenize(text)
        
        # filtered_words= [w for w in word_tokens if not w in stop_words] 
        # porter = PorterStemmer()
        # text = [porter.stem(word) for word in filtered_words]
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