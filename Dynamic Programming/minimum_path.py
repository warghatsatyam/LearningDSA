def minimum_path(i,j,arr):
    n = len(arr)
    m = len(arr[0])

    if i>=n:
        return float('inf')
    if j>=m:
        return float('inf')
    if i==n-1 and j==m-1:
        return arr[i][j]
    curr_cost = arr[i][j]
    return curr_cost + min(minimum_path(i+1,j,arr), minimum_path(i+1,j+1,arr),minimum_path(i,j+1,arr))


if __name__ == '__main__':
    arr = [[9,6,0,12,90,1],[2,7,8,5,78,6],[1,6,0,5,10,-4],[9,6,2,-10,7,4],[10,-2,0,5,5,7]]
    ans = minimum_path(0,0,arr)
    print(ans)