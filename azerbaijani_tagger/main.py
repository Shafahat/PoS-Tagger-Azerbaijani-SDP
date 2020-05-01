import codecs

import xlrd
from stemmer import Stemmer
from string import punctuation


def open_file(path):
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)
    a = {}
    for row_num in range(sheet.nrows):
        row_value = sheet.row_values(row_num)
        a [row_value[0]] = row_value[1]

    return a


# Program starts here.
if __name__ == '__main__':
    path = "obastan_final.xlsx"
    word_pos = open_file(path)
    output_file = "data.txt"
    # Instantiate Stemmer object
    my_stemmer = Stemmer()
    # Generate your text
    with open("stemtest.txt", 'r', encoding="utf-8-sig") as text:
        my_text = text.read()
    # Preprocess your text: remove punctuation, lowercase the letters, trim the spaces and newlines, and split the text by space/s
  #  my_text=my_text.replace("I", "İ")
    my_text=my_text.replace("“", "")
    my_text=my_text.replace("”", "")
    my_text=my_text.replace("'", "")
    my_text=my_text.replace('"', "")
    my_text=my_text.split()
    my_words=[]
    for word in my_text:
       newWord=""
       punct=""
       for char in word:
           if char in '!,?.:;':
               punct=char
               char=''
           newWord+=char
       if(newWord!=""):
            my_words.append(newWord)
       if (punct!=""):
             my_words.append(punct)
         #my_words.append(''.join(c for c in word if (c not in punctuation) or (c == '-')))
        # Print words before stemming
        # print(my_words)
        # Apply stemming to the list of words
    print(my_words)
    my_stemmed_words = my_stemmer.stem_words(my_words)
    # Print words after stemming
    print(my_stemmed_words)




    cnt=0
    fout = codecs.open(output_file, mode='w', encoding="utf-8")
    for index, word in enumerate(my_stemmed_words):
        pos = "NotDefined.;"
        word1=word
        if word1.__contains__('i') and not word1.__contains__('ı') :
           word1 = word1.upper()
           word1 = word1.replace("I", "İ")
          # print(word1)
        elif word1.__contains__('i') and word1.__contains__('ı'):
            word1 = word1.replace("i","w")
            word1 = word1.upper()
            word1 = word1.replace("W","İ")
        else:
            word1=word1.upper()
        if word1 in word_pos:
            pos = word_pos[word1]
       # print(my_words[index] + ' [ ' + pos + ' ]', end=' ')

        if pos=='.' or pos=='!' or pos=="?":
            fout.write(my_words[index] + '/' + pos.upper() + ' '+ "\n")
            cnt=cnt+1
        else:
            fout.write(my_words[index] + '/' + pos.upper() + ' ')

     #   print(my_words[index] + '/' + pos.upper() + ' ', end=' ' )
# print(cnt)

