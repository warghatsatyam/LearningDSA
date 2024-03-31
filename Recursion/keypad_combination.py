


def get_keypad(n):
    keypad_val = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
    if n == 0:
        return [""]
    small_int = n//10
    rem_int = n%10
    rem_int_arr = keypad_val[rem_int]
    small_int_arr = get_keypad(small_int)
    final_arr = []
    for x in small_int_arr:
        for y in rem_int_arr:
            final_arr.append(x+y)
    return final_arr


if __name__  == '__main__':
    n=23
    ans = get_keypad(n)
    print(ans)