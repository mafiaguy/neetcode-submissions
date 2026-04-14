class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = []
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            
            freq_list.append((nums[i], count))
            visited.add(nums[i])
        
        freq_list.sort(key=lambda x: x[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(freq_list[i][0])
        
        return result