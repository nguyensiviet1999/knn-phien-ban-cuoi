import os
import numpy as np
import re
import pickle
import pandas as pd
from math import sqrt
from random import randrange

dir_path = os.path.dirname(os.path.realpath(os.getcwd()))
dir_path = os.path.join(dir_path, 'Data')

def get_data(folder_path):
    X = []
    y = []
    dirs = os.listdir(folder_path)
    for path in dirs:
        file_paths = os.listdir(os.path.join(folder_path, path))
        for file_path in file_paths:
            with open(os.path.join(folder_path, path, file_path), 'r', encoding="utf-16") as f:
                lines = f.readlines()
                lines = ' '.join(lines)
                lines = lines.lower()
                lines = re.sub(r"[^\w\d\s]"," ",lines,flags=re.UNICODE)
                lines = re.sub("[0-9]"," ",lines,flags=re.UNICODE)
                lines = lines.split()
                lines = ' '.join(lines)
                X.append(lines)
                y.append(path)
    return X, y
# train_path = ('new train - Copy (3)')
# X_data, y_data = get_data(train_path)
# pickle.dump(X_data, open('X_data.pkl', 'wb'))
# pickle.dump(y_data, open('y_data.pkl', 'wb'))

# test_path = os.path.join('new test - Copy (3)')
# X_test, y_test = get_data(test_path)

# pickle.dump(X_test, open('X_test.pkl', 'wb'))
# pickle.dump(y_test, open('y_test.pkl', 'wb'))
