import math


def merge(src, dest, start, end):
    boundary1 = start + end
    boundary2 = min(start+ 2*end, len(src))
    idx_run1, idx_run2, idx_dest = start, start + end, start
    while idx_run1 < boundary1 and idx_run2 < boundary2:
        if src[idx_run1] < src[idx_run2]:
            dest[idx_dest] = src[idx_run1]
            idx_run1 += 1
        else:
            dest[idx_dest] = src[idx_run2]
            idx_run2 += 1
        idx_dest += 1
        if idx_run1 < boundary1:
            dest[idx_dest:boundary2] = src[idx_run1:boundary1]
        elif idx_run2 < boundary2:
            dest[idx_dest:boundary2] = src[idx_run2:boundary2]
            
def merge_sort(L):
    n = len(L)
    # creating runs of logarithmic length starting in 2,4,8...
    log_n = math.ceil(math.log(n,2))
    src, dest = L, [None]*n
    for i in (2**k for k in range(log_n)):
        for j in range(0, n, 2*i):
            merge(src, dest, j, i)
        # reverse roles    
        src, dest = dest, src
    if L is not src:
        L[0:n] = src[0:n]