import numpy as np
import random as rd
import scipy.stats as ss
import matplotlib.pyplot as plt


def distance(p1, p2):
    return np.sqrt(np.sum(np.square(p2 - p1)))

'''
p1 = np.array([2,3])
p2 = np.array([5,8])
print(distance(p1,p2))
'''
def max_votes(votes):

    votes_dict = dict()
    for vote in votes:
        if vote in votes_dict:
            votes_dict[vote] += 1
        else:
            votes_dict[vote] = 1

    winner = []
    maximum_votes = max(votes_dict.values())
    for can, num in votes_dict.items():
        if num == maximum_votes:
            winner.append(can)

    return rd.choice(winner)

points = np.array([[1,2], [2,3], [3,4], [3,2], [4,2], [3,3], [2,1]])
point = np.array([4,2.5])

plt.plot(points[:,0], points[:,1], "ro")
plt.plot(point[0], point[1], "bo")
plt.show()

def finding_nearest_neighbour(point, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(point, points[i])
        ind = np.argsort(distances)
    return ind
    # return distances[ind[:k]]

print(finding_nearest_neighbour(point, points, 2))
# print(distances)
# print(ind)
# print(distances[ind[0:2]])

def knn_predict(point, points, outcome, k=5):
    indices = finding_nearest_neighbour(point, points, k)
    return max_votes(outcome[indices])

outcome = np.array([1,1,1,2,2,2,2])
print(knn_predict(point, points, outcome))


