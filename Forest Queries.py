import sys, os, bisect, heapq, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(0) 
inf = 10**18
mod = 1000000007 

if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def get_int(): 
    return int(sys.stdin.readline())

def get_ints(): 
    return map(int, sys.stdin.readline().split())

def get_list(): 
    return list(map(int, sys.stdin.readline().split()))

def get_string(): 
    return sys.stdin.readline().rstrip()

def get_words(): 
    return sys.stdin.readline().split()

def fast_print(ans):
    sys.stdout.write(str(ans) + '\n')

def print_list(arr):
    sys.stdout.write(" ".join(map(str, arr)) + '\n')

def solve():
    n, q = get_ints()
    
    # a 2D prefix sum array with dimensions (n+1) x (n+1)
    # Using 1-based indexing for bounds handling
    P = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Reading the grid and building the prefix sum array
    for i in range(1, n + 1):
        row = get_string()
        for j in range(1, n + 1):
            # 1 if there's a tree ('*'), 0 if it's empty ('.')
            val = 1 if row[j - 1] == '*' else 0
            
            # 2D Prefix sum formula
            P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + val
            
    # Processing each query
    for _ in range(q):
        y1, x1, y2, x2 = get_ints()
        ans = P[y2][x2] - P[y1 - 1][x2] - P[y2][x1 - 1] + P[y1 - 1][x1 - 1]
        
        fast_print(ans)

if __name__ == '__main__':
    # multiple test cases
    # t = get_int()
    # for _ in range(t):
    #     solve()
    
    # single test case
    solve()