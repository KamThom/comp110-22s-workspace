"""Learning the dict function."""

schools: dict[str, int] = dict()

# Key-value pairing 
schools['UNC'] = 29400
schools['Duke'] = 15002
schools['Davis'] = 74392

print(schools)
print(f"UNC has {schools['UNC']} students")  # lookup

# schools.pop('Duke')

if'Duke' in schools:
    print('Duke is present')
else:
    print('Duke not present')

schools['UNC'] = 20000
schools['Duke'] += 12673
schools['Davis'] -= 172

schools = {}  # emptying dict
print(schools)
schools = {'UNC': 13845, 'Duke': 18278, 'Davis': 18329}  # asssigning new key value pairs
print(schools)

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")