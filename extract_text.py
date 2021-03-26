'''
@Author: rishi
'''

from datetime import date as D
from get_name import get_human_names, get_age
from extract_details import extract_details

def extract(text):
    name = " ".join(get_human_names(text))
    age = get_age(text)
    date = str(D.today())

    details = extract_details(text)
    
    tablet = []

    i = 0
    while i < len(details):
        

        while i < len(details) and details[i][1] == "DRUG":
            temp = ["", "", ""]
            temp[0] = details[i][0]
            i += 1

            while i < len(details) and details[i][1] != "DRUG":
                if details[i][1] == "STRENGTH" or details[i][1] == "DOSAGE":
                    temp[1] += details[i][0] + " "

                if details[i][1] == "DURATION" or details[i][1] == "FREQUENCY":
                    temp[2] += details[i][0] + " "
                
                i += 1
            tablet.append(temp)
        i += 1
                
        



    return name, age, date, tablet

if __name__ == "__main__":
    print(extract("Patient name is Ram age 19 tablet azithromycin 500mg 3days after food morning only syrup robitussin 5ml 5days before food thrice a day."))
