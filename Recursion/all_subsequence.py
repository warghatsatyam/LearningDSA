def all_subsequence(s):
    if len(s) == 0:
        return [""]
    
    ele = s[0]
    ans = all_subsequence(s[1:])
    final_arr = []
    final_arr.extend(ans)
    for i in ans:
        final_arr.append(ele+i)
    return final_arr


if __name__ == '__main__':
    s = 'asb'
    ans = all_subsequence(s)
    for ele in ans:
        print(ele)
