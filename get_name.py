import nltk
from nameparser.parser import HumanName
import re

def get_human_names(text):
    # uncomment below line for the first time
    # nltk.download()

    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        for part in person:
            name += part + ' '
        if name[:-1] not in person_list:
            person_list.append(name[:-1])
        name = ''    
        person = []

    return (person_list)

def get_age(text):
    return re.findall(r'\d{1,3}', text)[0]


