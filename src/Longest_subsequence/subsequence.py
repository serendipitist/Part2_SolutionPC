# Longest common subsequence
# However we can't do better than O(n^2) for solving first part because in worst number of subarrays with equal no of 0s and 1s
# could be proportional to n^2.

one_count = 0
zero_count = 0
max_len = 0
end = -1; 
f = open("input.txt", "r")
a = [1, 1, 0, 1, 0, 0, 0]
list = map(int, f.readline(1).strip().split(' '))


def MaximalSubSeq(a):
    countOne = 0
    countZero = 0
    for i in range(0, len(a)):
        if a[i] == 1:
            countOne = countOne + 1
        else:
            countZero = countZero + 1
    return 2 * min(countZero, countOne);


pos = MaximalSubSeq(a)
print "possible subsequence", a[:pos]




             
    

        
