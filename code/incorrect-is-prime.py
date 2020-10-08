def is_prime(n):
  if n in {0, 1}:
    return False
  for i in range(2, int(n ** 0.5)):
    if n % i == 0:
      return False
  return True
