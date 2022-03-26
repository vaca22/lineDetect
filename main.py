import cv2
import numpy as np


def rgb2hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g - b) / m) * 60
        else:
            h = ((g - b) / m) * 60 + 360
    elif mx == g:
        h = ((b - r) / m) * 60 + 120
    elif mx == b:
        h = ((r - g) / m) * 60 + 240
    if mx == 0:
        s = 0
    else:
        s = m / mx
    v = mx
    H = h / 2
    S = s * 255.0
    V = v * 255.0
    return H, S, V
import cv2
import numpy as np

def redFind(image):
    lower = np.array([168, 43, 46])
    upper = np.array([180, 255, 255])
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    openI = cv2.morphologyEx(mask,cv2.MORPH_OPEN,s,iterations=1)
    closeI = cv2.morphologyEx(openI,cv2.MORPH_CLOSE,s,iterations=1)
    contours, hierarchy = cv2.findContours(closeI, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        rect = cv2.minAreaRect(c)
        print("红色:", int((rect[0][1] + rect[1][1]/2)))

    cv2.imshow("aaa", closeI)
    cv2.waitKey(1000)

def purpleFind(image):
    lower = np.array([142, 43, 46])
    upper = np.array([147, 255, 255])
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    openI = cv2.morphologyEx(mask,cv2.MORPH_OPEN,s,iterations=1)
    closeI = cv2.morphologyEx(openI,cv2.MORPH_CLOSE,s,iterations=1)
    contours, hierarchy = cv2.findContours(closeI, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        rect = cv2.minAreaRect(c)
        print("紫色:", int((rect[0][1] + rect[1][1]/2)))

    cv2.imshow("aaa", closeI)
    cv2.waitKey(1000)

def blueFind(image):
    lower = np.array([102, 43, 46])
    upper = np.array([112, 255, 255])
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    openI = cv2.morphologyEx(mask,cv2.MORPH_OPEN,s,iterations=1)
    closeI = cv2.morphologyEx(openI,cv2.MORPH_CLOSE,s,iterations=1)
    contours, hierarchy = cv2.findContours(closeI, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        rect = cv2.minAreaRect(c)
        print("蓝色:", int((rect[0][1] + rect[1][1]/2)))

    cv2.imshow("aaa", closeI)
    cv2.waitKey(1000)

def yellowFind(image):
    lower = np.array([20, 43, 46])
    upper = np.array([25, 255, 255])
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    openI = cv2.morphologyEx(mask,cv2.MORPH_OPEN,s,iterations=1)
    closeI = cv2.morphologyEx(openI,cv2.MORPH_CLOSE,s,iterations=1)
    contours, hierarchy = cv2.findContours(closeI, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        rect = cv2.minAreaRect(c)
        print("黄色:", int((rect[0][1] + rect[1][1]/2)))

    cv2.imshow("aaa", closeI)
    cv2.waitKey(1000)

def orangeFind(image):
    lower = np.array([11, 43, 46])
    upper = np.array([15, 255, 255])
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
    openI = cv2.morphologyEx(mask,cv2.MORPH_OPEN,s,iterations=1)
    closeI = cv2.morphologyEx(openI,cv2.MORPH_CLOSE,s,iterations=1)
    contours, hierarchy = cv2.findContours(closeI, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        rect = cv2.minAreaRect(c)
        print("橙色:", int((rect[0][1] + rect[1][1]/2)))

    cv2.imshow("aaa", closeI)
    cv2.waitKey(1000)

def brownFind(image):
    lower = np.array([3, 43, 46])
    upper = np.array([8, 255, 255])
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    openI = cv2.morphologyEx(mask,cv2.MORPH_OPEN,s,iterations=1)
    closeI = cv2.morphologyEx(openI,cv2.MORPH_CLOSE,s,iterations=1)
    contours, hierarchy = cv2.findContours(closeI, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        rect = cv2.minAreaRect(c)
        print("棕色:", int((rect[0][1] + rect[1][1]/2)))

    cv2.imshow("aaa", closeI)
    cv2.waitKey(1000)



fk = cv2.imread('aa.jpg')
image = cv2.resize(fk, (500, 800))
purpleFind(image)
orangeFind(image)
yellowFind(image)
brownFind(image)
blueFind(image)
redFind(image)
cv2.waitKey()
