'''What will be te length of following set as:
s = set()
s.add(20)
s.add(20.0)
s.add('20')'''

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(s)
print(len(s)) # From output we can see that int == float in sets

