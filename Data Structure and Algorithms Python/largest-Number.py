from functools import cmp_to_key
# write a comparator,if xy>yx the return 1 ,if xy<yx then return -1
# else 0
def cmp(a,b):
    if int(str(a)+str(b))>int(str(b)+str(a)):
          return 1
    elif int(str(a)+str(b))<int(str(b)+str(a)):
          return -1
    else:
          return 0
def largestNumber(A):
    # A is a list
    # return the largest integer in string
    mx=max(A) # get the maximum element in A
    if mx==0:
       return "0"
    # after sorting the element y will appear before x if xy is larger
    # than yx in  he sorted list A
    # if yx is larger than xy then x will apear before y in the sorted list A
    # if A=[3,30,34,5,9,6]
    # then the sorted list will be [30,3,34,4,6,9]
    A.sort(key=cmp_to_key(cmp)) # sort the numbers according to the comparator cmp
    s=''
    # iterate from the end ,add to s
    for i in range(len(A)-1,-1,-1):
       s+=str(A[i])
    return s # finally return s
