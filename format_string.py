# получить строку вида 'switchport trunk allowed vlan 1,3,10,20,30,100'
vlan = ['1','2','3','10','20','30','100']
string = 'switchport trunk allowed vlan {}'
vlans = ','.join(vlan)
config = string.format(vlans)
print(config)


# получить строку вида ['1', '3', '8']
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
command1 = set(command1)
command2 = set(command2)
command3 = sorted(list(command1.intersection(command2)))
print(command3[2:5])


# получить строку вида ['1', '3', '10', '20', '30', '100']
conf = 'switchport trunk allowed vlan 1,3,10,20,30,100'
conf = conf.split()
conf = conf[-1].split(',')
print(conf)
#conf.reverse()
