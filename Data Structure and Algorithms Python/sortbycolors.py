def sortColors(A):
    # sort an array A containing numbers 0,1,2 without using
    # sort function
    if len(set(A))==1:
        return A
    if len(set(A))==2:
        m=max(A)
        mn=min(A)
        c_max=A.count(m)
        c_min=A.count(mn)
        res=[mn]*c_min+[m]*c_max
        return res
    if len(set(A))==3:
        c_0=A.count(0)
        c_1=A.count(1)
        c_2=A.count(2)
        return [0]*c_0+[1]*c_1+[2]*c_2
