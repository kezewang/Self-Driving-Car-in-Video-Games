import numpy as np
import cv2

path = 'C:\\Users\\kezew\\Dropbox\\work\\OnGoingProjects\\Self-Driving-Car-in-Video-Games\\vcla1007\\raw_data\\training_data30.npz'


data = np.load(path, allow_pickle=True)["arr_0"]

print(len(data))
dist_data = list()
count = 0
for data_i in data:#[:-1]:
    for data_i_j in data_i[:-1]:
        # print(data_i_j)
        cv2.imshow("data", data_i_j)
        cv2.waitKey(30)
    dist_data.append(data_i)
    print(count)
    count += 1

file_name = 'C:\\Users\\kezew\\Dropbox\\work\\OnGoingProjects\\Self-Driving-Car-in-Video-Games\\vcla1007\\raw_data\\filted_training_data30.npz'
np.savez(file_name, dist_data)