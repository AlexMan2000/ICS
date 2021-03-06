
import dice_student
import math
import matplotlib.pyplot as plt
import random
#
# import montecalo_helper

# compute the Eucliear distance of two vectors
def comp_dist(a, b):
    assert len(a) == len(b)
    d = 0
    for i in range(len(a)):
        d += (a[i] - b[i]) ** 2
    return math.sqrt(d)

def estimate_pi(num_points):
# replace the following line with your code

# use random.uniform(-1, 1) twice to get cordinate of a random dot
# record how many times dots are within unit circle
# estimate the area of circle
# estimate pi by pi
    in_set_x = []
    in_set_y = []
    out_set_x = []
    out_set_y = []
    pi = 0
    for i in range(num_points):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if comp_dist([0,0],[x,y]) <= 1.0:
            in_set_x.append(x)
            in_set_y.append(y)
        else:
            out_set_x.append(x)
            out_set_y.append(y)
    pi = 4*(len(in_set_x)/num_points)

# should return:
# - an estimate of pi
# - the x-axis cordinates list for those within the unit circle
# - the y-axis cordinates list for those within the unit circle
# - the x-axis cordinates list for those outside the unit circle
# - the y-axis cordinates list for those outside the unit circle
    return pi,in_set_x,in_set_y,out_set_x,out_set_y


results = []
# total number of random dots per trial
num_points_per_estimate = 1000
# perform multiple trails
num_trials = 100
for i in range(num_trials):
    est_pi, in_x, in_y, out_x, out_y = \
        estimate_pi(num_points_per_estimate)
    results.append(est_pi)

print("estimated pi: ", sum(results)/num_trials)

# visualize the dots in the last trial
plt.subplot(2, 1, 1)
plt.title('dots distribution')
plt.scatter(in_x, in_y, c='r')
plt.scatter(out_x, out_y, c='b')

# visualize the estimations of all trials
plt.subplot(2, 1, 2)
plt.title('estimate of pi')
plt.hist(results)

plt.show()
