
- [Face Recognition](#face-recognition)
  - [week1](#week1)

## Face Recognition
  - gitee: https://gitee.com/anjiang2020_admin/famous-enterprises-fr20201226
### week1 
```
CV名企实战 :  遮挡人脸活体检测与人脸识别-课程导论
https://gitee.com/anjiang2020_admin/famous-enterprises-fr20201226 
Pipeline:
1. 人脸识别一般过程
2. 活体检测技术回顾
3. 数据集与评价办法
4. 人脸对比技术回顾
5. 课程建议与注意事项

作业：
   [必做]1. 完成人脸识别活体检测前的步骤：人脸检测+关键点提取程序。
    作业步骤：
         1 参考课上的代码示范例子:dlib_detect_recognize_display_show-master,完成代码famous-enterprises-fr20201226/week1/homework/week1_homework.py的填空。【第26行填空]使用检测模型对图片进行人脸检测，[第29行填空] 对检测到的人脸提取人脸关键点， #[第33行填空] 人脸对齐。
         2 完成后，从网站https://thispersondoesnotexist.com 上，下载一张人脸图片，对此图片存储为person_not_exist.jpg 
         3 运行作业代码，得到人脸检测和关键点的结果图片week1_detect_landmark.jpg，得到人脸对齐后的图片week1_align.jpg
    作业要求：
         1 提交内容：完成填空的代码；自己的person_not_exist.jpg 以及 自己运行代码，得到的结果图片：week1_detect_landmark.jpg 和 week1_align.jpg
         2 代码填写正确可运行。给出图片结果正确。
         本作业在week2课前讲解。
   [选做]2. 用opencv的检测模型，深度学习的检测模型替换dlib模型。
    建议步骤：
          1. 以关键字"cv2 人脸检测"为关键字，在搜索引擎上搜索相应内容。应该有很多相关文章以及代码可以参考。
          2. 以关键字“深度学习 人脸检测" 为关键字，在搜索引擎上搜索相应内容。
   [选做]3. 求y=x^2的最小值，用梯度下降的方法，不使用框架
          本作业在week2课前讲解。
   [选做]4. 用框架pytorch求出loss=(5*w_1+3w_2-1)^2+(-3*w1-4*w_2+1)^2的最小值，用梯度下降的方法.
          本作业在week2课前讲解。

   课程资料：
    人脸识别全流程示例代码：dlib_detect_recognize_display_show-master
    人脸识别综述：deepfacerecognition.pdf
    人脸关键点经典方法FPS3000：CVPR14_FaceAlignment.pdf
    活体检测算法2020年综述：https://zhuanlan.zhihu.com/p/114313640
    活体检测算法2019年综述：cvpr2019活体检测进展.pdf
    homework:待填空作业代码

```