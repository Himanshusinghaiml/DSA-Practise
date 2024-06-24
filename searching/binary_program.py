def binary(array,target):
    first=0
    last=len(array)-1
    while first<=last:
        mid=(first+last)//2
        if array[mid]==target:
            return [mid,target]
        elif array[mid]<target:
            first=mid+1
        else:
            last=mid-1
    return -1

list=[5,10,15,20,25,30]
target =20
ans=binary(list,target)
if ans !=-1:
    print('yes element found in the list at index :',ans[0],'and value is ',ans[1])
else:
    print('element not found')