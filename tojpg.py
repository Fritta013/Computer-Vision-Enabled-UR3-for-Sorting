from glob import glob 
import cv2 
import os 
pngs= glob('darknet/pasta_data/pasta_images/*.jpeg')
for j in pngs: 
	print(j)
	img=cv2.imread(j)
	cv2.imwrite(j[:-4]+ 'jpg' , img) 
	os.remove(j)