#coding=utf-8
#__author__ ="Charles.Xie" 
# Steps:
# 1.use csv to read file
# 2.parse traning data to 5652 pairs of (x,y)
# 3.training using gradient descent, adagrad
# 4.predict testing pm2.5
import csv
import numpy as np
from numpy.linalg import inv
import random
import math
import sys
