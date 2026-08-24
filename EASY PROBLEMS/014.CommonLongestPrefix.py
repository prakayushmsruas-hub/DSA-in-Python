def longestCommonPrefix(strs):
    answer = ""
    found = False

    for i in range(min(len(s) for s in strs)):
        for j in range(len(strs)):
            if strs[j][i] != strs[0][i]:
                found = True
                break

        if found:
            break

        answer += strs[0][i]

    return answer


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
