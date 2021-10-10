# ImgVideoProcessing.PY

## Overview:

Learning Python - Image and Video processing.

Original source code and documents from https://www.udemy.com/course/the-python-mega-course.

1. Image processing
2. Batch resize image
3. Face detecting in image
4. Video capturing with webcam and Face detecting in video
5. Motion detecting
6. Show motion detecting result with Bokeh



## Install OpenCV library on Windows 10

Please execute one of the commands below to do the installation depending on what version of Python you are using:

```
pip3.10 install opencv-python
```

or

```
pip3.9 install opencv-python
```

or

```
pip3.8 install opencv-python
```



### Check if opencv works

Open a Python session and try:

```
import cv2
```

If you get no errors, that means you installed OpenCV successfully. If you get an error, please see the FAQs below:

## **FAQs**

**1. My OpenCV installation didn't go well on Windows**

Solution:

1. Uninstall OpenCV with:

```
pip uninstall opencv-python
```

2. Download a wheel (.whl) file from [this link](http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv) and install it with pip. Make sure you download the correct file for your Windows version and your Python version. For example, for Python 3.6 on Windows 64-bit, you would do this:

```
pip install opencv_python‑3.2.0‑cp36‑cp36m‑win_amd64.whl
```

3. Then try to import cv2 in Python again. If there's still an error, then please type the following again in the command line:

`pip install opencv-python` 

4. Now, you should successfully import cv2 in Python.



**2. My OpenCV installation didn't go well on Mac**

Solution:

If pip install OpenCV-python didn't go well, please install OpenCV for Python 2 and use Python 2 to run the programs that contain cv2 code. Its' worth mentioning that Python 2 is installed by default on Mac, so no need to install Python 2. Here are the steps to correctly install OpenCV:

1. Install brew:

Open your terminal and execute the following:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2. OpenCV depends on GTK+, so please install that dependency first with brew (always from the terminal):

```
brew install gtk+
```

3. Install OpenCV with brew:

```
brew install opencv
```

4. Open Python 2 by typing:

```
python
```

5. Import cv2 in Python:

```
import cv2
```

If you get no errors, that means you installed OpenCV successfully.



**3. My OpenCV installation didn't go well on Linux**

1. Please open your terminal and execute the following commands one by one:

```
sudo apt-get install libqt4-devcmake -D WITH_QT=ON ..makesudo make install
```

2. If that doesn't work, please execute this:

```
sudo apt-get install libopencv-*
```

3. Then install OpenCV with pip:

```
pip install opencv-python
```

4. Import cv2 in Python. If you get no errors, that means you installed OpenCV successfully.



# References:

- https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
- https://dikshit18.medium.com/training-your-own-cascade-classifier-detector-opencv-9ea6055242c2
- https://docs.opencv.org/3.4.15/d7/d1b/group__imgproc__misc.html

