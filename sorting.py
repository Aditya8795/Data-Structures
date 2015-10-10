# Various sorting techniques - Ascending Order

# Insertion sort, Merge sort, Heap sort,
# Quick sort, Counting sort, Radix sort, Bucket sort

test = [1,9,8,7,6,5.9997,4.9999,3,3.00001,2.9999999999999,1,1,0,0.3,0.6,-3,-999]

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
        
#insertionSort(test)

# Given sorted a[i...j-1] and a[j...k], this function merges both into sorted a[i...k]
def merge(a,i,j,k):
    temp = []
    p = i
    q = j
    # we compare the least of both sorted lists and create the merged list 'temp'
    while(p<j and q<(k+1)):
        if(a[p]<a[q]):
            temp.append(a[p])
            p = p + 1
        else:
            temp.append(a[q])
            q = q + 1
            
    # once we have done with a minimum of 1 of the 2 sorted lists we append the remaining list onto the now merged list 'temp'
    if(p==j):
        while(q<(k+1)):
            temp.append(a[q])
            q = q + 1
    elif(q==(k+1)):
        while(p<j):
            temp.append(a[p])
            p = p + 1
            
    # the merged list 'temp' is used to overwrite the existing list 'a'
    for l in range(len(temp)):
        a[i+l] = temp[l]

# test for merge
#merge([1,2,3,4,5,-3,-2,-1,0],0,5,8)

def mergeSort(a,p,r):
    # a singleton list is trivially sorted
    if(p>=r):
        return
    else:
        # // => integer division
        q = (p+r)//2
        mergeSort(a, p, q)
        mergeSort(a, q+1, r)
        merge(a, p, q, r)

print(test)
mergeSort(test, 0, (len(test)-1))
print(test)

