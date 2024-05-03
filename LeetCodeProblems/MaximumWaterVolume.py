from typing import List, Type


class Solution:

    def reduceWindow(self,height: List[int],i: int , j : int) -> (int,int):
        left_height = height[i]
        right_height = height[j]
        if height[i] <= height[j]:
            i=i+1
            while i < j and  height[i] < left_height:
                i = i + 1
        else:
            j=j-1
            while j > i and height[j] < right_height:
                j = j - 1

        print("now i, j are "+str(i)+ " "+str(j))
        return i,j

    def maxArea(self, height: List[int]) -> int:
        assert len(height) > 0
        i = 0
        j = len(height)-1
        max_volume = 0
        while i < j:
            volume = min(height[i], height[j]) * (j - i)
            max_volume = max(volume, max_volume)
            i, j = self.reduceWindow(height, i, j)
        return max_volume



def main():
    s = Solution();
    volume = s.maxArea([1,8,100,2,100,4,8,3,7])
    print(volume)

if __name__ == '__main__':
    main()

