import numpy as np 
import cv2
#import cv2


image= cv2.imread(r'C:\Users\DELL\Desktop\data science DWIT\practice\img.png')
original_image= image

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges= cv2.Canny(gray, 50,200)

img_gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(img_gray2, 150, 255, cv2.THRESH_BINARY)


contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

def get_contour_areas(contours):

    all_areas= []

    for cnt in contours:
        area= cv2.contourArea(cnt)
        all_areas.append(area)

    return all_areas


sorted_contours= sorted(contours, key=cv2.contourArea, reverse= False)

font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(0,4):
  smallest_item= sorted_contours[i]
  x=smallest_item[-1][0][0]
  y=smallest_item[-1][0][1]+78
  cv2.putText(original_image, str(i+1), (x,y),font, 1, (0, 255, 0), 2, cv2.LINE_AA)


cv2.waitKey(0)
cv2.imshow("og",original_image)


cv2.waitKey(0)
cv2.destroyAllWindows()