# Lines Finder
The Line Finder function takes a list of points (ex. [[5, 9], [6, 8], [3, 5]]). 
And returns a list of lines that are represented as a dictionary (ex.[{'a': -8, 'b': 4, 'c': -4, 'formatted_line': '-8x + 4y = -4'}, ...]). 
Every element within the returned list is a line that intersects with 3 or more points.   
## Usage

```python
from three_or_more_lines_finder import three_or_more_lines_finder

print(three_or_more_lines_finder([[5, 9], [6, 8], [3, 5]]))  # no lines. 
# []

print(three_or_more_lines_finder([[5, 9], [1, 1], [1, 1]]))  # 2 lines. 
# [{'a': -8, 'b': 4, 'c': -4, 'formatted_line': '-8x + 4y = -4'}, 
# {'a': 0, 'b': 0, 'c': 0, 'formatted_line': '0x + 0y = 0'}]

print(three_or_more_lines_finder([[1, 1], [5, 9], [2, 3]]))  # 3 lines. 
# [{'a': 8, 'b': -4, 'c': 4, 'formatted_line': '8x -4y = 4'}, 
# {'a': -6, 'b': 3, 'c': -3, 'formatted_line': '-6x + 3y = -3'}, 
# {'a': 2, 'b': -1, 'c': 1, 'formatted_line': '2x -1y = 1'}]
```

## License
[MIT](https://choosealicense.com/licenses/mit/)