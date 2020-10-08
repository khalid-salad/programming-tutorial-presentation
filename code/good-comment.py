def is_prime(n):
  if n == 1:
    return False
  elif n in {2, 3}:
    return True
  elif n % 2 == 0:
    return False
  else:  
    # we need only check for odd factors
    # up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
      if n % i == 0:
        return False
    return True
