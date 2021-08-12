class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            dic[tuple(sorted(s))].append(s)

        return list(dic.values())
