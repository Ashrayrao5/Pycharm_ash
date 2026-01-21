import numpy as np

# a = np.array([[1,2,3,4],[ 5,6,7,8],[10,11,12,13]])
# print(a)
#
#
# print(a.shape)
# print(a.dtype)
# print(a.ndim)
#
#
# zeros = np.zeros((3,2))
# print(zeros)
# print(zeros.shape)
# print(zeros.dtype)
#
# ones = np.ones((2,2))
# print(ones)

# range_array = np.arange(0,9,3)
# print(range_array)

# linespace_array = np.linspace(0,1,11)
# print(linespace_array)
#
# b = np.random.random(3)
# print(b)
#
# c = np.random.rand(3)
# print(c)

#
# d = np.random.exponential(size = 3)
# print(d)

#
# a = np .array([[1,2,3], [3,4,5]])
# b = np.array([[1,2,3], [3,4,5]])
# c = a+b
# print(c)
# print(np.max(c))
# print(np.min(c))
# print(np.sum(c))
# print(np.mean(c))
# print(np.median(c))
# print(np.sin(c))
# print(np.cos(1))


scores = np.array([78, 85, 92, 70, 88, 94, 67, 73, 82, 90,
                   76, 84, 95, 69, 80, 87, 91, 77, 83, 86,
                   79, 81, 89, 72, 68, 93, 74, 75, 96, 88])

average_scores = np.mean(scores, axis=0)
print(average_scores)

std_deviation_scores = np.std(scores, axis=0)
print(std_deviation_scores)