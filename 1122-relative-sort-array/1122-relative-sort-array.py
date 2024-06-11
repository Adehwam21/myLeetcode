class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count_dict = {num: arr1.count(num) for num in arr1}
        found, not_found= [], []

        for i in arr2:
            if i in arr1:
                found += [i] * arr1_count_dict[i]
        for i in arr1:
            if i not in arr2 and i not in not_found:
                not_found += [i] * arr1_count_dict[i]

        not_found.sort()
        result = found + not_found

        return result