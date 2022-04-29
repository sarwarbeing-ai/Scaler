def merge(A, n1, B, n2):
    ans =[]
    i=0
    j=0
    while i<n1 and j<n2:
        if A[i]<B[j]:
            ans.append(A[i])
            i+=1
        else:
            ans.append(B[j])
            j+=1
    while j<n2:
        ans.append(B[j])
        j+=1
    while i<n1:
        ans.append(A[i])
        i+=1





    return ans
