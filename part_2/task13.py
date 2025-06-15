line = input("-->")
upper_case = sum(1 for c in line if c.isupper())
lower_case = sum(1 for c in line if c.islower())
print(f"{lower_case=},{upper_case=}")