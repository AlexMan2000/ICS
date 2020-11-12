# -*- coding: utf-8 -*-

import random
import util
import cluster_student as cluster

# Kmeans: take a list of samples and make k clusters
def kmeans(samples, k, verbose):
    """Assumes samples is a list of samples of class Sample,
         k is a positive int, verbose is a Boolean
       Returns a list containing k clusters. """

    #Get k randomly chosen initial centroids
    initialCentroids = random.sample(samples, k)

    #Create a singleton cluster for each centroid
    clusters = []
    for e in initialCentroids:
        clusters.append(cluster.Cluster([e]))

    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        # call kmeans_iter(samples, clusters, k) in this file
        converged = kmeans_iter(samples, clusters, k)

        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('\n') #add blank line
    return clusters

def kmeans_iter(samples, clusters, k):
    '''
        implement one iteration of kmeans:
        - each sample finds the closest cluster by computing
          its distance to the centroids of all the clusters
        - then compute every cluster's new centroid
        - the algorithm converges if cluster's centroid does not
          move any more
    '''
    #----------- your code here ---------#
    converged = True
    newClusters = []
    #要分成k类,就创建k个buckets
    for i in range(k):
        newClusters.append([])

    #对于每一个元素,找到距离它最近的那个cluster的centroid
    for e in samples:
        smallest_distance = float('inf')
        index = 0
        for i in range(1, k):
            distance = e.distance(clusters[i].getCentroid())
            if distance < smallest_distance:
                smallest_distance = distance
                index = i
        newClusters[index].append(e)

    #更新每一个cluster, 看看有没有cluster需要变更,如果有就说明还要继续取平均计算下一批centroids,如果没有就说明k-means算法已经完成.
    for i in range(len(clusters)):
        if clusters[i].update(newClusters[i]) > 0.0:
            converged = False
    return converged


    #----------- end of your code ---------#

# one run of kmeans
def main(k=2, n=20, verbose=False):
    random.seed(100)
    d1samples = util.genDistribution(n=20)
    d2samples = util.genDistribution(xMean=0, xSD=1, yMean=4, ySD=1, n=20)
    allSamples = d1samples + d2samples

    print("before clustering")
    util.plot_cluster([cluster.Cluster(allSamples)])
    
    print("after clustering")
    clusters = kmeans(allSamples, 2, verbose)
    util.plot_cluster(clusters, verbose)

    for c in clusters:
        print(c)


if __name__ == "__main__":
    random.seed(0)
    main(k = 2)
