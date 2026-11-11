class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        nums=[1,2,3,4,5,6,7,8,9]
        def func(index,total,subset):
            if len(subset)==k and total==n:
                result.append(subset.copy())
                return
            if total>n or index>=9:
                return
            subset.append(nums[index])
            func(index+1,total+nums[index],subset)
            subset.pop()
            func(index+1,total,subset)
        func(0,0,[])
        return result