def cavityMap(arr):
    for i in range(1,n-1):
        for j in range(1,n-1):
            if ( arr[i][j]> arr[i-1][j]  and
                arr[i][j]> arr[i+1][j]  and
                arr[i][j]> arr[i][j-1]  and
                arr[i][j]> arr[i][j+1]):
                arr[i][j].replace(arr[i][j],"X")
          
    return arr
