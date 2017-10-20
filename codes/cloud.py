#Doneby: Chua Jun Hui 1700681
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Convert all the required text into a single string here
#and store them in word_string

#you can specify fonts, stopwords.txt, background color and other options
def gencloud(text):
    file = open('stopwords.txt', 'r')
    stopwords_str = file.read()
    stopwords_list = stopwords_str.split('\n')
    stopwords_set = set(stopwords_list)
    wordcloud = WordCloud(stopwords=stopwords_set,
                          background_color='white',
                          width=1200,
                          height=500
                          ).generate(text.lower())
    plt.imshow(wordcloud)
    plt.axis('off')
    return plt
