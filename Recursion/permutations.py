def substring_func(str):
    if len(str)==1:
        return [str[0]]
    output= []
    for i in range(len(str)):
        ele = str[i]
        str1 = str[0:i]
        str2 = str[i+1:]
        smaller_str = str1+str2
        ans = substring_func(smaller_str)
        for x in ans:
            output.append(x+ele)
    return output
str = 'abc'
ans = substring_func(str)
print(ans)