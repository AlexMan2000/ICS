#自底向上的递归
def maxpath(triangle):
    def helper(i,triangle):
        if i == 0:
            return [17]
        upper = helper(i-1,triangle)
        result = [upper[0]+triangle[i][0]]+[max(upper[j-1]+triangle[i][j],upper[j]+triangle[i][j]) for j in range(1,i)]+[upper[-1]+triangle[i][-1]]
        return result
    return max(helper(len(triangle)-1,triangle))

print(maxpath([[17],[15,8],[5,10,8],[16,6,10,12],[19,10,5,15,12]]))


#自顶向下的递归
def maxpath_rec(triangle):
    def helper(depth,index):
        if depth == len(triangle)-1:
            return triangle[depth][index]
        return triangle[depth][index] + max(helper(depth+1,index),helper(depth+1,index+1))
    return helper(0,0)

print(maxpath_rec([[17],[15,8],[5,10,8],[16,6,10,12],[19,10,5,15,12]]))


# if __name__ == "__main__":
#
#     triangle = open("maximum_path_triangle.txt","r").read().split("\n")
#
#     for x in range(len(triangle)):
#         triangle[x] = triangle[x].split(" ")
#         for y in range(len(triangle[x])):
#             triangle[x][y] = int(triangle[x][y])
#
#     for row in triangle:
#         print(row)
#
#     print()
#     print("The maximum path results in: ", maxpath(triangle))
#     # Answer is 538 for the test case in triangle.txt
#
#     for row in triangle:
#         print(row)
