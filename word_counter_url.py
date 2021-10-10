import urllib.request
from collections import Counter


def word_counter(func):
    def counter(*args, **kwargs):
        data = func(*args, **kwargs)    
        total_words = data.split()
        stopwords = ['y','Y','la','de','una','los', 'me', 'No', 'con', 'que']
        words = [word for word in total_words if word not in stopwords]
        wordcount = Counter(words)
        print('\n>>> TOP FIVE WORDS IN THIS SONG <<<\n')
        for w in wordcount.most_common(5):
            print(f"{w[0]}: {w[1]}")
    return counter


@word_counter
def text_reader(url):  
    data = urllib.request.urlopen(url).read().decode('utf_8') 
    return data



chilanga_banda = 'https://raw.githubusercontent.com/isabelyb/word_counter/main/chilanga_banda_lyrics.txt'
url2 = "/home/isa/estudio/Python/python_basic/09_professional_course/word_counter/chilanga_banda_lyrics.txt"
url3 = "/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt"

text_reader(chilanga_banda)

