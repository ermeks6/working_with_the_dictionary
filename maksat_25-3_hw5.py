data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []
for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)


x = 0
operators = {}
while len(operators) != len(designations):
    operators[designations[x]] = {codes[x]}
    x += 1

operators.pop('Katel')
operators.pop('Fonex')

operators['O!'] = ['0705', '0700', '0500']
operators['Megacom'] = ['0550', '0999', '0555']
operators['Beeline'] = ['0770', '0222', '0777']

for key, value in operators.items():
  print("{0}: {1}".format(key,value))



