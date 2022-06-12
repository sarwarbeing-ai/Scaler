# # This is the interface that allows for creating nested lists.
# # You should not implement it, or speculate about its implementation
# class NestedInteger:
#     def __init__(self, x):

#     # Return true if this NestedInteger holds a single integer, rather than a nested list.
#     def isInteger(self):

#     # Return the single integer that this NestedInteger holds, if it holds a single integer
#     # The result is 1e9 if this NestedInteger holds a nested list
#     def getInteger(self):

#     # Return the nested list that this NestedInteger holds, if it holds a nested list
#     # The result is an empty list if this NestedInteger holds a single integer
#     def getList(self):


class NestedIterator:
    def __init__(self, nestedList):
        self.finalList = self.flattenList(nestedList)
        self.count = -1

    def flattenList(self,l):
        l2 = []
        for ele in l:
            if ele.isInteger():
                l2.append(ele.getInteger())
            else:
                l2.extend(self.flattenList(ele.getList()))
        return l2

    def next(self):
        self.count+=1
        return self.finalList[self.count]

    def hasNext(self):
        return self.count<len(self.finalList) -1
