def Linear_search(arr,target):
    indices=[]
    for i in range(len(arr)):
        arr[i]== target
        indices.append(i)
    return indices
n = int(input("Enter number of elements: "))
arr=[]
for i in range (n):
    arr.append(int(input(f"Enter element {i+1}: ")))
target=int(input("enter element to search: "))
result=Linear_search(arr,target)
if len(result)>0:
    print("element found at index: ",result)
else:
    print('invalid')