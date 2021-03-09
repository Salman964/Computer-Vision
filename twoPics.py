import imageio
import numpy as np
import matplotlib.pyplot as plt

image1=imageio.imread("greySalman.png")
row1,col1,d3=image1.shape


newImage=np.zeros((row1,col1*2+15),dtype=np.uint8)
i=0
j=0


for i in range(row1):
    for j in range(col1):
        newImage[i,j]=image1[i,j,0]
        
        
i=0
for i in range(row1):
    for j in range(col1,col1+15):
        newImage[i,j]=0
         
        
image2=imageio.imread("greySalman.png")
row2,col2,d3=image2.shape
k=0
l=0
i=0
for i in range(row2):
    for j in range(col1+15,col1+15+col2):
        newImage[i,j]=image2[k,l,0]
        l=l+1
    l=0
    k=k+1
    
    

plt.imshow(newImage,cmap="gray")
plt.show()
plt.close()