'''
Created on 21 mar 2022

@author: mauro
'''

from Analisi_freq import *

def print_command():
    print("1 per aggiornare e stampare stampare il testo")
    print("2 per l'analisi di frequenza")
    print("3 per stampare il dizionario")
    print("4 per effettuare uno swap char")
    print("5 per lo score del testo")
    print("6 per match delle parole monolettera")
    print("7 per best_swap")
    print("exit per uscire")
    
def stampa_diz(diz):
    for key in diz:
        print(key , "-", diz[key])
        
        
def stampa_testo(text):
    lines = text.splitlines()
    input_utente = int(input("numero di righe da visualizzare"))
    number_line = input_utente if input_utente < len(lines) else len(lines)
    for i in range(0, number_line):
        print(lines[i])

def main():
    nome_file = input("inserire nome del file: ")
    file = open(nome_file, "r")
    text = file.read()
    diz = {}
    while True:
        print_command()
        command = input("inserisci comando: ")
        if command == "1":
            stampa_testo(text)
        elif command == "2":
            crea_freq(text)
        elif command == "3":
            stampa_diz(diz)
        elif command == "4":
            vecchio_car = input("inserisci il carattere da sostituire: ")
            while len(vecchio_car)!=1:
                vecchio_car = input("inserisci il carattere da sostituire: ")
            nuovo_car = input("inserisci il nuovo carattere: ")
            while len(nuovo_car)!=1:
                nuovo_car = input("inserisci il nuovo carattere")
            text = swap_char_in_new_text(text,vecchio_car, nuovo_car)
            diz[vecchio_car]=nuovo_car
        elif command =="5":
            print(score(text))
        elif command == "6":
            match_monolettera(text)
        elif command == "7":
            best_swap(text)
        elif command == "exit":
            break
            
    

if __name__ == '__main__':
    main()