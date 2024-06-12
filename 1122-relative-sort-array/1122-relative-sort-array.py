class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count_dict = {}
        found, not_found= [], []
        
        # Initialize a hashmap to keep track of the occurence of an element in arr1
        for i in arr1:
            if i not in arr1_count_dict:
                arr1_count_dict[i] = 1
            else:
                arr1_count_dict[i] += 1
        
        # Check if element in arr2 and arr1
        # If true multiply the element by its occurence and append to the found array
        for i in arr2:
            if i in arr1:
                found += [i] * arr1_count_dict[i]
                
        # Check if element in arr1 is not in arr2 and not_found array
        # If true multiply the element by its occurence and append to the not_found array
        for i in arr1:
            if i not in arr2 and i not in not_found:
                not_found += [i] * arr1_count_dict[i]

        # Sort the not found array and concatenate with found array
        not_found.sort()
        return found + not_found