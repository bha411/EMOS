def can_defeat_all(N, H, A, X):
    for j in range(N):
        if A[j] <= X:
            continue
        elif H > A[j]:
            H -= A[j]
        else:
            return False
    return True


def min_resistance(T, test_cases):
    results = []
    for i in range(T):
        N, H, A = test_cases[i]

        left = 0
        right = max(A)
        min_resistance = float('inf')

        while left <= right:
            mid = (left + right) // 2
            if can_defeat_all(N, H, A, mid):
                min_resistance = min(min_resistance, mid)
                right = mid - 1
            else:
                left = mid + 1

        results.append(min_resistance)

    return results


T = int(input())
test_cases = []
for _ in range(T):
    N, H = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append((N, H, A))

results = min_resistance(T, test_cases)
for result in results:
    print(result)
