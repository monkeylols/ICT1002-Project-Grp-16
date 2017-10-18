from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from os import path

#Convert all the required text into a single string here
#and store them in word_string

#you can specify fonts, stopwords, background color and other options
def gencloud(text):
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=500
                         ).generate(text)
    plt.imshow(wordcloud)
    plt.axis('off')
    return plt