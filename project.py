#!/usr/bin/env python
import cv2
import numpy as np
import sys
from skimage import io

def project(angle, img):
    
    height, width, _ = img.shape
    pts_src = np.array([[0,0],
                        [width- 1, 0],
                        [width - 1, height -1],
                        [0, height - 1 ]],dtype=float);

    added_height = int(width*np.sin(angle * np.pi / 180.))
    new_width = int(width*np.cos(angle * np.pi / 180.))

    pts_dst = np.array([[0,0],
                        [new_width-1,-1-added_height],
                        [new_width-1,height-1-added_height],
                        [0, height-1]],dtype=float);
    pts_dst += np.array([[0,added_height-1]])

    projected_img = 255*np.ones((height+added_height,new_width,3), dtype=np.uint8)
    cv2.fillConvexPoly(projected_img, pts_dst.astype(int), 0, 16);

    h, _ = cv2.findHomography(pts_src, pts_dst);
    im_temp = cv2.warpPerspective(img, h, (projected_img.shape[1],projected_img.shape[0]))

    projected_img += im_temp;
    return projected_img

if __name__ == '__main__':
    angle = float(sys.argv[1])
    img_filepath = sys.argv[2]
    out_filepath = sys.argv[3]

    img = io.imread(img_filepath)
    io.imsave(out_filepath, project(angle, img))