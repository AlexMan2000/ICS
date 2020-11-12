def count_winner(teamname):
	"""
	:param teamname: String -- the name of a team entered by the user.
	:return: an integer -- the number of times the selected team appears.
	"""
	# to do
	winners_file = open('WorldSeriesWinners.txt','r')
	winners_list = winners_file.read().split('\n')
	winners_file.close()
	if teamname in winners_list:
		return winners_list.count(teamname)
	else:
		return 0


'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
'''


# def main():
#
# 	print ('New York Yankees', count_winner('New York Yankees')) # Expected output: 26
# 	print ('Boston Americans', count_winner('Boston Americans')) # Expected output: 1
# 	print ('Shanghai Sharks', count_winner('Shanghai Sharks')) # Expected output: 0
# 	print ('Real Madrid', count_winner('Real Madrid')) # Expected output: 0
# 	print ('Boston Red Sox', count_winner('Boston Red Sox')) # Expected output: 6
# 	print ('Cleveland Indians', count_winner('Cleveland Indians')) # Expected output: 2
#
#
# if __name__ == '__main__':
# 	main()