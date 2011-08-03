import opencv
from opencv import highgui
import Image
import time

# Video Device number /dev/videoX
videodevice = 1

def snapshot():
    cam = highgui.cvCreateCameraCapture(1)
    img = highgui.cvQueryFrame(cam)

    pilImage = opencv.adaptors.Ipl2PIL(img)

    highgui.cvReleaseCapture(cam)
    
    return pilImage

def save_image(image, filename=None):
    if filename:
        image.save(filename)
    else:
        filename = str(time.time()) + ".jpg"
        image.save(filename)
