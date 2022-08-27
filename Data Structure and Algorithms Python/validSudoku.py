class Solution:
	# @param A : tuple of strings
	# @return an integer
	def isValidSudoku(self, A):
        # determine if a sudoko is valid or not
        # rule1:none of the rows contain duplicates
        # rule2: none of the columns contain duplicates
        # rule 3: each 9 sub-boxes should not contain duplicates
        # if the above three rules held then the sudoko is valid
        # else invalid

        # check for rule 1
        for i in range(len(A)):
            a=A[i]
            d={}
            for aa in a:
                if aa=='.':
                    continue
                else:
                    if aa in d:
                        return 0
                    else:
                        d[aa]=1
        # check for rule 2
        for i in range(9):
            d={}
            for aa in A:
                a=aa[i]
                if a=='.':
                    continue
                else:
                    if a in d:
                        return 0
                    d[a]=1
        # check for rule 3
        # each of the 9 sub-boxes of the grid must contain no duplicate
        k=0
        while k<=6:
            d1={}
            d2={}
            d3={}
            for i in range(k,k+3):
                aa=A[i]
                for j in range(0,9,3):
                    a=aa[j:j+3]
                    if j==0:
                        for m in range(3):
                            if a[m]=='.':
                                continue
                            else:
                                if a[m] in d1:
                                    return 0
                                d1[a[m]]=1
                    elif j==3:
                        for m in range(3):
                            if a[m]=='.':
                                continue
                            else:
                                if a[m] in d2:
                                    return 0
                                d2[a[m]]=1
                    else:
                        for m in range(3):
                            if a[m]=='.':
                                continue
                            else:
                                if a[m] in d3:
                                    return 0
                                d3[a[m]]=1
            k+=3
        return 1
