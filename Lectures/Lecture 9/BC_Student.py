import random
import util
import cluster_student as cluster
# import helper
import sample_student as sample

from kmeans_student import *


# Kmeans: take a list of samples and make k clusters


def kmeansTest(k=2, n=20, verbose=False):
    random.seed(0)

    """read the data from BC_data.csv
    create a dataset 'allSamples' which contains all data point 
    Use the first column 'id' as index
    Use the second column 'diagnosis' as label,
    Use 'radius_mean'  and 'texture_mean' as features  
    """
    print("before clustering")

    # read
    bcdatalines = open('BC_data.CSV', 'r').readlines()[1:]
    bcdatalines2 = [[i for i in line.strip().split(',')] for line in bcdatalines]

    allSamples = [sample.Sample(line[0],[float(j) for j in line[2:4]],line[4]) for line in bcdatalines2]

    util.plot_cluster([cluster.Cluster(allSamples)])


    # plot the data from the two groups "B" and "M"
    cluster_b = [s for s in allSamples if s.getLabel() == 'B']
    cluster_m = [s for s in allSamples if s.getLabel() == 'M']
    clusters = [cluster.Cluster(cluster_b), cluster.Cluster(cluster_m)]
    print("clustering with label info")
    util.plot_cluster(clusters)

    # Perform cluster analysis with k=2 and plot the clusters
    print("after clustering")
    """Implement cluster analysis here 
    """
    clusters = kmeans(allSamples,2,verbose)
    util.plot_cluster(clusters, verbose)

    print('Final result')
    for c in clusters:
        print('', c)


if __name__ == "__main__":
    random.seed(0)
    kmeansTest(k=2)
