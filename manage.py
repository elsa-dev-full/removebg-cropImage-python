import removebg
import cropper
from os import walk
import pathlib

startNum =1
endNum = 3
foldername = ["earring", "necklace"]

def main():
    removebg.RemoveBG(startNum, endNum, foldername[1])
    cropper.Cropper(startNum, endNum, foldername[1])

if __name__ == '__main__':
    # main()
    dirpath = pathlib.Path(__file__).parent.absolute()
    mypath = str(dirpath) + '/assests/earring/'
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break
    print(f)