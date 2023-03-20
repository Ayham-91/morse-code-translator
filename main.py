import csv

#reading csv file using csv.reader and making two dictionaries out of it
with open ("morse alphabet.csv",  newline='', encoding="utf-8") as morse_data:
    data=csv.reader(morse_data,delimiter=',')
    list_of_rows=[]
    word_to_morse={}
    morse_to_word={}
    for row in data:
       list_of_rows.append(row)
    for item in list_of_rows[1:]:
        word_to_morse[item[0]]=item[1]
        morse_to_word[item[1]]=item[0]


# defining two functions to do the work
def Morsetostring():
    user_input = (input("Enter the morse code you want to convert to string with a space between letters and '/' between words\n")).upper()
    user_code = user_input.split(" ")
    print(user_code)
    string=[]
    for code in user_code:
        if code == "/":
            string.append(" ")

        elif code in morse_to_word.keys():
            string.append(morse_to_word[code])
    result= "".join(string)
    print(result)



def Stringtomorse():
    user_input = (input("Enter the string you want to convert to morse code\n")).upper()
    user_words = user_input.split(" ")
    morse=[]
    for word in user_words:
        morse.append("/")
        for letter in word:
            if letter in word_to_morse.keys():
                morse.append(word_to_morse[letter])

    morse.pop(0)
    result = " ".join(morse)
    print(result)

#calling the functions by user imput
app_run=True
while app_run==True:
    user_input=input("Choose '1' for string to morse or '2' for morse to string or any thing else to quit\n")
    if user_input =="1":
        Stringtomorse()
    elif user_input == "2":
        Morsetostring()
    else:
        app_run=False

