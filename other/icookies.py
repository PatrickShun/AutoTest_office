f = open(r'icookies.txt')

cookies = {}

for i in f.read().split(';'):
	name,value = i.strip().split('=',1)
	cookies[name] = value

print(cookies)