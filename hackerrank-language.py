import sys
if __name__=='__main__':
    s="C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC"
    s=s.split(':')
    n=int(sys.stdin.readline())
    #print s
    for i in range(n):
        a=sys.stdin.readline()
        a=a.split()
        if a[1].strip() in s:
            print 'VALID'
        else:
            print 'INVALID'
