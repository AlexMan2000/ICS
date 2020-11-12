#def euclidean_distance(xy1,xy2):
#    return ( (xy1[0]-xy2[0])**2 + (xy1[1]-xy2[1])**2 ) ** 0.5

def manhanttan_dist(xy1, xy2):
    return abs(xy1[0]-xy2[0])+abs(xy1[1]-xy2[1])

def min_manhattan(coordinates):
    print(coordinates)
    import math
    min_sum = math.inf
    min_point = None
    coordinates_x = [coordinate[0] for coordinate in coordinates]
    coordinates_y = [coordinate[1] for coordinate in coordinates]
    max_x = max(coordinates_x)
    max_y = max(coordinates_y)
    low_x = min(coordinates_x)
    low_y = min(coordinates_y)
    rectangle = []
    for row in range(low_y,max_y+1):
        tmp = []
        for col in range(low_x,max_x+1):
            tmp.append((col,row))
        rectangle.append(tmp)
    for row in range(len(rectangle)):
        for col in range(len(rectangle[0])):
            tmp_sum = 0
            for i in range(len(coordinates)):
                tmp_sum += manhanttan_dist(rectangle[row][col],coordinates[i])
            if tmp_sum < min_sum:
                min_point = rectangle[row][col]
                min_sum = tmp_sum

    return min_point



            

if __name__ == "__main__":
    # Read test.txt, create list of coordinates
    all_coords = open("site_selection_test.txt","r").read().split("\n")[:-1]
    coordinates = []
    for xypair in all_coords:
        x,y = xypair.split(" ")[0], xypair.split(" ")[1]
        coordinates.append( (int(x),int(y)) )

    # Compute the x,y pair that is on average closest to all points
    closest_avg = min_manhattan(coordinates)

    # Answer is (8,3) for the test case
    print("Most central point to all points in test.txt: ", closest_avg) 
