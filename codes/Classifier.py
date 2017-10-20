# Done by: Foo Cher Zhi Adrian 1700550
import matplotlib.pyplot as plot


# Prepare the training data
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


# Get the probabilities of the type of order group for the categories
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
                        c_list[1] = (float(c_list[1]) / cl[1]) * 100

        prob[cat] = [counter]
    return prob


# The main function that returns a pie chart or an error message
def get_com_feedback_prob(feedbackinfo_list, cname, cat):

    # Get the required data
    train_data = set_training_data(feedbackinfo_list)

    # Get the probabilities from the set data
    prob = get_prob(train_data)

    if cname in prob:
        prob_list = prob[cname]
        labels = []
        sizes = []
        for pl in prob_list:
            if cat in pl:
                for items in pl[cat]:

                    labels.append(items[0])
                    sizes.append(round(items[1], 1))
            else:
                return 'Invalid order group selection'

        pie = plot.pie(sizes, shadow=True, autopct='%1.1f%%', pctdistance=1.2)
        plot.legend(pie[0], labels, loc="upper left", prop={'size': 6})
        plot.axis('equal')
        return plot
    else:
        return 'Invalid company name selection'






