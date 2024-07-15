"""
Создать папку, внутри ещё несколько папок, внутри файлы. И вывести дерево каталогов.
folder
    file1.txt
    subfolder
        2.txt
        3.txt
    subfolder2
"""

import os

path = os.getcwd() + '/modules/'

for root, dirs, files in os.walk(path):
    level = root.replace(path, '').count(os.sep)
    indent = ' ' * 4 * (level)
    print(f"{indent}{os.path.basename(root)}/")
    sub_indent = ' ' * 4 * (level + 1)
    for file in files:
        print(f"{sub_indent}{file}")