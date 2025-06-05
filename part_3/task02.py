import pprint
file = open("part_3/files/data.txt", 'r')
content = file.read()
content = content.split()

dict = {i:content.count(i) for i in content}
pprint.pprint(dict)
file.close()