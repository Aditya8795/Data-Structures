# Various sorting techniques - Ascending Order

# Insertion sort, Merge sort, Heap sort,
# Quick sort, Counting sort, Radix sort, Bucket sort


'''
* Its In-Place => requires O(1) extra memory
* Efficient for (quite) small data sets
(The size of list for which insertion sort has the
advantage varies by environment and implementation,
but is typically between eight and twenty elements.)

This is like sorting cards, you take the first
card and seperate it. Then we move on the next
card and keep it sorted with respect to the
second card then the third card with
respect to the first 2, and SO ON.
'''
def insertionSort(a):
    print("\n Performing Insertion Sort on the following list of numbers \n")
    print(a)
    # we start from 1 as the first element by itself is trivially sorted
    for i in range(1,len(a)):
        # select the next element among the unsorted (a[i] to a[len(a)-1])
        key = a[i]
        # insert key into its position in the sorted part (a[0] to a[i-1])
        j = i - 1
        '''
replace key<a[j] with key>a[j] for Descending
        '''
        while(j>=0 and key<a[j]):
            # as key is smaller than the j'th element we move towards a[0]
            # switching the elements as we traverse
            a[j+1] = a[j]
            j = j - 1
        # now that we reached a point where key>=a[j]
        a[j+1] = key

        if(i==(j+1)):
            print("\n\nvalue at index "+str(i)+" wasn't moved")
        else:
            print("\n\n moved "+str(key)+" from index "+str(i)+" to the index "+str(j+1)+"\n")
        print("\nThe list is now ->")
        print(a)
        
insertionSort([1,9,8,7,6,5.9997,4.9999,3,3.00001,2.9999999999999,1,1,0,0.3,0.6,-3,-999])
