import sys
def minArr(arr,min_ele):
    if len(arr)==0:
        print(min_ele)
        return
    
    ele = arr[0]
    min_ele = min(min_ele,ele)
    minArr(arr[1:],min_ele)


if __name__ == '__main__':
    min_ele = sys.maxsize
    arr = [1,2,3,3]
    minArr(arr,min_ele=min_ele)