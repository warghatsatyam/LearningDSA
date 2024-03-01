def get_maximum_occurence_in_dict(arr):
    d = {}
    if len(arr)>0:
        for ele in d:
            d[ele] = d.get(ele,0)+1
        max_key = arr[0]
        max_value = 1

        for x in d:
            val = d[x]
            if val > max_value:
                max_key = x 
                max_value = val 
        return max_key
    else:
        return 0

def input_arr():
    arr = []
    arr_len = input()
    if arr_len != '' and int(arr_len)>0:
        arr_str = input()
        if len(arr_str) == 0:
            return arr 
        else:
            arr = arr_str.split(' ')
            arr = [int(x) for x in arr]
            return arr 
    return arr

if __name__ == '__main__':
    arr_len = int(input())
    inp_arr = list(map(int, input().split()[:arr_len]))
    max_key = get_maximum_occurence_in_dict(inp_arr)
    print(max_key)
