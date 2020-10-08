def is_palindrome(num):
  s = str(num)
  n = len(s)
  for i in range(n):
    if s[i] != s[n - i - 1]:
      return False
  return True

def main():
  biggest = 0
  for a in range(100, 1000):
    for b in range(100, 1000):
      if is_palindrome(a * b):
        biggest = max(biggest, a * b)
  print(biggest)

if __name__ == "__main__":
    main()