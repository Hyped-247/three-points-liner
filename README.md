# Lines Finder
The get_lines_intersect_three_or_more_points function takes a list of points (ex. [[5, 9], [6, 8], [3, 5]]). 
And returns a list of dictionaries (ex.[{'a': -8, 'b': 4, 'c': -4, 'formatted_line': '-8x + 4y = -4'}, ...])
Each element within the returned list is a line that intersects with 3 or more points.   
## Usage

```python
from lines_finder import get_lines_intersect_three_or_more_points

print(get_lines_intersect_three_or_more_points([[5, 9], [6, 8], [3, 5]]))  # no lines. 
# []

print(get_lines_intersect_three_or_more_points([[5, 9], [1, 1], [1, 1]]))  # 2 lines. 
# [{'a': -8, 'b': 4, 'c': -4, 'formatted_line': '-8x + 4y = -4'}, 
# {'a': 0, 'b': 0, 'c': 0, 'formatted_line': '0x + 0y = 0'}]

print(get_lines_intersect_three_or_more_points([[1, 1], [5, 9], [2, 3], [2, 3]]))  # 3 lines. 
# [{'a': 8, 'b': -4, 'c': 4, 'formatted_line': '8x -4y = 4'}, 
# {'a': -6, 'b': 3, 'c': -3, 'formatted_line': '-6x + 3y = -3'}, 
# {'a': 2, 'b': -1, 'c': 1, 'formatted_line': '2x -1y = 1'}]
```

  '-8x + 4y = -4' => 4y = 8x - 4 => 2x - 1 => (m, c) / (2, -1)
  '-4x + 2y = -2' => 2y = 4x - 2 => 2x - 1 => (m, c) / (2, -1)  

# 

# [ [1, 1], [5, 9], [2, 3], [2, 5] ]

==> 
def colinear(p1, p2, p3):
   







## License
[MIT](https://choosealicense.com/licenses/mit/)