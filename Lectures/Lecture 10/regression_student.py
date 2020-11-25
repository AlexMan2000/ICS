# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import sample_student as sample
import util


VERBOSE = False


def make_data(n, w=1, scale=1):
    """ A simple y = wx curve, with noisy displacement on both
        both x and y axis; change scale to change the range
    """
    linear_data = [sample.Sample('', [float(x) / scale, float(x) / scale * w], '') for x in range(n)]
    noise = util.genDistribution(xSD=0.3, ySD=0.3, n=n)
    data = [linear_data[i] + noise[i] for i in range(n)]
    return data


def compute_error(pred, truth):
    """ mean square error:
        sum of (pred[i] - truth[i])^2, divided by 2*length
    """
    total = 0
    for i in range(len(pred)):
        total += (pred[i]-truth[i])**2
    return total/(2*len(pred))


def compute_grad(pred, truth, x):
    """ gradient is mean of (pred[i] - truth[i]) * x[i]
    """
    total = 0
    for i in range(len(pred)):
        total += (pred[i]-truth[i])*x[i]
    return 1*total/len(pred)


if __name__ == "__main__":

    num_samples = 100

    # Generating random data
    data = make_data(num_samples, w=2, scale=10)

    # Make a random split of the data
    random.shuffle(data)
    train_data = data[:80]
    test_data = data[80:]

    # Plotting the randomly generated data
    d_x = [d.getFeatures()[0] for d in train_data]
    d_y = [d.getFeatures()[1] for d in train_data]
    plt.scatter(d_x, d_y)
    plt.show()

    # hyper params
    num_iter = 10
    learning_rate = 0.01
    margin = 0.01

    # to store error history for plotting purpose
    error_history = []
    # w is the parameter to be learned, set initial value for w
    w = - 0.5

    steps = 0
    # training loop
    while True:

        # predict and compute error
        pred_y = [w * x for x in d_x]
        error = compute_error(pred_y, d_y)
        error_history.append(error)

        plt.scatter(d_x, d_y)
        plt.plot(d_x, pred_y, 'r')
        title_str = "train error: %0.2f" % error
        plt.title(title_str)
        plt.show()

        steps += 1
        if error <= margin or steps >= num_iter:
            break

        # gradient descent
        grad = compute_grad(pred_y, d_y, d_x)
        w -= learning_rate * grad

        if VERBOSE and input("cont? (y/n) ") == 'n':
            break

    # testing on test data
    d_x = [d.getFeatures()[0] for d in test_data]
    d_y = [d.getFeatures()[1] for d in test_data]
    pred_y = [w * x for x in d_x]
    error = compute_error(pred_y, d_y)

    plt.scatter(d_x, d_y)
    plt.plot(d_x, pred_y, 'r')
    title_str = "test error: %0.2f" % error
    plt.title(title_str)
    plt.show()

    plt.plot(error_history)
    plt.title('training error')
    plt.show()
