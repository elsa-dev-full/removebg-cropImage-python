import removebg
import cropper

startNum = 0
endNum = 45

def main():
    removebg.RemoveBG(startNum, endNum)
    cropper.Cropper(startNum, endNum)

if __name__ == '__main__':
    main()