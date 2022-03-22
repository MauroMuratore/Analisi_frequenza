'''
Created on 21 mar 2022

@author: mauro
'''

import re

def crea_freq(testo, stampa=True):
    freq={}
    for carattere in testo:
        if carattere in freq:
            freq[carattere] += 1
        else:
            freq[carattere] = 1
    
    lung = len(testo)
    for carattere in freq:
        freq[carattere] = freq[carattere]*100/lung
    
    if stampa:        
        stampa_dizionario_ordinato(freq)
    
    return freq
    
def takeSecond(element):
    return element[1]

def takeThird(element):
    return element[2]    

def stampa_dizionario_ordinato(diz):
    tuple_char_freq = []
    for key in diz:
        tuple_char_freq.append( (key, diz[key]) )
    
    tuple_char_freq.sort(key=takeSecond, reverse=True)
    
    for coppia in tuple_char_freq:
        print(coppia)    
        


def swap_char_in_new_text(text, vecchio_car, nuovo_car):
    ritorno = ""
    for i in range(0, len(text)):
        if text[i]==vecchio_car:
            ritorno += nuovo_car
        elif text[i]==nuovo_car:
            ritorno += vecchio_car
        else:
            ritorno += text[i]
        
    print(ritorno[0:5000])
    return ritorno


def score(text):
    file = open("match_parole.txt", "r")
    words = file.read()
    file.close()
    score = {"1":0 , "2":0, "3":0}
    
    for strg in text.split():
        s = re.sub(r'[^a-zA-Z]', '', strg)
        
        if len(s)==1:
            if s.lower() in words:
                score["1"]+=1
            else:
                score["1"]-=1
        elif len(s)==2:
            if s.lower() in words:
                score["2"]+=1
            else:
                score["2"]-=1
        elif len(s)==3:
            if s.lower() in words:
                score["3"]+=1
            else:
                score["3"]-=1
    
    return score

def match_monolettera(text):
    splitted = text.split()
    diz = {}
    for parola in splitted:
        if len(parola)==1:
            if parola in diz:
                diz[parola]+=1
            else:
                diz[parola]=1
    
    stampa_dizionario_ordinato(diz)    

def crea_freq_table_from_file():
    file = open("freq_inglese.txt", "r")
    testo = file.read()
    file.close()
    lista_inglese = testo.split("\n")
    dir_inglese = {}
    for line in lista_inglese:
        if line=="":
            continue
        line_split = line.split()
        dir_inglese[line_split[0]] = line_split[1]
    return dir_inglese

def best_swap(text):
    lettera = input("inserisci lettera: ")
    my_table_freq = crea_freq(text, False) 
    en_table_freq = crea_freq_table_from_file()
    my_freq = my_table_freq[lettera]
    range = my_freq * 0.3
    candidate = []
    for key in en_table_freq:
        candidate.append(key)
    my_match = score(text)
    my_sum = my_match["1"] + my_match["2"] + my_match["3"]
    list_cand = []
    for key in candidate:
        text_dec = text.replace(lettera, key)
        match_ = score(text_dec)
        sum = match_["1"] + match_["2"] + match_["3"]
        if(my_sum<sum):
            list_cand.append((key, match_, sum))
    
    list_cand.sort(key=takeThird, reverse=True)
    for i in list_cand:
        print(i)













