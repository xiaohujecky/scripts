#!/usr/bin/python
import os
import sys
import cv2

def draw_img_rects(img_name,box_file,save_name):
    img=cv2.imread(img_name)
    with open(box_file,'r') as f:
        lines=f.readlines()
        for line in lines:
            #box=line.strip().split(', ')
            #cv2.rectangle(img,(int(box[0]),int(box[1])),(int(box[2]),int(box[3])),(0,0,255),2)
            box=line.strip().split(' ')
            cv2.rectangle(img,(int(box[1]),int(box[2])),(int(box[3]),int(box[4])),(0,0,255),2)
        cv2.imwrite(save_name,img)


if __name__ == "__main__":
    draw_img_rects(sys.argv[1],sys.argv[2],sys.argv[3])
