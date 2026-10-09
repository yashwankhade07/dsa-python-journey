class Solution:
    def answer(self,array,target):
        for i in range(len(array)):
            for j in range(i+1,len(array)):
                if array[i]+array[j] == target :
                    return [i,j]

        return []

arr = [2, 6, 5, 8, 11]
t = 14

s = Solution()
print(s.answer(arr,t))
