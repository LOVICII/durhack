import glob
import requests

bnw_dir = "./bnw_imgs/"
coloured_dir = "./coloured_imgs/"

no_img = 0
for image in glob.glob(bnw_dir+"*.jpg"):
    print(image)
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={
            'image': open(image, 'rb'),
        },
        headers={'api-key': 'ad923361-d91c-41aa-a120-431feba6110f'}
    )
    response = r.json()
    print(response)
    result_url = response["output_url"]

    response = requests.get(result_url)
    result_filename = str(no_img) + ".jpg"
    file = open(coloured_dir+result_filename, "wb")
    file.write(response.content)
    file.close()

    no_img+=1