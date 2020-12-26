def min_swap(s, n):
    s = list(s)
    count = 0
    if s == s[::-1]:
        return 0
    else:
        for i in range(n // 2):
            left = i
            right = n - i - 1
            while left < right:
                if s[left] == s[right]:
                    break
                else:
                    right -= 1

            if left == right:
                return -1
            else:
                for j in range(right, n-left-1):
                    (s[j], s[j+1]) = (s[j+1], s[j])
                    count += 1

        return count

string = input()
n = len(string)
print(min_swap(string,n))