def main():
    t=(int)(input())
    for abc in range(t):
        s=raw_input()
        if len(s)<5:
            print "OMG>.< I don't know!"
            continue
        p=s[0:5]
        q=s[-5:]
        if p=='miao.' and q=='lala.':
            print "OMG>.< I don't know!"
        elif p=='miao.':
            print "Rainbow's"
        elif q=='lala.':
            print "Freda's"
        else:
            print "OMG>.< I don't know!"
if __name__=='__main__':
    main()
