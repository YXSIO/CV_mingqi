# coding:utf-8
import dlib
import numpy as np
from copy import deepcopy
import cv2
import os

#使用关键点模型需要提前下载此模型,并解压得到shape_predictor_68_face_landmarks.dat
#http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

if __name__=="__main__":
    # 初始化dlib的人脸检测模型
    detector = dlib.get_frontal_face_detector()
    # 初始化关键点检测模型
    predictor = dlib.shape_predictor(r'/Users/yuxiangzhang/Desktop/Kaikeba/名企课/CV_mingqi/Week_9/Homework/famous-enterprises-fr20201226/week1/homework/shape_predictor_68_face_landmarks.dat')
    # 从这个网站上，拿一张不存在的人脸图片：https://thispersondoesnotexist.com 
    # 保存为person_not_exist.jpg
    if 1:
        # 读取图片
        frame_src = cv2.imread("/Users/yuxiangzhang/Desktop/Kaikeba/名企课/CV_mingqi/Week_9/Homework/famous-enterprises-fr20201226/week1/homework/person_not_exist.jpeg")
        # 将图片缩小为原来大小的1/3
        x, y = frame_src.shape[0:2]
        # Downsample the size of the raw image
        frame = cv2.resize(frame_src, (int(y / 3), int(x / 3)))
        face_align = frame
        # [填空]使用检测模型对图片进行人脸检测
        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.
        dets = detector(face_align, 1)
        # 遍历检测结果
        for det in dets:
            #[填空] 对检测到的人脸提取人脸关键点
            shape=predictor(frame, det)
            # 在图片上绘制出检测模型得到的矩形框,框为绿色
            frame=cv2.rectangle(frame,(det.left(),det.top()),(det.right(),det.bottom()),(0,255,0),2)
            #[填空] 人脸对齐
            face_align=dlib.get_face_chip(frame, shape)
            # 将关键点绘制到人脸上，
            for i in range(68):
                cv2.putText(frame, str(i), (shape.part(i).x, shape.part(i).y), cv2.FONT_HERSHEY_DUPLEX, 0.3,(0, 255, 255), 1,cv2.LINE_AA)
                cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0, 0, 255))
        # 显示图片，图片上有矩形框，关键点
        cv2.imwrite("week1_result.jpg",cv2.resize(frame,(y,x)))
        cv2.imwrite("week1_align.jpg",cv2.resize(face_align,(y,x)))
       
        # 在对齐的图片上标注key points
        dets = detector(face_align, 1)
        if len(dets) == 1:
                # 关键点提取
            point68 = predictor(face_align, dets[0])
            for i in range(68):
                cv2.circle(face_align, (point68.part(i).x, point68.part(i).y), 1, (0, 0, 255))
            cv2.imwrite("week1_align.jpg",face_align)