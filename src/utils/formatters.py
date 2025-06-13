import re
import os

def convert_info(value):
    if value == True: 
        return "Sim"
    elif value == False:  
        return "Não"
    return value

def remover_titulos(nome):
    return re.sub(r'\b(Dr\.|Dra\.|Sr\.|Srta\.)\b', '', nome).strip()

