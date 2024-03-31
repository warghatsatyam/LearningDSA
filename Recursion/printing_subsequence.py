def printin_subsequence_code(s,ans):
    if len(s)==0:
        print(ans)
        return
    
    ele = s[0]
    printin_subsequence_code(s[1:],ans)
    printin_subsequence_code(s[1:],ans+ele)


if __name__=='__main__':
    s = 'abc'
    printin_subsequence_code(s,'')