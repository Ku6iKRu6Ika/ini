## Installation
Clone the repository:
```
git clone https://github.com/Ku6iKRu6Ika/ini
```

## Quickstart
```python
import ini

content_ini = open('tests/test.ini', 'r').read()
content_dict = {'section' : {'var1' : '1', 'var2' : '2'}}

print(ini.ini_to_dict(content))
print(ini.dict_to_ini(content_dict))
```