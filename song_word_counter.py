from collections import Counter


def word_counter(func):
    def counter(*args, **kwargs):
        data = func(*args, **kwargs)    
        total_words = data.split()
        stopwords = ['y','Y','la','de','una','los', 'me', 'No', 'con', 'que']
        words = [word for word in total_words if word not in stopwords]
        wordcount = Counter(words)
        for w in wordcount.most_common(6):
            print(f"{w[0]}: {w[1]}")
    return counter

# @word_counter
# def text_reader():  
#     file = open("/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt", "rt")
#     data = file.read()
#     return data

@word_counter
def text_reader(url):  
    file = open(url, "rt")
    data = file.read()
    return data

url1 = "/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt"
url2 = "/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt"
url3 = "/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt"

text_reader(url2)

