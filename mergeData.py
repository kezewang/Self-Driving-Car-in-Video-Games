import numpy as np
import os
import pickle

folder_path = 'vcla1007/training_data/train_hdd'
filelist = os.listdir(folder_path)
data = None
for filename in filelist:
    path = os.path.join(folder_path, filename)
    if data is None:
       data = np.load(path, allow_pickle=True)["arr_0"]
    else:
       data_t = np.load(path, allow_pickle=True)["arr_0"]
       data = np.concatenate((data, data_t), axis=0)

dst_folder_path = 'vcla1007/training_data/train_ssd/'
print(data.shape)

for i in range(data.shape[0]):
    with open(os.path.join(dst_folder_path, str(i) + '.pkl'), 'wb') as fid:
         pickle.dump(data[i], fid, pickle. HIGHEST_PROTOCOL)

   
