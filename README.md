# durhack
This is a code that handling to perform a better view in Durham County history online project.

## ./website
Run npm start in this folder. Run npm start to run the server. The website can then be accessed on http://127.0.0.1:8080/.
The simple website gives an illustration of the original and colourized&enhanced versions of images from the Durham County Council database.
An image, which is the main image, is displayed in the middle of the page, and four smaller images are displayed below it.
By clicking the button on the top, the main image is switched between the two versions. The four images at the bottom are semantically relavent to the main image. Clicking them, the user is brought to the webpage where that image is displayed as the main image.

## colourize.py
We use this to colourize black and white images by calling deepai api. The image is sent through the api and the url of the colourized version is returned. Note that the api has some restrictions in its license. see more details in the file.

## processing.py
This program was used to enlarge and sharpen images, as well as remove noises and adjust contrast of the images.

## nltk_class.py
This program was used to extract keywords for each image, compare the similarity of the keywords betweeen images and find 4 most related images to each image. The output of this program is a json file containing information of the images including filename, relative, title and description. 
