import nltk
import pandas as pd

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
                noun_list[-1] = noun_list[-1] + ' ' + tagged_example[i][0]
            else:
                noun_list.append(tagged_example[i][0])
        else:
            continue

    return noun_list


data = pd.read_excel(io=r'./pppmedia.xlsx')
dropped_data = data.drop_duplicates(subset=["comptitle"])
dropped_data = dropped_data.reset_index()
t = 0
photo_dict = {}
while t < dropped_data.shape[0]:
    caption = dropped_data.loc[t, "description"]
    keyword_list = get_label(str(caption))
    photo_dict[dropped_data.loc[t, "comptitle"]] = keyword_list
    t += 1
    print(t)

# print(photo_dict)

caption_list = []
caption_dict = {}

for picture in photo_dict:
    for key in photo_dict[picture]:
        # if key in caption_list:
        #     continue
        # else:
        #
        caption_list.append(key)


for key in caption_list:
    caption_dict[key] = caption_dict.get(key, 0) + 1

# print(caption_dict)

for key in caption_dict:
    if int(caption_dict[key]) > 50:
        print(key + ':' + str(caption_dict[key]))