class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        # delete all the uppercase letters in A
        # replace each vowel with #
        # concatenate the string with itself
        # return the resultant string
        A=A+A
        A=list(A)
        res=''
        for a in A:
            if a.isupper():
                continue
            if a in 'aeiou':
                res+="#"
            else:
                res+=a
        return res
