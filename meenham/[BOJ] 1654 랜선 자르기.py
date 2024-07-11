K, N = map(int,input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end:
    
    mid = (start+end)//2
    
    k = 0
    for line in lines:
        k += line//mid
    
    if start == end and k < N:
        start -= 1
        break
    
    if k > N:
        if start == mid and start == end:
            break
        elif start == mid and start < end:
            start += 1
        else:
            start = mid
            
    elif k == N:
        if start == mid and start == end:
            break 
        elif start == mid and start < end:
            start += 1            
        else:
            start = mid

        
    if k < N:
        end = mid - 1
        

print(start)
    

    