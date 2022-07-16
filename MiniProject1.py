#RGB  EXTRACTION - IT WILL EXTRACT ONE OF THE THREE COLORS AND GIVE ITS SHADE TO THE IMAGE

#10. Chess board
#RGB  EXTRACTION - IT WILL EXTRACT ONE OF THE THREE COLORS AND GIVE ITS SHADE TO THE IMAGE

#10. Chess board
import numpy as np
import cv2
img = np.zeros((64,64,3))
for i in range (0,8):
    if i%2 == 0:
        for j in range(0,8):
            if j%2 == 0:
                img[(8*i):(8*(i+1)),(8*j):(8*(j+1))] = 255,255,255
            else:
                img[(8*i):(8*(i+1)),(8*j):(8*(j+1))] = 0,0,0
    else:
        
        for j in range(0,8):
            
            if j%2 == 0:
                
                img[(8*i):(8*(i+1)),(8*j):(8*(j+1))] = 0,0,0
            else:
                img[(8*i):(8*(i+1)),(8*j):(8*(j+1))] = 255,255,255

            

cv2.imshow('MY FIRST CHESS BOARD',img)


cv2.waitKey(4000)
cv2.destroyAllWindows()
