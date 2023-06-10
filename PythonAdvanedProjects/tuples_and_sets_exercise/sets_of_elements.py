n, m = [int(x) for x in input().split()]
n_set = {int(input()) for x in range(n)}
m_set = {int(input()) for y in range(m)}
print(*n_set.intersection(m_set), sep="\n")
