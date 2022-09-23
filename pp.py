def selSort (nums):
	n = len(nums)
	for bottom in range(n - 1):
		minPos = bottom
		for i in range (bottom + 1, n):
			if nums [i] < nums [minPos]:
				minPos = i


		temp = nums [bottom]
		nums [ bottom] = nums [ minPos]
		nums[minPos] = temp

def main():
	exampleList = [4, 10, 9, 2, 6, 7]
	
	print (“ original List”)
	for value in exampleList:
		print(value)
	selSort(exampleList)

	print(“Sorted list”)
	for value in exampleList:
		print(value)
