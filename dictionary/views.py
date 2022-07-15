from django.shortcuts import render
import requests
import json
from django.contrib import messages
from random_word import RandomWords

def start_dictionary(request):
    try:
        r = RandomWords()
        random_word_def_text = r.word_of_the_day()
        jsonformat = json.loads(random_word_def_text)
        query = jsonformat['word']
        print('worked')
    except:
        query = None
        print('didnt work')        


    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q'].capitalize()


    definition_list = []
    audios = []
    texts = []
    try:
        dict = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{query}').text
        word_info = json.loads(dict)
        for x in word_info:
            meanings = x['meanings']
            for y in meanings:
                all_definitions = y['definitions']
                partOfSpeech = y['partOfSpeech']
                for definitions in all_definitions:
                    full_word_def = {
                        'partOfSpeech':partOfSpeech,
                        'definition': definitions['definition'],
                    }
                    definition_list.append(full_word_def)

            phonetics = x['phonetics']
            if phonetics == []:
                audio = 'N/A'
                text = 'N/A'
                audios.append(audio)
                texts.append(text)
            else:
                for z in phonetics:
                    try:
                        audio = z['audio']
                        text = z['text']
                    except:
                        audio = 'N/A'
                        text = 'N/A'
                    audios.append(audio)
                    texts.append(text)
    except:
        messages.error(request,"Word entered is not in the dictionary!!")
        audio = 'N/A'
        text = 'N/A'
        audios.append(audio)
        texts.append(text)


    
    
    context = {
        'query': query,
        'definition_list': definition_list,
        'audios':audios[0],
        'pronouncing': texts[0],
    }
    

    return render(request, 'dictionary/dictionary.html', context)
