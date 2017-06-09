#!/usr/bin/python
import os
import sys
import cv2

def convert_anno(img_folder,anno_folder,label):
    if not os.path.exists(img_folder):
        print "img folder : {} does not exist.".format(img_folder)
        sys.exit()
    if not os.path.exists(anno_folder):
        print "img folder : {} does not exist.".format(anno_folder)
        sys.exit()

    anno_new_folder=anno_folder
    label_file = img_folder
    if label_file[-1] == '/':
        label_file = label_file[:-1]
    label_file += ".det_label"
    label_out=open(label_file,'w')
    imgs=os.listdir(img_folder)
    if len(imgs) > 0:
        for img in imgs:
            anno_file= anno_folder + "/gt_" + img[0:-4] + ".txt"
            anno_new_file = anno_new_folder + "/" + img[0:-4] + ".txt"
            if not os.path.exists(anno_file):
                print "img annoation file : {} does not exist.".format(anno_file)
                continue
            fout = open(anno_new_file,'w')
            with open(anno_file) as annof:
                for line in annof.readlines():
                    box=line.strip().split(',')
                    if len(box) < 4:
                        continue
                    fout.write("%s %s %s %s %s\n"%(label,box[0],box[1],box[2],box[3]))
            fout.close()
            label_out.write("%s %s\n"%(img_folder + "/" + img, anno_new_file))
        label_out.close()


if __name__ == "__main__":
    convert_anno(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
