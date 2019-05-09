# USAGE
# python fltest.py --shape-predictor shape_predictor_68_face_landmarks.dat --image example_01.jpg 

# Using Dlib & iBUG300-W dataset

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import math

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
   help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
   help="path to input image")
args = vars(ap.parse_args())

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# load the input image, resize it, and convert it to grayscale
image = cv2.imread(args["image"])
image = imutils.resize(image, width=300)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
rects = detector(gray, 1)

# loop over the face detections
for (i, rect) in enumerate(rects):
   # determine the facial landmarks for the face region, then
   # convert the facial landmark (x, y)-coordinates to a NumPy
   # array

   # by yumin 
   if i >= 1:
      print("Only one face can be detected")
      break

   shape = predictor(gray, rect)
   shape = face_utils.shape_to_np(shape)

   # convert dlib's rectangle to a OpenCV-style bounding box
   # [i.e., (x, y, w, h)], then draw the face bounding box
   (x, y, w, h) = face_utils.rect_to_bb(rect)
   
   # Print Rectangle 
   cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

   # show the face number
   cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
      cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

   # Print Rect Num
   print("Face #{}".format(i + 1))   

   # Point Number
   point = 0

   # loop over the (x, y)-coordinates for the facial landmarks
   # and draw them on the image
   for (x, y) in shape:
      cv2.putText(image, "{}".format(point), (x+2,y+2),
         cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 0, 255), 1)
      cv2.circle(image, (x, y), 2, (0, 255, 255), -1)

      
      # Print nose-facial line
      if point == 30:
         print("nose-facial line \n")
         temp = 0
         for temp in range(7):   
            cv2.line(image, (x, y), (shape[temp][0], shape[temp][1]), (255, 0, 0), 1)
            a = shape[temp][0]-x
            b = shape[temp][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.{}".format(temp),":",result)
            cv2.line(image, (x, y), (shape[16-temp][0], shape[16-temp][1]), (255, 0, 0), 1)
            a = shape[16-temp][0]-x
            b = shape[16-temp][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.{}".format(16-temp),":",result)
            print("\n")
         
         
      # Print nose-eyes
       # nose-front
      if point == 27:
            print("nose-front of eyes \n")
            cv2.line(image, (x, y), (shape[39][0], shape[39][1]), (255, 0, 0), 1)
            a = shape[39][0]-x
            b = shape[39][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.39 :",result)
            cv2.line(image, (x, y), (shape[42][0], shape[42][1]), (255, 0, 0), 1)
            a = shape[42][0]-x
            b = shape[42][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.42 :",result, "\n")

            cv2.line(image, (x, y), (shape[36][0], shape[36][1]), (255, 0, 0), 1)
            a = shape[36][0]-x
            b = shape[36][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.36 :",result)
            cv2.line(image, (x, y), (shape[45][0], shape[45][1]), (255, 0, 0), 1)
            a = shape[45][0]-x
            b = shape[45][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.45 :",result)

      if point == 28:
            print("nose-front of eyes \n")
            cv2.line(image, (x, y), (shape[39][0], shape[39][1]), (255, 0, 0), 1)
            a = shape[39][0]-x
            b = shape[39][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.39 :",result)
            cv2.line(image, (x, y), (shape[42][0], shape[42][1]), (255, 0, 0), 1)
            a = shape[42][0]-x
            b = shape[42][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.42 :",result, "\n")

            cv2.line(image, (x, y), (shape[36][0], shape[36][1]), (255, 0, 0), 1)
            a = shape[36][0]-x
            b = shape[36][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.36 :",result)
            cv2.line(image, (x, y), (shape[45][0], shape[45][1]), (255, 0, 0), 1)
            a = shape[45][0]-x
            b = shape[45][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.45 :",result)      
         
      if point == 29:
            print("nose-front of eyes \n")
            cv2.line(image, (x, y), (shape[39][0], shape[39][1]), (255, 0, 0), 1)
            a = shape[39][0]-x
            b = shape[39][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.39 :",result)
            cv2.line(image, (x, y), (shape[42][0], shape[42][1]), (255, 0, 0), 1)
            a = shape[42][0]-x
            b = shape[42][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.42 :",result, "\n")

            cv2.line(image, (x, y), (shape[36][0], shape[36][1]), (255, 0, 0), 1)
            a = shape[36][0]-x
            b = shape[36][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.36 :",result)
            cv2.line(image, (x, y), (shape[45][0], shape[45][1]), (255, 0, 0), 1)
            a = shape[45][0]-x
            b = shape[45][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.45 :",result)
      
      if point == 30:
            print("nose-front of eyes \n")
            cv2.line(image, (x, y), (shape[39][0], shape[39][1]), (255, 0, 0), 1)
            a = shape[39][0]-x
            b = shape[39][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.39 :",result)
            cv2.line(image, (x, y), (shape[42][0], shape[42][1]), (255, 0, 0), 1)
            a = shape[42][0]-x
            b = shape[42][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.42 :",result, "\n")

            cv2.line(image, (x, y), (shape[36][0], shape[36][1]), (255, 0, 0), 1)
            a = shape[36][0]-x
            b = shape[36][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.36 :",result)
            cv2.line(image, (x, y), (shape[45][0], shape[45][1]), (255, 0, 0), 1)
            a = shape[45][0]-x
            b = shape[45][1]-y
            result = math.sqrt((a*a)+(b*b))
            print("Distance between p.{}".format(point), "and p.45 :",result)

      # Print nose-lip     
      if point == 30:
         print("nose-lip \n")
         cv2.line(image, (x, y), (shape[48][0], shape[48][1]), (255, 0, 0), 1)
         a = shape[48][0]-x
         b = shape[48][1]-y
         result = math.sqrt((a*a)+(b*b))
         print("Distance between p.{}".format(point), "and p.48 :",result)
         cv2.line(image, (x, y), (shape[54][0], shape[54][1]), (255, 0, 0), 1)
         a = shape[54][0]-x
         b = shape[54][1]-y
         result = math.sqrt((a*a)+(b*b))
         print("Distance between p.{}".format(point), "and p.54 :",result)
         cv2.line(image, (x, y), (shape[50][0], shape[50][1]), (255, 0, 0), 1)
         a = shape[50][0]-x
         b = shape[50][1]-y
         result = math.sqrt((a*a)+(b*b))
         print("Distance between p.{}".format(point), "and p.50 :",result)
         cv2.line(image, (x, y), (shape[52][0], shape[52][1]), (255, 0, 0), 1)
         a = shape[52][0]-x
         b = shape[52][1]-y
         result = math.sqrt((a*a)+(b*b))
         print("Distance between p.{}".format(point), "and p.52 :",result)


      # print Point
     # print ("p.{}".format(point),(x,y))
      point = point + 1


# show the output image with the face detections + facial landmarks
cv2.imshow("Output", image)
cv2.waitKey(0)
