import cv2 
poster=cv2.imread("C:/Users/OmSai/Downloads/PRO-104-Project-Image-main/PRO-104-Project-Image-main/solar-system.jpg")
print(poster)
poster = cv2.putText(poster, 'MERCURY', (100,200), cv2.FONT_HERSHEY_COMPLEX,0.5, (255,156,134), 2,)  
poster = cv2.putText(poster, 'VENUS', (189,250), cv2.FONT_HERSHEY_COMPLEX,0.5, (255,156,134), 2,)
poster = cv2.putText(poster, 'EARTH', (290,260), cv2.FONT_HERSHEY_COMPLEX,0.5, (255,156,134), 2,)  


                                       
                                                        
cv2.imshow("ll",poster)
cv2.waitKey(0)