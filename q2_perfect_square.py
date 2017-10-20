def isPerfectSquare(num):
	start = 1
	end = num
	while start <= end:
		mid = (start + end) / 2
		target = mid ** 2
		if target == num:
			return True
		elif target > num:
			end = mid - 1
		else:
			start = mid + 1
	return False
