# Various sorting techniques

# Insertion sort, Merge sort, Heap sort, Quick sort, Counting sort, Radix sort, Bucket sort

test = [1,9,8,7,6,5,95,93,29,17,4,199,43,394,59,3,30,34,704,601,26,69,89,99,999,9868,95,59,939,14,12,604,5023,13,6,-3,-99]

# Insertion sort

'''

Why study this О(n^2) algorithm? as wiki says it has the following advantages,

* Its In-Place - requires O(1) extra memory

* Efficient for (quite) small data sets
	The size of list for which insertion sort has the
	advantage varies by environment and implementation,
	but is typically between eight and twenty elements.

* Adaptive
	 It's efficient for data sets that are already substantially sorted: 
	 the time complexity is O(nk) when each element in the input is no more
	 than k places away from its sorted position.

* Stable - It does not change the relative order of elements with equal keys.

* Online - It can sort a list as it receives it.

LOGIC

This is like sorting cards, you take the first
card and seperate it. Then we move on the next
card and keep it in it's place next to the
first card. So we have ever increasing set 
of sorted cards in our left hand while we pick
cards from the unsorted set and _Insert_ it into
the appropriate position in the sorted set of cards.

In the below code, we are operating on a list a [0 ... len(a)-1]
as we sort In-Place, here the left of the array progressively becomes sorted.
We can think of i and j as 2 pointers, starting from 1 and 0

i is used to traverse the list and pick the 'key' from the unsorted elements.
it also keeps track of the division between the sorted and unsorted sub-lists.
j is used to find the position in the sorted sublist where 'key' is supposed
to be.

For each 'key' we select the next element among the unsorted set
(a[i] to a[len(a)-1]). Now in the while loop j goes on swapping numbers
till it reaches the position where k is supposed to be (key>=a[j]).
'''

def insertionSort(a):
	for i in range(1,len(a)):
		key = a[i]
		j = i - 1

		# Note: You could replace 'key<a[j]' with 'key>a[j]' for Descending
		while(j>=0 and key<a[j]):
			a[j+1] = a[j]
			j = j - 1
		a[j+1] = key
		
		# Just to let us know whats happening - prints to the Cmd line.
		if(i==(j+1)):
			print("\n\nThe value at index "+str(i)+" wasn't moved.")
		else:
			print("\n\nWe have moved '"+str(key)+"' from index "+str(i)+" to the index "+str(j+1)+"\n")
		print("\nThe list is now sorted upto index "+str(i))
		print(a)

# Merge sort

'''
This algorithm has a worst case running time of O(n*ln(n)).
But for small lists insertion sort beats merge sort (The constant term hidden in the O notation makes a difference) 
So for optimal performance we can use merge sort upto some small list size
and then use insertion sort.

This requires a auxiliary space of O(n)

'''

# This takes a list of numbers - 'a', starting and ending index - p & q, and sorts them in ascending order.
def mergeSort(a,p,r):
	# a singleton list is trivially sorted
	if(p>=r):
		return
	else:
		# // => integer division
		q = (p+r)//2
		mergeSort(a, p, q)
		mergeSort(a, q+1, r)
		# Now that a[p..q] and a[q+1..r] is sorted
		merge(a,p,q+1,r)

# Given sorted a[i...j-1] and a[j...k], this function sortes and merges both into the same list a[i...k]
def merge(a,i,j,k):
	temp = []
	p = i
	q = j

	#print("\nPerforming Merge on sublists of size "+str(j-1-i)+" and "+str(k-j))
	#print(a)
	#print("\nThe sorted sublists are from "+str(i)+" to "+str(j-1)+" and from "+str(j)+" to "+str(k))

	# while there are elements left in both sub lists, sort them into temp
	while(p<j and q<(k+1)):
		if(a[p]<a[q]):
			temp.append(a[p])
			p = p + 1
		else:
			temp.append(a[q])
			q = q + 1

	# once we have done with a minimum of 1 of the 2 sorted lists we append the remaining list onto the now merged list 'temp'
	if(p == j):
		while(q<(k+1)):
			temp.append(a[q])
			q = q + 1
	elif(q == (k+1)):
		while(p<j):
			temp.append(a[p])
			p = p + 1

	# the merged list 'temp' is used to overwrite both sublist's in 'a'
	for l in range(i,k+1):
		a[l] = temp[l-i]

	#print("\nBoth sublists have been merged!")
	#print(a)

# Heap sort - Max heap

'''
The (binary) heap data structure is an array object that we can view as a
nearly complete binary tree.
For the heapsort algorithm, we use max-heaps. Min-heaps commonly implement
priority queues. - WHYYY???
Here the max-heap property refers to a[i//2] >= a[i]. which mens parents are always larger
than its children.

'''

# This is used to maintain the max-heap property, assuming the child subtree's of a[i] are satisfying max-heap
# the value at a[i] is floated down such that the subtree rooted at index i obeys the max-heap property.
def maxHeapify(a,i):

	print("\n Working on "+str(a[i])+" and its children")
	print(a)

	# The two subtrees of a[i]
	leftIndex = 2*i
	rightIndex = 2*i + 1
	largestIndex = i # just for now, so that later we can check if it's children were larger.
	leftValue = None
	rightValue = None
	rootValue = a[i]
	try:
		leftValue = a[leftIndex]
	except IndexError:
		print("leftIndex doesnt exist")
	try:
		rightValue = a[rightIndex]
	except IndexError:
		print("leftIndex doesnt exist")

	if(leftValue and leftValue>rightValue and leftValue>rootValue):
		largestIndex = leftIndex
		print("\nleft child of "+str(a[i])+" i.e. "+str(a[leftIndex])+" is the largest")
	if(rightValue and rightValue>leftValue and rightValue>rootValue):
		largestIndex = rightIndex
		print("\nright child of "+str(a[i])+" i.e. "+str(a[rightIndex])+" is the largest")

	if(largestIndex == i):
		print("No further change required - rootValue is the largest")
		return
	
	# among its immediate children correct a[i]'s position
	temp = a[i]
	a[i] = a[largestIndex]
	a[largestIndex] = temp

	print("so after switching them we get =>")
	print(a)
	# move on to ensure that in a[largestIndex]'s children a[i] finds its correct position
	maxHeapify(a,largestIndex)

# This runs in linear time to produce a maxheap from an unordered input array.
def buildMaxHeap(a):
	# fix all the nodes bottom-up starting from the First parent - parent of the leaf node
	for i in range(len(a)//2,0,-1):
		maxHeapify(a,i)


# TESTS

print("START Testing\n")

'''
print("\nPerforming Insertion Sort on 'test' ")
print(test)
insertionSort(test)
'''

'''
print("\nPerforming Merge Sort on 'test' ")
print(test)
merge([3,4,1,2,3,4,5,-3,-2,-1,0],2,7,10)
mergeSort(test, 0, (len(test)-1))
print(test)
'''

'''
print("Testing maxHeapify starting at 'index = 2'")
test1 = ["dummy",16,4,10,14,7,9,3,2,8,1]
print(test1)
maxHeapify(test1,2) # We use index's starting from 1 as 2*0 = 0 (the finding of children won't work)
print("\n\nThis the final result is =>")
print(test1)
if(['dummy', 16, 14, 10, 8, 7, 9, 3, 2, 4, 1] == test1):
	print("\n\nTest is likely to have been passed")
else:
	print("\n\nTest has failed!!")
'''

print("Testing buildMaxHeap")
test2=["dummy",4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print(test2)
buildMaxHeap(test2)
print("\n\nThis the final result is =>")
print(test2)
