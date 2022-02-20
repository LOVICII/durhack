import glob
import requests

# License
# Unless otherwise stated, DeepAI.org and/or it's licensors own the intellectual property rights for all material on DeepAI.org All intellectual property rights are reserved.
# You may view and/or print pages from https://DeepAI.org for your own personal use subject to restrictions set in these terms and conditions.
# You must not:
#   Republish material from https://DeepAI.org
#   Sell, rent or sub-license material from https://DeepAI.org
#   Reproduce, duplicate or copy material from https://DeepAI.org
# Redistribute content from DeepAI.org (unless content is specifically made for redistribution).

bnw_dir = "./bnw_imgs/"
coloured_dir = "./coloured_imgs/"

no_img = 898
for image in glob.glob(bnw_dir+"*.jpg"):
    print("uploading image {} ...".format(image))
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={
            'image': open(image, 'rb'),
        },
        headers={'api-key': 'ad923361-d91c-41aa-a120-431feba6110f'}
    )
    response = r.json()
    print("get response {}".format(response))
    result_url = response["output_url"]

    response = requests.get(result_url)
    result_filename = str(no_img) + ".jpg"
    file = open(coloured_dir+result_filename, "wb")
    file.write(response.content)
    file.close()

    no_img+=1
