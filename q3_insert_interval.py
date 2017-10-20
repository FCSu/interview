def insert(intervals, newInterval):
	left = []
	right = []
	for i in intervals:
		if i[1] < newInterval[0]:
			left.append(i)
		elif i[0] > newInterval[1]:
			right.append(i)
		else:
			newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
	return left + [newInterval] + right
