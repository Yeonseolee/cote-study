N = int(input())

index_list = [ 1, 2, 3 ]
def function(num, start, end):
    if num > 1:
        for index in index_list:
            if index != start and index != end:
                index_left = index
        return function(num-1,start,index_left) + [(start,end)] + function(num-1,index_left,end)
    else:
        return [(start,end)]

answer = function(N,1,3)

print(len(answer))
for ans in answer:  
    print(ans[0],ans[1])