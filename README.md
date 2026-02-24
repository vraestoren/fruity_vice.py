# fruity_vice.py
Web-API for [fruityvice.com](https://www.fruityvice.com) powerful webservice which provides data for all kinds of fruit! 

## Example
```python
from fruity_vice import FruityVice

fruity_vice = FruityVice()
fruits = fruity_vice.get_all_fruits()
print(fruits)
```
