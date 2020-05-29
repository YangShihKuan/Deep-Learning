# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:33:52 2020

@author: Hsun Jung Chen
"""

import numpy as np
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from PIL import Image
# 神經網路 _分類問題 _回歸問題
# 分類問題 - softmax
# 回歸問題 - 恆等

def softmax(a):
    c = np.max(a)
    adjust_a = a - c
    exp_a = np.exp(adjust_a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a
    
    return y

# softmax 機率

#%%

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

img = x_train[0]
label = t_train[0]

print(label)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)





