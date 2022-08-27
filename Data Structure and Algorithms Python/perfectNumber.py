class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        '''
        perfect number starts from 11,then 22,1111,1221,2112,...
        the last half of any number is just the reverse of the first half
        just add the number with its reverse
        if A is 100000 then answer would be 21111221212111122111121212211112
        so on reversing half of this number is just a constant time
        Hence TC:O(A)
        sc:O(3) maximum three elements will be stored in the queue as every time
        loop goes one element is popped up
        so SC:O(1)
        '''
        from collections import deque
        qu=deque([1,2])
        for i in range(A):
            dummy=qu.popleft()
            ans=str(dummy)+str(dummy)[::-1] # this will take a nearly constant time
            # this loop will run in constant time time
            for d in [1,2]:
                qu.append(dummy*10+d)
        return ans



    
