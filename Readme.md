## Guidence for this project

```bash
Please make sure to run this command:
pip install -r requirements.txt
```

```bash
Structure for this project:
    __pycache__/
    assests/
        earring/
        necklace/
    results/
        earring/
            cropped/
            removebg/
        necklace/
            cropped/
            removebg/
    cropper.py
    manage.py
    Pipfile
    Pipfile.lock
    Readme.md
    removebg.py
```

```bash
# When you run this project like below
# python manage.py
In manage.py file, there are three parameters - startNum=1, endNum=3, foldername = ["earring", "necklace"]:
and run 'removebg.RemoveBG(startNum, endNum, foldername[1])' which mean the range from 
necklace-1.jpg to necklace-3.jpg in assests/necklace folder. This will create removebg images and also cropped images 
which are matched with every image in assests/necklace folder.
The results will be in results/necklace folder-removebg, and cropped folders.
User can change parameter as he wants.
```

```bash
# When you run this project like below
# python removebg.py
# if __name__ == '__main__':
#     RemoveBG(1, 20, "earring")
This will remove background of images from earring-1.jpg to earring-20.jpg in assests/earring folder, and will be saved in results/earring/removebg folder as earring-1-no-bg.png, etc.
User can change parameter as he wants.
```

```bash
# When you run this project like below
# python cropper.py
# if __name__ == '__main__':
#     Cropper(1, 20, "earring")
This will crop images from earring-1-no-bg.png to earring-20-no-bg.png in results/earring/removebg folder, and will be saved in results/earring/cropped folder as earring-1-no-bg-cropped.png, etc.
In case of the foldername == "necklace", the cropped image will be saved in results/necklace/cropped folder with the type of name necklace-1-no-bg-cropped-0-160.png, in which 0 means the x1 point of image, 160 means x2 point of image.
User can change parameter as he wants.
```
