import random
def shellSort(arr): 
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap //= 2


def binaria(arr,elem):
    cont=0
    medio=(len(arr))/2
    narr=[]
    if arr[medio]==elem:
        print("El elemento esta en el indice "+str(medio))
    elif arr[medio]>elem:
        for num in range(0,medio):
            return binaria(arr,elem)


arr=[random.randint(0,10) for num in range(50)]
shellSort(arr)
binaria(arr,5)