def longestConsecutiveSubsequence(arr):
    d = {}
    max_len=0
    start,end=0,0
    for x in arr:
        new_arr = []
        y=x
        while True:
            new_arr.append(y)
            y=y+1
            if y not in arr:
                break
        d[x]=new_arr
        child_max_length = len(new_arr)
        if max_len < child_max_length:
            max_len=child_max_length
            start = new_arr[0]
            end   = new_arr[-1]
    print(start,end)
    return d 




if __name__ == '__main__':
    arr = [2,12,9,16,10,5,3,20,25,11,1,8,6]
    arr = [3,7,2,1,9,8,41]
    d = longestConsecutiveSubsequence(arr)
    print(d)
