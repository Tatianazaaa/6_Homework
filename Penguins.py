#Пингвины

n = 4
a = '   _~_    '
b = '  (o o)   '
c = ' /  V  \  '
d = '/(  _  )\ '
e = '  ^^ ^^   '
line = [a,b,c,d,e]
with open('penguins.txt', 'r') as p:
    pr = p.read()
    print((pr*int(n)))


