# TensorFlow 学习



## 安装

我使用window 10 python 3.7进行对TensorFlow的学习。

期间出现了几个大坑

1. TensorFlow对window的兼容性可能不是很好（官网上推荐用Linux或者Mac，虽然我有Linux deepin，但是总感觉用得别扭），如果直接用 pip install tensorflow 总是会有各种问题，最后我用Anaconda来安装TensorFlow，用anaconda的好处是它可以根据python的版本选择合适的TensorFlow版本 [这是anaconda的详细教程](https://www.jianshu.com/p/62f155eb6ac5)
2. 网速慢,使用国内conda镜像源

如果以后要重装TensorFlow的话,[就按照这个教程](https://blog.csdn.net/KID_yuan/article/details/88775254)



## 初期学习方法和目标

1. [官网教程](http://tensorfly.cn/tfdoc/tutorials/mnist_beginners.html),简单教程是中文版的,这些都是机器学习基础中的基础,要认真学
2. 在官网中文教程中有一些扩展链接,这些多为英文,可以当成英语阅读理解.
3. 然后是老师要求的[micro-courses](https://www.kaggle.com/learn/overview),这个看前六个
4. 根据上面六个micro-courses 写六篇学习笔记
5. 每三天汇报一次进度
6. 登录kaggle, 验证码无法显示



## 小任务: 猫狗识别

I think this assignment is not as simple as I thought. Here are several difficulties.

1. I have to find the data by myself. Though I find pictures of cats and dogs from the [kaggle website](https://www.kaggle.com/c/dogs-vs-cats) easily, I cannot download it since the speed of download is limited. In order to address this tricky problem, I tried several way and finally found a comparetively good measure: use kaggle api. Here is the [detail](https://www.jianshu.com/p/7da54c564c55) of this measure. In this way, I can at least download the complete data, even though it takes me a lot of time.
2. I just a beginner of tensorflow and deep learning to some extent, which means I do not know any model used frequently in deep learning and be familiar with programing this kind of things. Also I realized that the images of dogs and cats have color, which means I need to transform these colorful images to grey-scale images.

Based on the statements mentioned above, I think this assignment is too difficult to me.

Then, what's next? Should I stand still? Of course not! Here is the assignment I give to myself: learning tensorflow from the official tensorflow tutorials website.

[here is the official tensorflow tutorials website](https://tensorflow.google.cn/tutorials/quickstart/beginner). By learning tensorflow in this website, I found one very useful tool which helped me get some insight on tensorflow: google colab. First of all, I don't need to annoy installing all the environement such as installing editor, installing tensorflow extension, downloading the relative data. Therefore, this tool give me a huge convenience.



