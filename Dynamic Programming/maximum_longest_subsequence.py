

def longest_subsequence(i,j,str1,str2):
    if i>=len(str1) or j>=len(str2):
        return 0
    if i==len(str1)-1 and j==len(str2)-1 and str1[i]==str2[j]:
        return 1 
    if i==len(str1)-1 and j==len(str2)-1 and str1[i]!=str2[j]:
        return 0 
    if str1[i] == str2[j]:
        return 1 + longest_subsequence(i+1,j+1,str1,str2)
    else:
        return max(longest_subsequence(i,j+1,str1,str2), longest_subsequence(i+1,j,str1,str2))
    
if __name__ == '__main__':
    str1 = 'abdgec'
    str2 = 'afbdqgzec'
    ans = longest_subsequence(0,0,str1,str2)
    print(ans)