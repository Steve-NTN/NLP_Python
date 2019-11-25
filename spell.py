#!/usr/bin/python

# -*- coding: utf8 -*-
################ Spelling Corrector 
ASCII_REPLS = {u"[àảãáạăằẳẵắặâầẩẫấậ]": "a", u"[ÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬ]": "A",
               u"đ": "d",                   u"Đ": "D",
               u"[èẻẽéẹêềểễếệ]": "e",       u"[ÈẺẼÉẸÊỀỂỄẾỆ]": "E",
               u"[ìỉĩíị]": "i",             u"[ÌỈĨÍỊ]": "I",
               u"[òỏõóọôồổỗốộơờởỡớợ]": "o", u"[ÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢ]": "O",
               u"[ùủũúụưừửữứự]": "u",       u"[ÙỦŨÚỤƯỪỬỮỨỰ]": "U",
               u"[ỳỷỹýỵ]": "y",             u"[ỲỶỸÝỴ]": "Y"}
VIET_REPLS = {u"[àảãáạ]": u"a",     u"[ÀẢÃÁẠ]": u"A",
              u"[ăằẳẵắặ]": u"ă",    u"[ĂẰẲẴẮẶ]": u"Ă",
              u"[âầẩẫấậ]": u"â",    u"[ÂẦẨẪẤẬ]": u"Â",
              u"[èẻẽéẹ]": u"e",     u"[ÈẺẼÉẸ]": u"E",
              u"[êềểễếệ]": u"ê",    u"[ÊỀỂỄẾỆ]": u"Ê",
              u"[ìỉĩíị]": u"i",     u"[ÌỈĨÍỊ]": u"I",
              u"[òỏõóọ]": u"o",     u"[ÒỎÕÓỌ]": u"O",
              u"[ôồổỗốộ]": u"ô",    u"[ÔỒỔỖỐỘ]": u"Ô",
              u"[ơờởỡớợ]": u"ơ",    u"[ƠỜỞỠỚỢ]": u"Ơ",
              u"[ùủũúụ]": u"u",     u"[ÙỦŨÚỤ]": u"U",
              u"[ưừửữứự]": u"ư",    u"[ƯỪỬỮỨỰ]": u"Ư",
              u"[ỳỷỹýỵ]": u"y",     u"[ỲỶỸÝỴ]": u"Y"}
import re
from collections import Counter

##Uni-Gram
def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big1.txt', encoding="utf8").read()))

def Pw(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

##Bi-Gram
def readBiGram(lines):
    arr = []
    f = open(lines, encoding="utf8")
    for i in f:
        arr.append(i.replace("\n", "").lower())
    return arr
    
Bi_GramCounter = Counter(readBiGram("big2.txt"))
Bi_Gram = readBiGram("big2.txt")

def Pw0w1(text):
    N = sum(Bi_GramCounter.values())
    return Bi_GramCounter[text] / N

def Pw1_w0(text):
    (w0, w1) = text.split(" ")
    if w0 in WORDS and w1 not in WORDS:
        w1 = max(candidates(w1), key=Pw0w1)
        return w1
    elif w1 in WORDS:
        return w1
    elif w0 not in WORDS and w1 not in WORDS:
        w1 = max(candidates(w1), key=Pw0w1)
        return w1
    else:
        return ""


def correctionBi_gram(text):
    text.strip()
    (w0, w1) = text.split(" ")
    Pmax = 0
    word = ""
    for bi_word in Bi_Gram:
        if bi_word.split(" ")[0] == w0:
            if Pw0w1(bi_word) > Pmax:
                Pmax = Pw0w1(bi_word)
                word = bi_word.split(" ")[1]
            
    if w1 not in WORDS:
        if word in candidates(w1):       
            return word
        else:
            return correction(w1)
    else:
        return w1

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=Pw)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = u'aàảãáạăằẳẵắặâầẩẫấậbcdđeèẻẽéẹêềểễếệfghiìỉĩíịklmnoòỏõóọôồổỗốộơờởỡớợpqrstuùủũúụưừửữứựvxyỳỷỹýỵ'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    arr = readTV(open("big4.txt", encoding="utf8"))
    addTV = []
    for i in arr:
        addTV.append(word.replace(i[0], i[1]))
      
    return set(addTV + deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

################ Test Code 
def unit_tests():
    assert correction('hăg') == 'hăng'              # insert
    assert correction('dạu') == 'dạo'           # replace 2
    assert correction('nhug') == 'nhung'               # replace
    assert correction('ưl') =='lư'                 # transpose + delete
    return 'unit_tests pass'


def spelltest(tests, verbose=False):
    "Run correction(wrong) on all (right, wrong) pairs; report results."
    import time
    start = time.clock()
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = correction(wrong)
        good += (w == right)
        if w != right:
            unknown += (right not in WORDS)
            if verbose:
                print('correction({}) => {} ({}); expected {} ({})'
                      .format(wrong, w, WORDS[w], right, WORDS[right]))
    dt = time.clock() - start
    print('{:.0%} of {} correct ({:.0%} unknown) at {:.0f} words per second '
          .format(good / n, n, unknown / n, n / dt))

def countLine(f):
    return sum(1 for line in f)

def Testset(lines):
    "Parse 'right: wrong1 wrong2' lines into [('right', 'wrong1'), ('right', 'wrong2')] pairs."
    import time
    start = time.clock()
    good, n = 0, 0
    for line in lines:
        if len(line) == 1:
            t = time.clock() - start
            print('{:.0%} correct of {} words at {:.0f}s'.format(good/n, n, t))
            exit()
        else:
            (right, wrongs) = (line.split(':'))
            for wrong in wrongs.split():
                w = correction(wrong)    
                good += (w == right)            
                n += 1
def correctionText(sentences):
    sentences.strip()
    a = sentences.lower().split(' ')
    if len(a) == 1:
        return correction(sentences)
    textRight = ""

    a[0] = correctionFirst(a)
    textRight += a[0] + " "
    for k in range(1, len(a)):
        textRight += correctionBi_gram(a[k-1] + " " + a[k]) + " "
        arr = textRight.split()
        a[k] = arr[len(arr)-1]
        
    return textRight

def correctionFirst(arrText):
    first = arrText[0]
    second = correction(arrText[1])
    Pmax = 0
    word = ""
    for bi_word in Bi_Gram:
        if bi_word.split(" ")[1] == second:
            if Pw0w1(bi_word) > Pmax:
                Pmax = Pw0w1(bi_word)
                word = bi_word.split(" ")[0]
    if first not in WORDS:
        if word in candidates(first):       
            return word
        else:
            return correction(first)
    else:
        return first


def readTV(lines):
    a = []
    for line in lines:
        if line == None:
            break
        else:
            (left, right) = line.split(':')
            a.append((left, right.replace("\n","")))
    return a
    #for i in a:
        #print(i[0], i[1])

def option():
    while True:
        print("Choose option you want to fix:\n1.Word\t2.Text\t3.Quit")
        num = input()
        if num == "1":
            while True:
                print("Press word...(P/s: press 0 to stop)")
                str = input()
                if str == "0": break
                print("Candidates of word:\n", candidates(str))
                #print("Words:\n", known(edits2(str)))
        elif num == "2":
            while True:
                print("Press text...(P/s: press 0 to stop)")
                str = input()
                if str == "0": break
                print(correctionText(str))
        elif num == "3":
            exit()
        else:
            print("Try again")


if __name__ == '__main__':
     
    #print(unit_tests())
    #Testset(open('data_text1.txt'))
    #option()
    print(correctionText("Emm ddax bỏa ttooi ddi thieejt roofi phhari hôg"))
    #print(correctionText("Thusy kieefu"))
    
    