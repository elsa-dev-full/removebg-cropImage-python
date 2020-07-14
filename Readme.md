## Guidence for this project

```bash
# python manage.py
In manage.py file, there are two parameters-startNum=0, endNum=45 which mean the range from 
img-0.jpg to img-45.jpg in assests folder. This will create removebg images and also cropped images 
which are matched with every image in assests folder.
The results will be in results folder-removebg, and cropped folders.
User can change parameter as he wants.
```

```bash
# python removebg.py
# if __name__ == '__main__':
#     RemoveBG(0,3)
This will remove background of images from img-0.jpg to img-3.jpg in assests folder, and will be saved in results/removebg folder as img-0-no-bg.png, img-1-no-bg.png, etc.
User can change parameter as he wants.
```

```bash
# python cropper.py
# if __name__ == '__main__':
#     Cropper(0,45)
This will crop images from img-0-no-bg.png to img-45-no-bg.png in results/removebg folder, and will be saved in results/cropped folder as img-0-no-bg-cropped.png, etc.
User can change parameter as he wants.
```
