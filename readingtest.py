fo=open('C:\Users\SONU\Desktop\garbled_email_dictionary.txt','rt')
a=fo.readline()
while a:
    if a[0]=='a':
        print a
        a=fo.readline()
fo.close()
