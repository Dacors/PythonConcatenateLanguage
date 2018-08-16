import re
alphabet = open("Alphabet1.txt")
alphabet1 = open("Alphabet2.txt")
content = alphabet.read()
content1 = alphabet1.read()
result = []


def concat_alphabets(alphabet,alphabet1):
    caracters = re.findall(r"[\w']+", alphabet)
    caracters1 = re.findall(r"[\w']+", alphabet1)

    for i in range(1,len(caracters)):
        for b in range(1,len(caracters1)):
            caracter = caracters[i] + caracters1[b]
            if caracter in result:
                result
            else:                
                result.append(caracter)

    return result

print(concat_alphabets(content,content1))