import numpy as np

A = [[1,2,3],[0,5,6],[1,0,1]]
print('Einfaches Summe:' + str(np.sum(A)))
print('Zweifaches Summe:' + str(np.sum(np.sum(A))))
print(np.shape(A))