import removebg
import cropper

startNum = 1
endNum = 7
foldername = "necklace"

def main():
    removebg.RemoveBG(startNum, endNum, foldername)
    cropper.Cropper(startNum, endNum, foldername)

if __name__ == '__main__':
    main()