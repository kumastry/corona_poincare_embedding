from math import sqrt
from gensim.models.poincare import PoincareModel, PoincareRelations
#from gensim.viz.poincare import poincare_2d_visualization
from numpy import arccosh
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib import patches
from gensim.test.utils import datapath
import csv


print("1")
model = PoincareModel(PoincareRelations(file_path="./corona3.tsv", delimiter='\t'), size = 2, negative = 2)  #Change size for higher dims
print("2")
model.train(epochs=1)
print("3")
#print(model.kv.most_similar('新型コロナウイルス感染症', topn=300))

#save model
model.save("p3.model")
print("save")

