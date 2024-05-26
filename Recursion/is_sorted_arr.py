def isSorted(a,si):
    l = len(a)
    if si == l-1:
        return True
    if a[si]> a[si+1]:
        return False
    smallerArrOutput = isSorted(a,si+1)
    return smallerArrOutput


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,0]
    output = isSorted(arr,0)
    print(output)

