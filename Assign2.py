import numpy as np

n=int(input("Enter the number of rows (n): "))
m=int(input("Enter the number of columns (m): "))

matrix=np.array([list(map(int,input().split()))for _ in range(n)])

MaxElement = np.max(matrix)
MinElement = np.min(matrix)
print("Maximum Element is: ",MaxElement)
print("Minimum Element is: ",MinElement)

SortedMatrix = np.sort(matrix, axis=None)
print("Sorted Array: ")
print(SortedMatrix)

SortedMatrixRow = np.sort(matrix, axis=1)
print("Sorted Row_Wise: ")
print(SortedMatrixRow)

SortedMatrixCol = np.sort(matrix, axis=0)
print("Sorted column_Wise: ")
print(SortedMatrixCol)
