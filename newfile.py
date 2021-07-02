import cv2
import pytesseract   #Text recognisation

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
img = cv2.imread('edit.png')     #here image location should be in same folder and reads image   #load the image
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img)) #to get image_to_srting() press control and click left button on pytesseract

cv2.imshow('Result',img)
cv2.waitKey(0)

#file = open("attendance.csv","a") # Open the text file in append mode 
#text = pytesseract.image_to_string("3.JPG")   # Applying tesseract OCR on the cropped image 
#file.write(text)    # Appending the text into file 
#file.write("\n")    # Appending the text into file 
#file.close          # Close the file 


