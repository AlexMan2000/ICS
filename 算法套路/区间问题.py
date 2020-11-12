#铺垫
a = [[1,2],[2,5],[2,4],[5,6],[3,5]]
#按照每个列表的第一个元素排序
#保证第2号元素是倒序排列的
a.sort(key = lambda x:x[1],reverse=True)
#保证第1号元素是升序排列的
a.sort(key = lambda x:x[0])
# a.sort(key = lambda x:x[0])
# a.sort(key = lambda x:x[1],reverse = True)
print (a)


#