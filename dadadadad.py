def allsubstrshelper(s, startindex): 
    print s[startindex] 
    for i in range(startindex + 1, len(s)): 
        print(s[startindex:i+1]) 

def allsubstrs(s): 
    for i in range(len(s)): 
        allsubstrshelper(s, i)

def main():
    allsubstrs('abc')
if __name__=='__main__':
    main()
