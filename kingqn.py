def main():
    t=(int)(input())
    vowel=['a','e','i','o','u']
    for abc in range(t):
        s=raw_input()
        if s[-1]=='y':
            print 'Case #'+str(abc+1)+': '+s+' is ruled by nobody.'
        elif s[-1] not in vowel:
            print 'Case #'+str(abc+1)+': '+s+' is ruled by a king.'
        else:
            print 'Case #'+str(abc+1)+': '+s+' is ruled by a queen.'
if __name__=='__main__':
    main()
