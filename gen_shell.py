import string
import random

def print_str(s):
	# print with green color
	print("\033[92m[+]",s,"\033[0m")

with open('./basic_rev.txt', 'r') as f:
	data = f.read()

print_str("Opening file...")
print_str("Got an original data:")
print(data)
print()
print_str("Injecting spaces...")

inject_space = ""
for i in data:
	if i == ' ':
		inject_space = inject_space + ' ' * random.randint(1, 5)
	inject_space = inject_space + i

print(inject_space)
print()

var_next = [" ", ";", ".", "`", "{", "}", "(", ")", ","]
flag = False
var_list = []

for i in inject_space:
	if i == '$':
		flag = True
		var = ""
	elif flag == True and i in var_next:
		flag = False
		var_list.append(var)
	elif flag == True:
		var = var + i

filtered_var = [word for word in var_list if word[0].isupper()]
unique_var = list(set(filtered_var))

print_str("Got variables to mass:")
print(unique_var)
print()

characters = string.ascii_letters + string.digits
mass_var = inject_space

for i in unique_var:
	mass = ''.join(random.choice(characters) for _ in range(random.randint(10, 20)))
	mass_var = mass_var.replace("$" + i, "$" + mass)

print_str("Mass variables:")
print(mass_var)
print()

print_str("Writing to file...")
with open('./mass_rev.txt', 'w') as f:
	f.write(mass_var)
print_str("Success to write file: ./mass_rev.txt")
