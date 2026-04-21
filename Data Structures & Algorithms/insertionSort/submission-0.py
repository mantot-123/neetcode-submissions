# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []
        for i in range(len(pairs)):
            k = pairs[i]
            j = i-1
            # swap positions with elements before it bigger than the current element being checked
            while j >= 0 and k.key < pairs[j].key: 
                pairs[j+1] = pairs[j]
                j -= 1
            pairs[j+1] = k
            output.append([p for p in pairs])
        return output
        