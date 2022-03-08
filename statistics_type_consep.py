import os
import scipy.io as io
import numpy as np
import json


types_num = {}
for i in range(1, 8):
    types_num[i] = 0

labeles_path = 'E://NucleiSegmentation//Data//hovernet//consep//CoNSeP//Test//Labels'
labels = os.listdir(labeles_path)
for label in labels:
    mat = io.loadmat(labeles_path + '//' + label)
    type_map = mat['type_map']
    inst_map = mat['inst_map']
    values = np.unique(type_map)[1:]

    for value in values:
        binary_map = type_map == value
        type_inst_map = binary_map * inst_map
        type_num = len(np.unique(type_inst_map)[1:])
        types_num[value] += type_num

print(types_num)
with open('types_num.txt', 'w') as f:
    f.write(json.dumps(types_num))