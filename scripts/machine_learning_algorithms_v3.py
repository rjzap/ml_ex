from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
import csv
import numpy as np
import pandas as pd

#uncomment to visually confirm input data
#pd.read_csv('C:\Users\zappari\Desktop\ML ex\LoanStats3a_20170620_v12.csv')

#define input file as dataframe
df = pd.read_csv('C:\Users\zappari\Desktop\ML ex\LoanStats3a_20170620_v12.csv')
