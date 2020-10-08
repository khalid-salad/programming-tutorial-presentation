biggest = 0
for a in range(100, 1000):
  for b in range(100, 1000):
    prod = a * b
    is_palindrome = True
    s = str(prod)
    n = len(s)
    # check if number is palindrome
    for i in range(n):
      if s[i] != s[n - i - 1]:
        is_palindrome = False
        break
    if not is_palindrome:
      continue
    else:
      if prod > biggest:
        biggest = prod
print(biggest)