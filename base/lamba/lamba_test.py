#! python3
# -- coding: utf-8 --

import numpy as np

block_vector = np.linspace(0,4,9)
print block_vector
test = 2.0
print(test)
normalize = lambda block_vector, magnitude: [element / magnitude for element in block_vector]
print(normalize(block_vector,test))
