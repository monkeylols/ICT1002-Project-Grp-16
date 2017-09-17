import nltk
import CsvReader


def set_training_data(feedbackinfo_list):
    train_data = []
    for i in range(len(feedbackinfo_list)):
        tokens = nltk.word_tokenize(feedbackinfo_list[i].description)
        #stop_token = removing_stopword(tokens)
        tagged = nltk.pos_tag(tokens)
        data = [dict(tagged), feedbackinfo_list[i].category]
        train_data.append(data)
    return train_data


def set_test_data(feedbackinfo_list):
    test_data = []
    for i in range(len(feedbackinfo_list)):
        tokens = nltk.word_tokenize(feedbackinfo_list[i].description)
        #stop_token = removing_stopword(tokens)
        tagged = nltk.pos_tag(tokens)
        data = [dict(tagged)]
        test_data += data

    return test_data


def nb_classify(trian_data, test_data):
    classifier = nltk.classify.NaiveBayesClassifier.train(trian_data)

    print sorted(classifier.labels())
    classified_data = classifier.classify_many(test_data)
    for data in classified_data:
        print data

    '''
    # getting probability
    catogries = []
    for i in range(len(train_data)):
        catogries.append(train_data[i][1])
    unique_cat = list(set(catogries))
    count = 0
    for data in classifier.prob_classify_many(test_data):

        for i in range(len(unique_cat)):
            print (unique_cat[i], ': %.4f' % data.prob(unique_cat[i])),
        print ''
        count += 1

    test_set = set_training_data(feedbackinfo_list[500:])
    print (nltk.classify.accuracy(classifier, test_set))
    print count
    '''

def removing_stopword(tokens):
    filename = 'stopwords.txt'
    stopword_file = open(filename, 'r')
    stopword_list = stopword_file.readlines()
    for i in range(len(tokens)):
        if tokens[i] in stopword_list:
            del tokens[i]
    return tokens



feedbackinfo_list = CsvReader.CsvReader().read_file()
train_data = set_training_data(feedbackinfo_list[:500])
test_data = set_test_data(feedbackinfo_list[500:])
nb_classify(train_data, test_data)





