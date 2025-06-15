cases = {
    'Василий': 'Олег',
    'Василия': 'Олега',
    'Василию': 'Олегу',
    'Василием': 'Олегом',
    'Василии': 'Олеге'
}

with open('in.txt', 'r') as f:
    text = f.read()

for old_name, new_name in cases.items():
    text = text.replace(old_name, new_name)

with open('./files/out.txt', 'w') as f:
    f.write(text)