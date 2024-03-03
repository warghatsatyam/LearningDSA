def uniqueChar(s): 
    # Write your code here
    pass
    d = {}
    for x in s:
        if x in d:
            d[x] = d.get(x)+1
        else:
            d[x] = 1
    unique_str = ''
    for x in d:
        unique_str+=x
    return unique_str

if __name__ == '__main__':
    s = input()
    print(uniqueChar(s))