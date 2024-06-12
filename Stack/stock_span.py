

def stock_span(arr):
    stock_span_arr = []
    for i in range(len(arr)):
        count = 1
        j = i-1
        while j>=0 and arr[i]>arr[j]:
            count+=1
            j-=1
        stock_span_arr.append(count)
    return stock_span_arr      

if __name__ == '__main__':
    # arr = [int(x) for x in input().split()]
    arr = [100,80,60,70,60,75,85]
    stock_span_arr = stock_span(arr)
    print(stock_span_arr)