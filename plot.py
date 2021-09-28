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


#キーワード読み込み
key = []
with open('keyword.csv', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        key.append(row[0])


#disk書き込み
fig, ax = plt.subplots(figsize=(7,7))
c = patches.Circle( xy=(0,0), radius=1, fill = False)
ax.add_patch(c)

#モデルロード
model = PoincareModel.load('p150.model')


data = []
annotations = []
cnt = 0
data.append([0,0])
cnd = data[0]
annotations.append('新型コロナウイルス感染症')

dip = 0
notdip = 0
for i in key:
    if(i != '新型コロナウイルス感染症'):
        try: 
            tmp = [model.kv[i][0],model.kv[i][1]]
            tmp[0] -= cnd[0]
            tmp[1] -= cnd[1]
            data.append(tmp)
            annotations.append(i)
            dip += 1
        except KeyError as e:
            #print(i)
            notdip += 1

print("fin")
print(dip)
print(len(data))
print(notdip)
#print(data)

x, y = zip(*data)
plt.xlim(-1.0, 1.0)
plt.ylim(-1.0, 1.0)

plt.scatter(x, y, s=15, alpha=0.3)

for i, label in enumerate(annotations):
    plt.annotate(label, (x[i], y[i]), fontsize=7,  fontname="MS Gothic")

plt.show()

