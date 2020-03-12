#Haiku game!  A game which gets a word from user and creates a poem... how fun is that!
# Farzan Khoobchehr    Feb 16, 2020
import requests
import json
repeat = "yes"
print ("Hello, welcome to the predictive text Haiku generator!")
while repeat.lower() == "yes":   #user can repeat the game by typing "yes"    
    try: # try to generate a poem if not
        word = input("What would you like to see a Haiku about? ")
        url_1 = "https://api.datamuse.com/words?md=s&rel_trg=" + word   # URL that generates related words to the input word
        response_1 = requests.get(url_1)
        if response_1:  # check the connection with the API
            data_1 = json.loads(response_1.text)  #loading the data
            first_list = []  #we're creating these lists to store all the words that meet the syllables condition and then we get their first element which is the most relevant word
            for line in data_1:  #iterate through the data
                if line["numSyllables"] == 3:  #syllables condition
                    word_1 = line["word"]  #words that meet the syllables condition
                    first_list.append(word_1)  #making a list of all those words that meet the syllables condition
            term_1 = first_list[0]  #getting the first element of the list (which has the highest score --> most relevant)
        else:
            print("couldn't connect to Datamuse")
        url_2 = "https://api.datamuse.com/words?md=s&lc=" + term_1  #create the next URL with the first element of the previous list
        response_2 = requests.get(url_2)  # all the codes below will have a similar commenting...
        if response_2:
            data_2 = json.loads(response_2.text)
            second_list = []      
            for line in data_2:
                if line["numSyllables"] == 2:
                    word_2 = line["word"]
                    second_list.append(word_2)
            term_2 = second_list[0]
        else:
            print("Couldn't connect to Datamuse")

        url_3 = "https://api.datamuse.com/words?md=s&lc=" + term_2
        response_3 = requests.get(url_3)
        if response_3:
            data_3 = json.loads(response_3.text)
            third_list = []
            for line in data_3:
                if line["numSyllables"] == 3:
                    word_3 = line["word"]
                    third_list.append(word_3)
            term_3 = third_list[0]
        else:
            print("Couldn't connect to Datamuse")

        url_4 = "https://api.datamuse.com/words?md=s&lc=" + term_3
        response_4 = requests.get(url_4)
        if response_4:
            data_4 = json.loads(response_4.text)
            fourth_list = []
            for line in data_4:
                if line["numSyllables"] == 2:
                    word_4 = line["word"]
                    fourth_list.append(word_4)
            term_4 = fourth_list[0]
        else:
            print("couldn't connect to Datamuse")

        url_5 = "https://api.datamuse.com/words?md=s&lc=" + term_4 + "&rel_rhy=" + term_2
        response_5 = requests.get(url_5)
        if response_5:
            data_5 = json.loads(response_5.text)
            fifth_list = []
            for line in data_5:
                if line["numSyllables"] == 2:
                    word_5 = line["word"]
                    fifth_list.append(word_5)
            term_5 = fifth_list[0]
        else:
            print("Couldn't connect to datamuse")

        url_6 = "https://api.datamuse.com/words?md=s&lc=" + term_5
        response_6 = requests.get(url_6)
        if response_6:
            data_6 = json.loads(response_6.text)
            sixth_list = []
            for line in data_6:
                if line["numSyllables"] == 3:
                    word_6 = line["word"]
                    sixth_list.append(word_6)
            term_6 = sixth_list[0]
        else:
            print("Couldn't connect to Datamuse")

        url_7 = "https://api.datamuse.com/words?md=s&lc=" + term_6 + "&rel_rhy=" + term_2
        response_7 = requests.get(url_7)
        if response_7:
            data_7 = json.loads(response_7.text)
            seventh_list=[]
            for line in data_7:
                if line["numSyllables"] == 2:
                    word_7 = line["word"]
                    seventh_list.append(word_7)
            term_7 = seventh_list[1]
        else:
            print("couldn't connect to Datamuse")
        print()
        print(term_1, term_2)
        print(term_3, term_4, term_5)
        print(term_6, term_7)
        print()
    
    except: # if couldn't generate a poem (because it had difficulty with following the rules or list index out of range etc) print the next line
        print("we couldn't generate a poem!")
    repeat = input("Would you like to see another Haiku (yes/no)? ")


