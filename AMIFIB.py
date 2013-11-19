def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def main():
    t=int(input())
    for i in range(t):
        p=int(input())
        q=5*p*p+4
        if is_square(q) or is_square(q-8):
            print "YES"
        else:
            print "NO"
if __name__=='__main__':
    main()
