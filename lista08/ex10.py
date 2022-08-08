def mdc(a, b):
  if not b:
    return a 
  return mdc(b, a % b)


if __name__ == '__main__':
  print(mdc())
