import matplotlib.pyplot as plt
import numpy as np

# Numpy

# number + python = numpy
# 3+2 = 5

# [1, 2, 3] * 2 = [1, 2, 3, 1, 2 ,3]
# [1, 2, 3] * 2 = [2, 4, 6]
# print([2, 4, 6])
# arr = np.array([1, 2, 3])
# print(arr * 2)

# arr_Str = np.array(["Python", "HTML", "Java"])
# print(arr_Str[2])

# arange
# val = np.arange(1, 11)
# print(type(val))

# Matplotlib = 3graph = 1.line, 2.bar, 3.pie chart
# colour code = "r", "g", "b", "k", "orange", "y"

arr1 = np.array(np.arange(1,6))
arr2 = np.array([10, 20, 30, 40, 50])
# Line graph
# plt.plot(arr1, arr2, "r", linewidth=1.2, linestyle="", marker="*")
# Bar Graph
city = ["Delhi", "Mumbai", "Kolkata", "Chennai"]
lst = [45, 38, 32, 28]
# plt.bar(city, lst, color=["r", "g", "y", "b"])
# pie chart
plt.pie(lst, labels=city, explode=[0.2, 0, .5, 0], autopct="%1.1f%%")
# plt.xlabel("Value of X")
# plt.ylabel("Value of Y")
plt.show()