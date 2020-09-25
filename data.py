import os
import sys
import pandas as pd
import numpy as np
import xml.etree.cElementTree as ET 

file_list = './DATA/nlptea14cfl_release1.1/nlptea14cfl_release1.1/Test/A2_CFL_test.sgml'
DOMTree = ET.ElementTree(file_list)
print(DOMTree.findall('SENTENCE'))