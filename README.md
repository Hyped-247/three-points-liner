# Lines Finder
The LinesFinder class takes a list of non duplicate points (ex. [[1, 2], [1, 3], [1, 4], [1, 7], [2, 3], [5, 9], [0, -1]]) as an input, 
and computes a distinct list of lines that intersect with 3 or more 
points from the input set (ex. ['y = 2.0x + -1.0', 'x = 1.0']). In the future, we might 
implement other methods (ex. get_lines_given_triangle) within the LinesFinder class. But for now, 
we only have one method.  


## Usage
Examples of valid inputs
```python
from lines_finder.lines_finder import LinesFinder

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
Examples of invalid inputs
```python
from lines_finder.lines_finder import LinesFinder

lines_finder_obj = LinesFinder([[1, 2], [1, 3]])  # need three points.
print(lines_finder_obj.get_lines_intersect_three_or_more_points())
# [] 

lines_finder_obj = LinesFinder([[1, 2], [1, 3], [1, 3]])  # cannot have duplicates.
print(lines_finder_obj.get_lines_intersect_three_or_more_points())
# TypeError: Duplicate points are not allowed.


lines_finder_obj = LinesFinder([[1, 1], [1, 2], [1], [1, 4]])  # must have two numbers within list.
print(lines_finder_obj.get_lines_intersect_three_or_more_points())
# TypeError: Each list of points must contain two numbers.


lines_finder_obj = LinesFinder([[1, 1], [1, 2], [1, '2'], [1, 4]])  # type must be int or float.
print(lines_finder_obj.get_lines_intersect_three_or_more_points())
# TypeError: The points list must contain float or int.
```

# Project Structure
``` 
lines_finder/
    ├── lines_finder/
        ├── __init__.py
        ├── lines_finder.py
    ├── tests/
        ├── __init__.py
        ├── lines_finder/
        |   ├── __init__.py
        |   ├── test_lines_finder.py
        ├── utilities/
        |   ├── __init__.py
        |   ├── test_compute_line.py
        |   ├── test_format.py
        |   ├── test_validator.py
    ├── utilities/
    |   ├── __init__.py
    |   ├── compute_line.py
    |   ├── format.py
    |   ├── validator.py
    ├── README.md
    └── LICENSE.md
```
Let me explain what each directory does:  
* lines_finder 
    * This dir contains the LinesFinder class. This class contains a method called:  
get_lines_intersect_three_or_more_points. This method returns a distinct list 
of lines that intersect with 3 or more points from the input set.  

* tests
    * This dir contains tests that cover %100 of the code base. Every test 
file tests a single python module. To know what each file is testing, simply 
look at what follows test_. For example, test_lines_finder.py ensures that 
lines_finder.py is working correctly. This naming convention makes it easy to know what each test is testing.   

* utilities
    * This dir contains helper functions. These helper functions are placed in three different python files. 
    First, compute_line.py contains functions that will help the LinesFinder class preform mathematical operations. 
    Second, format.py contains a single function called: format_line_str. This function formats lines. The reason why 
    it is called format_line_str instead of format_line is because we might add more functions to
    this file (ex. format_line_tuple, format_line_dict, etc). Finally, we have validator.py. This file contains functions that will validate the points. 

## Built With

* [Python 3.7](https://www.python.org) 


## Author

* **Mohammad Mahjoub** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

