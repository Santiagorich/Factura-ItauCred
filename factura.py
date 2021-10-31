import fitz 
import re
import sys
import os
from collections import defaultdict as ddict

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



with fitz.open(sys.argv[1]) as doc:
    text = ""
    for page in doc:
        text += page.getText()

op = 'y'


while(op.lower()=='y'):
    for matches in re.findall("([0-9]{2} ){3}(.*[A-Z].* )(.[0-9].*)", text):
        print(matches[1]+' '+matches[2])
    lookfor = input('Buscar: ')

    sum = 0.0

    for matches in re.findall("([0-9]{2} ){3}(.*[A-Z].* )(.[0-9].*)", text):


        if (lookfor.lower() in matches[1].lower()):
            print(matches[1]+' '+matches[2])
            sum = sum + float(matches[2].replace('.','').replace(',', '.'))
            
    print('Total: $%s' % round(sum))
    op = input('Continue? Y/N\n')
    cls()






