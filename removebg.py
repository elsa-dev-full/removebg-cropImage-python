import requests
from PIL import Image
import numpy as np
import os

def RemoveBG(start, end, foldername):
    # os.mkdir('results/' + foldername)
    # os.mkdir('results/' + foldername + '/removebg')
    # os.mkdir('results/' + foldername + '/cropped')
    for x in range(start, end + 1):
        PUBLIC_IMAGE_NAME = foldername + '-' + str(x)
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open('./assests/' + foldername + '/' + PUBLIC_IMAGE_NAME + '.jpg', 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'XKn6qPJaaCWyepNPMVmRCYtp'},
        )
        if response.status_code == requests.codes.ok:
            with open('results/' + foldername + '/removebg/' + PUBLIC_IMAGE_NAME + '-no-bg.png', 'wb') as out:
                out.write(response.content)    
            print("Successed to remove bg for " + foldername + "-" + str(x) + '.jpg in removebg.py')
        else:
            print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    RemoveBG(1, 1, "earring")