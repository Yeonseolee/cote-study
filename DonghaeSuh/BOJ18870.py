import collections
N=int(input())
nums=list(map(int,input().split()))
num_dict=collections.defaultdict(int)
sorted_nums=list(set(nums))
sorted_nums.sort()

for i,n in enumerate(sorted_nums):
    num_dict[n]=i

for n in nums:
    print(num_dict[n], end=' ')
