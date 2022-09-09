import numpy as np
import seaborn
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# df = pd.read_csv ('heatmap_move.csv')
# # df = pd.read_csv('move.csv')
# print(df)

heat_move = []

with open('heatmap_move.csv') as csvdatei:
    reader = csv.reader(csvdatei, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
    for row in reader:
        heat_move.append(row)

print(np.shape(heat_move))
print(type(heat_move))


heat_move = np.array(heat_move, dtype='float')

print(heat_move[200,0])
print(type(heat_move[200,0]))
print(type(heat_move))

fig = plt.imshow(heat_move)
plt.show()

# print(type(heat_move))
# print(np.shape(heat_move))

# fig, ax = plt.subplots()
# im = ax.imshow(heat_move)

# ax.set_xticks(np.arange(len(heat_move[:,0])), labels="x_Werte")
# ax.set_yticks(np.arange(len(heat_move[0,:])), labels="y_Werte")

# for i in range(len(heat_move[:,0])):
#     for j in range(len(heat_move[0,:])):
#         text = ax.text(j, i, heat_move[i, j],
#                        ha="center", va="center", color="w")


# fig.tight_layout()
# plt.show()

# for row in csv_reader_object:
    #print(row)
    

# seaborn.heatmap(heat_move)

# plt.imshow(heat_move, cmap='hot', interpolation='nearest')
# plt.show()


#DURCHARBEITEN
#https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html