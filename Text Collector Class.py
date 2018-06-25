import copy
import os
from collections import Counter
import numpy as np
import en

class TextCollect(object):
    def __init__(self, textfile):
        self.data = copy.deepcopy(textfile)

