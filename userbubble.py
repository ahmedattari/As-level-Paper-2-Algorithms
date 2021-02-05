# array is a name of liabrary from which we call every thing which library offers
from array import *

# main function to call the bubble sort algorithm for character string 
def main():
    print("unsorted",arr)
    sort(arr)
    print("sorted",arr)
    
# binary search 
    if bisch(arr):
        print("found")
    else:
        print("not found")

# input the user array 
arr = array('i',[])
a = int(input("Enter the size of array in Integer "))
for i in range(a):
    d = int(input("Enter values "))
    arr.append(d)
    if i == a:
        break
print(arr)

# function to bubble sort the user array
def sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# function of binary search using while loop
def bisch(arr):
    l = 0 
    u = len(arr)-1
    b = int(input("enter the value to search from the array "))
    while l <= u:
        mid = (l+u)//2
        if arr[mid] == b:
            return True
        elif arr[mid] < b:
            u = mid+1
        else:
            l = mid-1
        break
    return False
main()
input()