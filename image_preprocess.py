import requests
from PIL import Image
import numpy as np


class preprcessInput:

    def __init__(self):
        self.o_width = None
        self.o_height = None
        self.o_image = None

        self.t_width = None
        self.t_height = None
        self.t_image = None

    def remove_bg(self, file_path:str, api_key='API_KEY', save_path='no-bg.png'):

        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(file_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': api_key},
        )

        pic = Image.open(file_path)
        self.o_width = np.asarray(pic).shape[1]
        self.o_height = np.asarray(pic).shape[0]
        try:
            self.o_channels = np.asarray(pic).shape[2]
        except Exception as e:
            print("Single channel image and error", e)

        if response.status_code == requests.codes.ok:
            with open(save_path, 'wb') as out:
                out.write(response.content)
        else:
            raise("Error:", response.status_code, response.text)

        self.o_image = Image.open('no-bg.png')
        # .convert('RGB')
        return np.asarray(self.o_image)

    def transform(self, width=768, height=1024, save_path='transformed_image.jpg'):
        newsize = (width, height)
        self.t_height = height
        self.t_width = width

        pic = self.o_image
        img = pic.resize(newsize)

        self.t_image = img

        background = Image.new("RGBA", newsize, (255, 255, 255, 255))
        background.paste(img, mask=img.split()[3])  # 3 is the alpha channel

        background.convert('RGB').save(save_path, 'JPEG')

        return np.asarray(background.convert('RGB'))


# USAGE OF THE CLASS
preprocess = preprcessInput()
op = preprocess.remove_bg('PATH')
arr = preprocess.transform(768, 1024)
