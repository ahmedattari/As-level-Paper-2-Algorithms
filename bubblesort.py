# main function to call bubble_sort
def main():      
    print("unsorted",arr)
    bubble_sort(arr)
    print("sorted",arr)
    
    
    #input the user array 
arr = []
a = int(input("Enter the size that how many element of array you want "))
for i in range(a):
    d = int(input("Enter values "))
    arr.append(d)
    if i == a:
        break

# function to bubble sort the user array
def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

main()
input()