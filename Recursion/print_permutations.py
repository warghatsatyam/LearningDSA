

def permutations(strx,ans):
    if len(strx)==1:
        ans+=strx[0]
        print(ans)

        return
    for i in range(len(strx)):
        ele = strx[i]
        new_ans = ans+ele
        str1 = strx[0:i]
        str2 = strx[i+1:]
        small_str = str1+str2
        permutations(small_str,new_ans)

str1 = 'abc'
permutations(str1,'')


# def permutations(s, ans):
#     if len(s) == 0:
#         print(ans)
#         return

#     for i in range(len(s)):
#         new_ans = ans + s[i]
#         remaining_chars = s[:i] + s[i+1:]
#         permutations(remaining_chars, new_ans)

# str1 = 'abc'
# permutations(str1, '')