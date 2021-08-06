import cv2
import matplotlib.pyplot as plt


def draw_mustache(filename):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    # Read the input image
    img = cv2.imread('static/uploads/'+filename)
    hat1 = cv2.imread('appfolio_hat.png',1)

    tmp = cv2.cvtColor(hat1, cv2.COLOR_BGR2GRAY) 
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)    
    b, g, r = cv2.split(hat1)
    rgba = [b,g,r, alpha]
    dst  = cv2.merge(rgba,4)
    cv2.imwrite("test.png", dst)
    temp = cv2.imread('test.png')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  
     # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        #cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0), 2)
        if (y - (h/12)) < 0:
            delta_y = 0
        else:
            delta_y =int (  y - (h/12))
        cv2.rectangle(img, (x, y), (x+w, delta_y), (0,0,0), -1)
        if (y - (h/3)) < 0:
            delta_y2 = 0
        else:
            delta_y2 =int( y - (h/3))
        cv2.rectangle(img, (x+20, y), (x+w-20, delta_y2), (0,0,0), -1)
        cv2.putText(img,'Appfolio', (x+int(.25 * w), delta_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA) 
   # Display the output
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(RGB_img,cmap=None,  interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    newfilename = "altered_" + filename
    plt.savefig('static/uploads/' + newfilename)
    return newfilename