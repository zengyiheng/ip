import IPy

for i in open('IpList','r'):
    if '/' in i:
        print(IPy.IP(i).strNormal(2))
    else:
        print i

