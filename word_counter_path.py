import sys
from collections import Counter


def word_counter(func):
    def counter(*args, **kwargs):
        data = func(*args, **kwargs)    
        total_words = data.split()
        stopwords = ['y','Y','la','de','una','los','me','No','con','que','el','un','es','en','Que','muy','al','a','él','le','quiere','A','da','faltan','Mas','bien','no']
        words = [word for word in total_words if word not in stopwords]
        wordcount = Counter(words)
        print('\n>>> TOP SIX WORDS IN THIS SONG <<<\n')
        for w in wordcount.most_common(6):
            print(f"{w[0]}: {w[1]}")
    return counter


@word_counter
def text_reader(url):  
    file = open(url, "rt")
    data = file.read()
    return data


try:
    text_reader(str(sys.argv[1]))
except:
    print('This program needs 2 arguments:\n1. python file name\n2. song file path')


