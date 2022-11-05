from urllib.request import urlopen
from re import compile, finditer
from os import remove


html = urlopen('https://pypi.org/simple/').read().decode('utf-8')
pattern = compile(r'>([^<]+)</a>')
all_packages = [match[1] for match in finditer(pattern, html)]
print(f'Found {len(all_packages):,} packages\n')

remove('requirements.txt')
file = open('requirements.txt', 'w')
for package in all_packages:
    file.write(package + '\n')
file.close()