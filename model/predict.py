import random
import json
import pickle
import numpy as np
from datetime import datetime, date
import nltk
from nltk.stem import WordNetLemmatizer
import spotify
from tensorflow.keras.models import load_model

lemmantizer = WordNetLemmatizer()

intents = json.load(open("model/intents.json"))

words = pickle.load(open('model/words.pkl', "rb"))
classes = pickle.load(open('model/classes.pkl', "rb"))
model = load_model("model/chatbotmodel.h5")
ignore_letters = ["?", "!", ".", ","]


def cleen_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmantizer.lemmatize(
        word) for word in sentence_words if word not in ignore_letters]
    sentence_words = [word.lower() for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = cleen_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_TRESHHOLD = 0.25
    resoult = [[i, r] for i, r in enumerate(res) if r > ERROR_TRESHHOLD]

    resoult.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in resoult:
        return_list.append({"intent": classes[r[0]], "probability": r[1]})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]["intent"]
    if intents_list[0]['probability'] < 0.65:
        return "I don't understand. Please try again."

    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i["tag"] == tag:
            resoult = random.choice(i["responses"])
            if tag == "time":
                resoult = resoult.replace(
                    "xxx", datetime.now().strftime("%H:%M"))
            if tag == "date":
                resoult = resoult.replace(
                    "xxx", date.today().strftime("%d/%m/%Y"))
            if tag == "music":
                spotify.play()
            if tag == "music-stop":
                spotify.stop()
            break
    return resoult


def predict(sentence):
    ints = predict_class(sentence)
    res = get_response(ints, intents)
    return res
