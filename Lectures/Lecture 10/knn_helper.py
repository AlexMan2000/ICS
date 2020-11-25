# -*- coding: utf-8 -*-
import util

def knn(p, data, k):
    # p the new observation that want to set lable
    # Calculating the distances b/w p & every pt. in data
    distances = {}
    for d in data:
        if d.distance(p) not in distances.keys():
            distances[ d.distance(p) ] = [ d ]
        else:
            distances[ d.distance(p) ].append(d)

    # Sorting the k nearest neighbours
    result = []        
    for key in sorted(distances.keys()):
        result.extend( distances[key] )

    k_nearest_neighbours = result[:k]

    # Assigning a label to the new point based on the k neighbours
    label_votes = { l:0 for l in util.LABELS }
    print(label_votes)
    for x in k_nearest_neighbours:
        label_votes[ x.getLabel() ] += 1
    max_label = sorted(label_votes, key = label_votes.get, reverse = True)[0]
    
    p.setLabel(max_label)
