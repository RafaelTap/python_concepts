name_list = ["rafael", "bruno", "ricardo", "marina", "julia"]

print("<<first name list>>")
for name in name_list:
    print(name)

# inserting new names
name_list.append("rosimery")
name_list.append("ronaldo")
name_list.append("julia")
name_list.append("marcos")
name_list.append("breno")

print("\n<<second name list>>")

for name_1 in name_list:
    print(name_1)

#inserting names in specific positions
name_list.insert(2, "MARIA")
name_list.insert(8, "ROMILDA")
name_list.insert(10, "ROMULO")

print("<<third name list>>")
for name_2 in name_list:
    print(name_2)


