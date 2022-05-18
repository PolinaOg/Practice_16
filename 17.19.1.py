L = list(map(int, input('Enter yours numbers for array (minimum 2)').split()))

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

sort=merge_sort(L)
print('Sorted array', merge_sort(L))
print('Elements quantity', len(merge_sort(L)))


def binary_search(array, element, left, right):
    if left > right:
        return False
#   print('left',left)
#   print('right',right)
    middle = (right + left) // 2
#    print('middle',middle)
    if ((array[middle] < element) and array[middle+1] >= element):
        return middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

element = int(input('Enter your number from 0 to 99'))
array = [i for i in range(0,len(L))]

print('Founded element in sorted array is:',binary_search(sort, element, 0, (len(L)-1)))
b=200


#a = int(input('Enter your number from 0 to 99'))
a=element
if a < 0 or a > 99:
    print("Number is not from 0 to 99")
else:
#    print (len(L))
    for i in range (0, len(L)-1):
#        print (i)
#        print(L[i])
        if L[i]<a and L[i+1]>=a:
            b=i
if b==200:
   print('Enter another value')
else:
    print('Number of founded element in initial array is:=',b)
                  #print("This number is not in the array")







