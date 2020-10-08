def qs(a):
  if len(a) <= 1:
    return a
  else:
    x, z = [], []
    y = a[0]
    for p in a:
      if p < y:
        x.append(p)
      else:
        z.append(p)
    return qs(x) + qs(z)
