#####################coding=utf-8######################################
####################### 图片编码 #######################################
####################### created by tengxing on 2017.3 #################
tensorflow 似乎不去关心如何卷积和池化操作,关心最后喂给的数据,所以我们可以提前处理好数据,比如
之前就对图像进行卷积和赤化,用的时候直接读取就行。
