print("Ulam's")
m,n=10,10
matrix = [[0 for i in range(m)]for i in range(n)]
dir = (1,0); mod = 1; o = (m/2, n/2); start = 1;

while (o[0] < m and o[1] < n):
    end = o + dir
    start +=1