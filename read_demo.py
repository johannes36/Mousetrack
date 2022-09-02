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

print(type(heat_move(1,1)))
print(type(heat_move))
print(np.shape(heat_move))
    
    
# for row in csv_reader_object:
    #print(row)
    

# seaborn.heatmap(heat_move)

# plt.imshow(heat_move, cmap='hot', interpolation='nearest')
# plt.show()


#DURCHARBEITEN
#https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html