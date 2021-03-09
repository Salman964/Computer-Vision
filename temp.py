import imageio as io
import numpy as np
import matplotlib.pyplot as plt

im=io.imread('salman.jpeg')
   
r,c1,c2=im.shape

new_img=np.zeros((r,c1),dtype=np.uint8);

j=0
k=0
m=0


sum=0;
for j in range(r):    
    for k in range(c1):
        for m in range(c2):
            if(m==0):
                sum=sum+im[j,k,m]*0.3;
            elif(m==1):
                sum=sum+im[j,k,m]*0.59; 
            elif(m==2):
                sum=sum+im[j,k,m]*0.11;
            
            
        new_img[j,k]=sum;
        sum=0
              
           
plt.imshow(new_img,cmap='gray')
plt.show()
plt.close()
    


print("hello")
