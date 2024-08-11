def binary_search(arr,key):


  low=0
  high=len(arr)-1
  while low<=high:
      mid=(low+high)//2
      if arr[mid]==x:
          return mid
      elif arr[mid]:
           low=mid+1
      else:
           high=mid-1
           return-1    
arr=[15,23,52,89,90]
x=52
result=binary_search(arr,x)
if result==-1:
  print(f"{x} not found array")
else:
  print(f"{x} found at index {result}")
