class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        ans = 0
        n = len(s)
        hash_map = {}
        while end < n:
            if s[end] in hash_map and hash_map[s[end]] == True:
                if s[start] == s[end]:
                    end+=1
                else:
                    hash_map[s[start]] = False
                start+=1
            else:
                ans = max(ans, end-start+1)
                hash_map[s[end]] = True
                end+=1

        return ans