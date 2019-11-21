import json 
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0: 
        yn = input("Did you mean %s instead? \n enter y or n \n" %get_close_matches(w, data.keys())[0])
        if yn.lower() == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        else: 
            return "good bye!"
    else: 
        return "Do not exist"
    
    
word = input("Enter Word: ")
output = translate(word)

if type(output) == list:
    for item in output: 
        print(item)
else:
    print(output)