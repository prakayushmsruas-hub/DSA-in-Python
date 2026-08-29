class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        note = {}
        mag = {}

        for ch in ransomNote:
            if ch not in note:
                note[ch] = 1
            else:
                note[ch] += 1

        for ch in magazine:
            if ch not in mag:
                mag[ch] = 1
            else:
                mag[ch] += 1

        for ch in note:
            if ch not in mag:
                return False

            if mag[ch] < note[ch]:
                return False

        return True
S=Solution()
print(S.canConstruct("aa","aab"))    