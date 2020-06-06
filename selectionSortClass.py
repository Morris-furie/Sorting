

#create function
#make an array for the sorting of the selection

array = [13, 4, 9, 5, 3, 16, 12]


def selectionSort(array):

	n = len(array)

	for in range(n): #<-- whatever the length of the array is how many times you are going to run the for loop

		#initially assume the first element of the unsorted part as the minimum

		minimum = i
		for j in range(i+1, n):
			if (array[j] <array[minimum]): #<-----Comparison operator

				minimu = j

		#swap the minimum element with the first ekement of the unsorted part

		temp = array[i]
		array[i] = array[minimum]
		array[minimum] = temp
	return array

print(selectionSort(array))

