'''
@Author: rishi
'''

from datetime import date as D
# TODO: change this file using nlp

def extract(text):
    text = text.lower()
    str = text.split(" ")
    val = "mg"
    for i in range(str.count(val)):
        str.remove(val)
    val = "milligram"
    for i in range(str.count(val)):
        str.remove(val)
    val = "days"
    for i in range(str.count(val)):
        str.remove(val)
    val = "ml"
    for i in range(str.count(val)):
        str.remove(val)
    val = "for"
    for i in range(str.count(val)):
        str.remove(val)

    name = ""
    age = ""
    date = D.today()
    tablet = []
    syrup = []
    for i in range(len(str)):
        if (str[i] == 'name'):
            name = str[i + 2]
        if (str[i] == 'i' and str[i + 1] == 'am'):
            name = str[i + 2]
        if (str[i] == "i'm"):
            name = str[i + 2]
        if (str[i] == 'name' and str[i + 3] != 'age'):
            name += str[i + 3]
        if (str[i] == 'age'):
            age = str[i + 1]
        if (str[i] == 'tablet'):
            ar = []
            default = "0-0-0"
            ar.append(str[i + 1])
            if (str[i + 2].find("mg") >= 0):
                str[i + 2] = str[i + 2][:-2]

            ar.append(str[i + 2])

            if (str[i + 3].find("days") >= 0):
                str[i + 3] = str[i + 3][:-4]

            ar.append(str[i + 3])

            if (str[i + 4] == 'before'):
                ar.append(str[i + 4])
            else:
                ar.append("After")
            for j in range(5):
                if (str[i + j + 3] == 'once'):
                    default = '1' + '-' + default[2] + '-' + default[4]
                    break
                if (str[i + j + 3] == 'twice'):
                    default = '1' + '-' + default[2] + '-' + '1'
                    break
                if (str[i + j + 3] == 'thrice' or str[i + j + 3] == 'prices' or str[i + j + 3] == 'rice'):
                    default = '1' + '-' + '1' + '-' + '1'
                    break
                if (str[i + j + 3] == 'night'):
                    default = default[0] + '-' + default[2] + '-' + '1'
                if (str[i + j + 3] == 'afternoon'):
                    default = default[0] + '-' + '1' + '-' + default[4]
                if (str[i + j + 3] == 'morning'):
                    default = '1' + '-' + default[2] + '-' + default[4]
                if (str[i + j + 3] == 'done' or str[i + j + 3] == 'dun'):
                    break

            ar.append(default)
            tablet.append(ar)
        if (str[i] == 'syrup'):
            arr = []
            default = "0-0-0"
            arr.append(str[i + 1])

            if (str[i + 2].find("ml") >= 0):
                str[i + 2] = str[i + 2][:-2]

            arr.append(str[i + 2])

            if (str[i + 3].find("days") >= 0):
                str[i + 3] = str[i + 3][:-4]

            arr.append(str[i + 3])

            if (str[i + 4] == 'before'):
                arr.append(str[i + 4])
            else:
                arr.append("After")
            for j in range(8):
                if (str[i + j + 3] == 'once'):
                    default = '1' + '-' + default[2] + '-' + default[4]
                    break
                if (str[i + j + 3] == 'twice'):
                    default = '1' + '-' + default[2] + '-' + '1'
                    break
                if (str[i + j + 3] == 'thrice' or str[i + j + 3] == 'prices'):
                    default = '1' + '-' + '1' + '-' + '1'
                    break
                if (str[i + j + 3] == 'night'):
                    default = default[0] + '-' + default[2] + '-' + '1'
                if (str[i + j + 3] == 'afternoon'):
                    default = default[0] + '-' + '1' + '-' + default[4]

                if (str[i + j + 3] == 'morning'):
                    default = '1' + '-' + default[2] + '-' + default[4]
                if (str[i + j + 3] == 'done' or str[i + j + 3] == 'dun'):
                    break

            arr.append(default)
            syrup.append(arr)

    return name, age, date, tablet, syrup

if __name__ == "__main__":
    print(extract("Patient name is ram age 19 tablet azithromycin 500mg 3days after food morning only syrup robitussin 5ml 5days before food thrice a day."))