# Lines Finder
The LinesFinder class takes a list of three or more 
 non duplicate points (ex. [[1, 2], [1, 3], [1, 4]]). And returns a list of lines that intersects with 3 or more points 
(ex.['y = 2.0x + -1.0', 'x = 1.0', ...]). 

## Usage

```python
from lines_finder import LinesFinder

# Construct an object 
lines_finder_obj = LinesFinder([[5, 9], [6, 8], [3, 5]])

print(lines_finder_obj.get_lines_intersect_three_or_more_points())  # no lines.
# []

lines_finder_obj = LinesFinder([[1, 2], [1, 3], [1, 4]])

print(lines_finder_obj.get_lines_intersect_three_or_more_points())  # one line.
# ['x = 1.0']

lines_finder_obj = LinesFinder([[1, 2], [1, 3], [1, 4], [1, 7], [2, 3], [5, 9], [0, -1]])
print(lines_finder_obj.get_lines_intersect_three_or_more_points())  # two line.
# ['y = 2.0x + -1.0', 'x = 1.0']

lines_finder_obj = LinesFinder([[1, 2], [1, 3], [1, 4], [1, 7],  # three lines.
                                                [2, 3], [5, 9], [0, -1], [0.5, 0],
                                                [1, 1], [10, 10], [-4, -4]])
print(lines_finder_obj.get_lines_intersect_three_or_more_points()) 
# ['y = 1.0x + -0.0', 'y = 2.0x + -1.0', 'x = 1.0']
 
lines_finder_obj = LinesFinder([[1, 2], [1, 3], [1, 4], [1, 7],  # four lines.
                                                [2, 3], [5, 9], [0, -1], [0.5, 0],
                                                [1, 1], [3, 3], [-4, -4]])
print(lines_finder_obj.get_lines_intersect_three_or_more_points()) 
# ['y = 1.0x + -0.0', 'y = 2.0x + -1.0', 'y = -0.0x + 3.0', 'x = 1.0']
 
```

# Project Structure
``` 
lines_finder/
    ├── tests/
    |   ├── __init__.py
    |   ├── test_lines_finder.py
        ├── utilities/
        |   ├── test_compute_line.py
        |   ├── test_format.py
        |   ├── test_validator.py
    ├── utilities/
    |   ├── __init__.py
    |   ├── compute_line.py
    |   ├── format.py
    |   ├── validator.py
    ├── README.md
    └── lines_finder.py
```
