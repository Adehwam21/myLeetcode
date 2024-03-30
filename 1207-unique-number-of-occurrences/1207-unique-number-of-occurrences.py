class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        def count_occurences(arr: List[int]) -> dict:
            nums_count = {}
            for i in range(len(arr)):
                count = 0
                for j in range(len(arr)):
                    if arr[i] == arr[j]:
                        count += 1
                nums_count[arr[i]] = count
            return nums_count
        
        seen = set()
        occurences = count_occurences(arr)
        for i in occurences.values():
            if i in seen:
                return False
            else:
                seen.add(i)
        return True
          