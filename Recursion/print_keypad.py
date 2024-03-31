keypad_values = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def print_keypad_code(num,ans):
    if num==0:
        print(ans)
        return
    small_num = num//10
    rem_int   = num%10
    rem_int_arr = keypad_values[rem_int-2]
    for x in rem_int_arr:
        print_keypad_code(small_num,x+ans)




if __name__ == '__main__':
    num = 23
    ans = ''
    print_keypad_code(num,ans)
