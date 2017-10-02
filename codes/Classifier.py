import CsvReader


# def set_training_data(feedbackinfo_list):
#     train_data = []
#     for i in range(len(feedbackinfo_list)):
#         tokens = nltk.word_tokenize(feedbackinfo_list[i].description)
#         tagged = nltk.pos_tag(tokens)
#         data = [dict(tagged), feedbackinfo_list[i].category]
#         train_data.append(data)
#     return train_data
#
#
# def set_test_data(feedbackinfo_list):
#     test_data = []
#     for i in range(len(feedbackinfo_list)):
#         tokens = nltk.word_tokenize(feedbackinfo_list[i].description)
#         tagged = nltk.pos_tag(tokens)
#         data = [dict(tagged)]
#         test_data += data
#
#     return test_data
#
#
# def nb_classify(trian_data, test_data):
#     classifier = nltk.classify.NaiveBayesClassifier.train(trian_data)
#
#     print sorted(classifier.labels())
#     classified_data = classifier.classify_many(test_data)
#     for data in classified_data:
#         print data

def set_training_data(feedbackinfo_list):
    train_data = []
    for feedbackinfo in feedbackinfo_list:
        if feedbackinfo.company == '':
            data = ['others', feedbackinfo.category, feedbackinfo.des_type]
            train_data.append(data)
        else:
            data = [feedbackinfo.company, feedbackinfo.category, feedbackinfo.des_type]
            train_data.append(data)

    return train_data


def get_prob(data):

    # Get the categories count for each company (e.g. [company: [feedback = 5] [complain = 2]])
    company_and_cat = {}
    for data_list in data:

        if not data_list[0] in company_and_cat:
            company_and_cat[data_list[0]] = [[data_list[1], 1]]
        else:
            item = company_and_cat[data_list[0]]
            contains = False

            for i in range(len(item)):
                if item[i][0] == data_list[1]:
                    item[i][1] += 1
                    company_and_cat[data_list[0]] = item
                    contains = True
                    break
                else:
                    contains = False

            if not contains:
                company_and_cat[data_list[0]].append([data_list[1], 1])
    prob = {}
    for cat in company_and_cat:
        cat_list = []
        counter = {}
        # Get the number of categories order group
        for i in range(len(data)):
            if data[i][0] == cat:
                cat_list.append([data[i][1], data[i][2]])

        for i in range(len(cat_list)):
            if not cat_list[i][0] in counter:
                counter[cat_list[i][0]] = [[cat_list[i][1], 1]]
            else:

                item = counter[cat_list[i][0]]
                contains = False
                for u in range(len(item)):
                    if item[u][0] == cat_list[i][1]:
                        item[u][1] += 1
                        counter[cat_list[i][0]] = item
                        contains = True
                        break
                    else:
                        contains = False

                if not contains:
                    counter[cat_list[i][0]].append([cat_list[i][1], 1])

        # Calculate the probabilities
        for c in counter:
            for cl in company_and_cat[cat]:
                if cl[0] == c:
                    for c_list in counter[c]:
                        c_list[1] = float(c_list[1]) / cl[1]

        prob[cat] = [counter]
    return prob


def get_com_feedback_prob(prob, cname, cat):
    prob_list = prob[cname]
    for pl in prob_list:
        return pl[cat]



feedbackinfo_list = CsvReader.read_file()
train_data = set_training_data(feedbackinfo_list)
prob = get_prob(train_data)
print get_com_feedback_prob(prob, 'CUSHMAN & WAKEFIELD (S) PTE LTD', 'Feedback')





