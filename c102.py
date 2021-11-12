import cv2
import time
import random
import dropbox

startTime=time.time()

def takeSnapshot():

    randomNumber=random.randint(0,100)

    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imgName="img"+str(randomNumber)+".png"
        cv2.imwrite(imgName,frame)
        result=False
    
    return imgName
    print("snapshot is taken")
        
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFiles(imageName):
    accessToken="sl.A7pveekka7QqTscpRBPyUkMT2t9UrmsKeu2j7KXnrjoOq6Rv8kXQiKzTlYD__f5i11ta6YHvSzHkugMAWNkfJtKPyjJ9cUR5yQGgCIUO0Rd5LUZhZf5HC2GTh7n1lHdEOryJQiI"
    fileFrom=imageName
    Fileto="/newFolder/"+imageName
    dbx=dropbox.Dropbox(accessToken)

    with open(fileFrom,"rb") as f:
        dbx.files_upload(f.read(),Fileto,mode=dropbox.files.WriteMode.overwrite)
        print("File is uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=300):
            imageFileName=takeSnapshot()
            uploadFiles(imageFileName)

main()


