import nltk
import pandas as pd
import json
import random


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


def get_label(caption):
    token_caption = nltk.word_tokenize(caption)
    tagged_example = nltk.pos_tag(token_caption)

    noun_list = []
    for i in range(0, len(tagged_example)):
        if tagged_example[i][0] == "Photograph" or tagged_example[i][0] == "Postcard":
            pass
        elif tagged_example[i][1] == "NN":
            noun_list.append(tagged_example[i][0])
        elif tagged_example[i][1] == "NNP":
            if tagged_example[i - 1][1] == "NNP" and len(noun_list) > 0:
                noun_list[-1] = noun_list[-1] + ' ' + tagged_example[i][0].lower()
            else:
                noun_list.append(tagged_example[i][0].lower())
        else:
            continue

    return noun_list


def get_keyword_dictionary(data):
    dropped_data = data.drop_duplicates(subset=["comptitle"])
    dropped_data = dropped_data.reset_index()
    t = 0
    photo_dict = {}
    while t < dropped_data.shape[0]:
        caption = dropped_data.loc[t, "description"]
        keyword_list = get_label(str(caption))
        photo_dict[dropped_data.loc[t, "comptitle"]] = keyword_list
        t += 1

    return photo_dict


def count_dictionary(keyword_dictionary):
    keyword_cloud_list = []
    caption_dict = {}

    for picture in keyword_dictionary:
        for key in keyword_dictionary[picture]:
            keyword_cloud_list.append(key)

    for key in keyword_cloud_list:
        caption_dict[key] = caption_dict.get(key, 0) + 1

    for key in caption_dict:
        if int(caption_dict[key]) > 10:
            print(key + ':' + str(caption_dict[key]))


def compare_similarity(list_1, list_2):
    return len(list(set(list_1).union(set(list_2))))


def get_keyword_cloud(photo_dictionary):
    keyword_cloud = {}
    for picture in photo_dictionary.keys():
        for keyword in photo_dictionary[picture]:
            if keyword in keyword_cloud.keys():
                keyword_cloud[keyword].append(picture)
            else:
                keyword_cloud[keyword] = [picture]
    return keyword_cloud


def get_most_relative(picture, keyword_cloud, photo_dictionary):
    picture_cloud = []
    for keyword in photo_dictionary[picture]:
        picture_cloud = picture_cloud + keyword_cloud[keyword]
    picture_cloud = list(set(picture_cloud))

    # print(picture_cloud)
    dict_sort = {}
    for relative_picture in picture_cloud:
        union = compare_similarity(photo_dictionary[picture], photo_dictionary[relative_picture])
        dict_sort[union] = relative_picture
    key_sort = sorted(dict_sort, reverse=True)

    relative_list = []
    for i in range(0, 4):
        try:
            relative_list.append(dict_sort[key_sort[i]])
        except IndexError:
            pass
        finally:
            pass
    return relative_list


data = pd.read_excel(io=r'./pppmedia.xlsx')
photo_dict = get_keyword_dictionary(data)
# count_dictionary(photo_dict)
keywords = get_keyword_cloud(photo_dict)
print("End initializing")

random.seed(114514)
for photo in photo_dict.keys():
    photo_dict[photo] = get_most_relative(photo, keywords, photo_dict)
    index = int(photo[4:])
    pre = photo[0:4]
    while len(photo_dict[photo]) < 4:
        photo_dict[photo].append(pre + str(random.randint(1, index)).zfill(4))

print("Tag is over")

# print(photo_dict)

########################################
dropped_data = data.drop_duplicates(subset=["comptitle"])
dropped_data = dropped_data.reset_index()

dataset_dict = {}
for key in dropped_data.loc[:, "comptitle"]:
    root_dict = {}
    info_dict = {}
    relative_dict = {}
    raw_data = dropped_data.loc[dropped_data['comptitle'] == key]
    raw_data = raw_data.reset_index()

    root_dict["filename"] = raw_data.loc[0, "mediaurl"]

    relative_dict["0"] = photo_dict[key][0]
    relative_dict["1"] = photo_dict[key][1]
    relative_dict["2"] = photo_dict[key][2]
    relative_dict["3"] = photo_dict[key][3]
    info_dict["relative"] = relative_dict

    info_dict["description"] = raw_data.loc[0, "description"]
    info_dict["title"] = raw_data.loc[0, "title"]
    info_dict["location"] = raw_data.loc[0, "settlementarea"]
    root_dict["info"] = info_dict

    dataset_dict[key] = root_dict


data = {"blac0001": {
    "filename": "blac0001_tcm4-17374.jpg",
    "info": {
        "relative": {
            "0": "sout0036",
            "1": 'hord0043',
            "2": 'seah0090',
            "3": 'seah0173'
        },
        "description": "Photograph showing three children standing in front of a blanket suspended behind them; on the left is a boy, aged approximately six years, wearing an open-necked shirt, a jacket, long socks and dark shoes; on the right is a girl, aged approximately nine years, wearing a dark blazer with a light border, a pleated skirt, socks and button shoes; in front of the other two is a child, aged approximately four years, wearing a light-coloured dress, socks and sandals; they have been identified as being in Blackhall",
        "title": "blac0001",
        "location": "Blackhall",
    }
}}


with open('data.json', 'w') as outfile:
    json.dump(dataset_dict, outfile)