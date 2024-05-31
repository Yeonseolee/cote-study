M, N = map(int,input().split())
snack_length = list(map(int,input().split()))
    
start = 1
end = int(1e9)
result = 0

while start <= end:
    c = 0
    
    mid = (start+end)//2

    for snack in snack_length:
        c += snack//mid
        
    if c >= M:
        result = max(mid,result)
        start = mid+1
    elif c < M:
        end = mid -1

print(result)