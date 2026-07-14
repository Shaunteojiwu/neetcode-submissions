class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        
        for i in strs:
            key=tuple(sorted(i))
            
            if key not in dict:
                dict[key]=[]
            dict[key].append(i)

        return list(dict.values())
#class Solution(object):
#     def groupAnagrams(self, strs):
#         anagram_map = {}
        
#         for s in strs:
#             # 1. Create a frequency array of 26 zeros (one for each letter a-z)
#             count = [0] * 26
            
#             # 2. Count the occurrences of each character
#             for char in s:
#                 # ord(char) - ord('a') maps 'a'->0, 'b'->1, ..., 'z'->25
#                 count[ord(char) - ord('a')] += 1
            
#             # 3. Convert the list to an immutable tuple to use as a key
#             key = tuple(count)
            
#             # 4. Group them in the dictionary
#             if key not in anagram_map:
#                 anagram_map[key] = []
#             anagram_map[key].append(s)
            
#         return list(anagram_map.values())