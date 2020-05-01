import codecs
from tokenize import String

import xlrd
from xlrd.timemachine import xrange

from stemmer import Stemmer
from string import punctuation

if __name__ == '__main__':
    mistag_indexes = []
    right_tags = []
    inputfile= "auto.txt"
    testfile="manual.txt"
    outputfile="accuracy.txt"
    mistags=0
    a=True
    my_words=[]
    tags= ["/IS.;","/SIF.;","/F.;","/ƏVƏZ.;","/ƏD.;","/MODAL","/ZƏRF.;","/SAY.;","/QOŞ.;","/HISSƏCIK","/BAĞL.;","/NIDA","/.","/,","/:","/-","/–" ]

    with open(inputfile, encoding="utf-8-sig") as file:
        auto = file.read().split()

    with open(testfile, encoding="utf-8-sig") as file:
        manual = file.read().split()

    if len(manual) != len(auto):
        print('Documents do not match')
        a=False
    else:
        for i in range(0, len(manual)):
            f = manual[i].find('/')
            if manual[i][:f] != auto[i][:f]:
                print('Documents do not match')
                a=False
                break
            elif manual[i][f:] != auto[i][f:]:
                mistags += 1
                mistag_indexes.append(i)
                xx = manual[i][::-1]
              #  xx = xx[xx.find(';'):][::-1]
                print(xx)
                right_tags.append(xx[f:])
        result=100-100*mistags/len(manual)
        mistag_indexes.insert(0, result)
        print(mistags,'/',len(manual))
        print('Accuracy is ', result)

if a==False:
      fout = codecs.open(outputfile, mode='w', encoding="utf-8")
      fout.write("Documents do not match")
else :
      result1 = str(result)
      fout = codecs.open(outputfile, mode='w', encoding="utf-8")
      fout.write(result1)
