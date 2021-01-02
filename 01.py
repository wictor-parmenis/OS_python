import os

# apath = str(input('Insert a path here: '))
path_search = '/Users/WICTOR/Downloads/Compra de ações'
# print(path_search)
item = 'VID'

for root, directories, arquives in os.walk(path_search):
    for arquive in arquives:
        complete_path = os.path.join(root, arquive)
        print(complete_path)