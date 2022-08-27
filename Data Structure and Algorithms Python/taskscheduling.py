class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        '''
        A CPU has N tasks to be performed. It is to be noted that
        the tasks have to be completed in a specific order to avoid deadlock.
        In every clock cycle, the CPU can either perform a task or move it to
        the back of the queue. You are given the current state of the scheduler
        queue in array A and the required order of the tasks in array B.

        Determine the minimum number of clock cycles to complete all the tasks.
        '''
        if len(A)==1:
            return 1
        from collections import deque
        qu=deque(A)
        count=0
        for b in B:
            while len(qu)!=0:
                a=qu.popleft()
                if a==b:
                    count+=1
                    break
                else:
                    count+=1
                    qu.append(a)
        return count
