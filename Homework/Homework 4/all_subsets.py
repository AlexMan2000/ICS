def all_subsets(lst):
	'''
	:param lst: List -- list given by the user
	:return: a list containing all the subsets of lst
	'''
	# to do
	res = []
	n = len(lst)

	def cache(i, tmp):
		res.append(tmp)
		for j in range(i, n):
			cache(j + 1, tmp + [lst[j]])

	cache(0, [])
	return res


'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
'''


# def main():
# 	print (all_subsets([1])) # [[],[1]]
# 	print (all_subsets([1,2])) # [[],[1],[2],[1,2]]
#
#
# if __name__ == '__main__':
# 	main()

