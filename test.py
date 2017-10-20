import q1_reverse_string
import q2_perfect_square
import q3_insert_interval

s = 'hello'
print(s, 'reversed answer is', q1_reverse_string.reverse(s))

n = 16
print(n, 'is perfect square', q2_perfect_square.isPerfectSquare(n))
n = 14
print(n, 'is perfect square', q2_perfect_square.isPerfectSquare(n))

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(intervals, 'insert new interval', newInterval, 'result is', q3_insert_interval.insert(intervals, newInterval))
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 9]
print(intervals, 'insert new interval', newInterval, 'result is', q3_insert_interval.insert(intervals, newInterval))