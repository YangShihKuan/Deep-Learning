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

#print(x_train.shape)
#print(t_train.shape)
#print(x_test.shape)
#print(t_test.shape)

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

img = x_train[0]
label = t_train[0]

#print(label)

#print(img.shape)
img = img.reshape(28, 28)
#print(img.shape)

img_show(img)
import pickle
def sigmoid(x):
    return 1 / (1 + np.exp(-x)) 

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p= np.argmax(y) # 最も確率の高い要素のインデックスを取得
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))    