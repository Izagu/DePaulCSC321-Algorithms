#readFiles
def read_Files(file):
    infile = open(file, "r")
    fname = infile.read()
    strings = fname.split('\n')
    lst = []
    for i in strings:
        if i!= '':
            lst.append(int(i))
    infile.close()
    return lst

#Check sorted

def sorts(array):
    for i in range(0,len(array)-1):
        if array[i] > array[i+1]:
            return False
        return True
    
def sortedReversed(array):
    for i in range(0,len(array)-1):
        if array[i] < array[i+1]:
            return False
        return True
#insertion sort
def insertionS(file)
    arr=read_files(file)
    if sorts(array):
        return (array)
    elif sortedReversed(file):
        array.reverse()
        return array
    else:
        for i in range(len(array)):
            element = array[i]
            j = i-1
            while element < array[j] and j>=0:
                array[j+1] = array[j]
                j-=1
            A[j+1] = element
        return array
            
#merge sort

def mergeS(file):
    lst = read_Files(file)
    if sorts(lst):
        return array
    elif sortedReversed(lst):
        return array.reverse()
    else:
        return merge_Sort(lst)
    
    
def merge_Sort(array):
    if len(array) <= 1:
        return array
    if len(array) == 2:
        if array[0] > array [1]:
            array[0] += A[1]
            array[1] = array[0] - array[1]
            array[0] = array[1] - array[1]
        return array
    if len(array) > 2:
        center = (len(array)//2)
        left = array[:center]
        right = array[center:]

    #because we have to split the array multiples times we can call each side recursively

        merge_sort(left)
        merge_sort(right)
        return merger(left,right)
    
def merger(L,R):
    ans = []
    i=0
    j=0
    while i<len(L) and j <len(R):
        if L[i] <= R[j]:
            ans.append(A[i])
            i+=1
        else:
            ans.append(R[j])
            j+=1
        return ans


def quickS(file):
    lst = read_Files(file)
    if sorts(lst):
        return array
    elif sortedReversed(lst):
        return array.reverse()
    else:
        quick_sort(array, 0, len(array)-1)
    return array

def quick_Sort(array, fst, lst):
    if fst < lst:
        i = quick_Sort(array, fst, lst)
        quick_Sort(array, fst, i-1)
        quick_Sort(array, i+1, lst)
    
def partions(A,fst,lst):
    pivot=array[lst]
    i=fst-1
    for j in range(fst,lst):
        if A[j]<=pivot:
            i+=1
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
    i+=1
    temp=A[i]
    A[i]=A[last]
    A[last]=temp
    return i
    
    
