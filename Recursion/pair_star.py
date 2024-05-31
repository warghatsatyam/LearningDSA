
def pair_star(str):
    if len(str) == 1:
        return str 
    small_string = pair_star(str[1:])
    if str[0] == small_string[0]:
        return str[0] + '*' + small_string
    else:
        return str[0] + small_string



if __name__ == '__main__':
    str = input()
    output = pair_star(str)
    print(output)