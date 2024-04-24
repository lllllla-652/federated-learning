import numpy as np

idxs_labels = np.array([
    [0, 1, 2, 3, 4, 5],  # 图片索引
    [2, 0, 3, 1, 4, 7]   # 图片标签
])
print(idxs_labels[1:])

idxs_labels_sorted = idxs_labels[:, idxs_labels[1, :].argsort()]

b = idxs_labels[1, :].argsort()
print(b)
print(idxs_labels_sorted)

dict_users = {i: np.array([], dtype='int64') for i in range(10)}
print(dict_users)
idxs = idxs_labels_sorted[0,:]
for i in range(2):
    dict_users[i] = np.concatenate((dict_users[i], idxs[1*3:2*3]), axis=0)

print(dict_users)
