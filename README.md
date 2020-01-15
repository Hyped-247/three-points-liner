# Lines Finder
The LinesFinder class takes a list of point objects (ex. [Point(1, 2), Point(1, 3), Point(1, 4)]) as an input, 
and computes a distinct list of lines that intersect with 3 or more 
points from the input set (ex. ['y = 2.0x + -1.0', 'x = 1.0']). 


## Usage
```python
from lines_finder.lines_finder import LinesFinder
from point.point import Point

print("No lines")
points = [Point(5, 9), Point(6, 8), Point(3, 5), Point(3, 5), Point(3, 5)]  # no lines.

lines_finder_obj = LinesFinder(points)
print([res.get_line_tuple() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# []
print([res.get_line_str() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# []
print([res.get_line_dict() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# []
print("................................................................................")

print("One lines")
points = [Point(1, 2), Point(1, 3), Point(1, 4)]  # one line.

lines_finder_obj = LinesFinder(points)
print([res.get_line_tuple() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# [(True, 1.0, None)]
print([res.get_line_str() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# ['x = 1.0']
print([res.get_line_dict() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# [{'x': 1.0}]
print("................................................................................")


print("Two lines")
points = [Point(1, 2), Point(1, 3), Point(1, 4),  # two lines
          Point(1, 7), Point(2, 3), Point(5, 9), Point(0, -1)]

lines_finder_obj = LinesFinder(points)
print([res.get_line_tuple() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# [(False, 2.0, -1.0), (True, 1.0, None)]
print([res.get_line_str() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# ['y = 2.0x + -1.0', 'x = 1.0']
print([res.get_line_dict() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# [{'y': 2.0, 'x': -1.0}, {'x': 1.0}]
print("................................................................................")


print("Three lines")
points = [Point(1, 2, ), Point(1, 3), Point(1, 4), Point(1, 7),  # three lines.
          Point(2, 3), Point(5, 9), Point(0, -1), Point(0.5, 0),
          Point(1, 1), Point(10, 10), Point(-4, -4)]

lines_finder_obj = LinesFinder(points)
print([res.get_line_tuple() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# [(False, 1.0, 0.0), (False, 2.0, -1.0), (True, 1.0, None)]
print([res.get_line_str() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# ['y = 1.0x + 0.0', 'y = 2.0x + -1.0', 'x = 1.0']
print([res.get_line_dict() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# [{'y': 1.0, 'x': 0.0}, {'y': 2.0, 'x': -1.0}, {'x': 1.0}]
print("................................................................................")


print("Four lines")
points = [Point(1, 2), Point(1, 3), Point(1, 4), Point(1, 7),  # four lines.
          Point(2, 3), Point(5, 9), Point(0, -1), Point(0.5, 0),
          Point(1, 1), Point(3, 3), Point(-4, -4), Point(-4, -4), Point(-4, -4)]

lines_finder_obj = LinesFinder(points)
print([res.get_line_tuple() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# [(False, 1.0, 0.0), (False, 2.0, -1.0), (False, -0.0, 3.0), (True, 1.0, None)]
print([res.get_line_str() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# ['y = 1.0x + 0.0', 'y = 2.0x + -1.0', 'y = -0.0x + 3.0', 'x = 1.0']
print([res.get_line_dict() for res in lines_finder_obj.get_lines_intersect_three_or_more_points()])
# [{'y': 1.0, 'x': 0.0}, {'y': 2.0, 'x': -1.0}, {'y': -0.0, 'x': 3.0}, {'x': 1.0}]
print("................................................................................")

```

# Project Structure
``` 
├── lines_finder 
    ├── line
    │   ├── __init__.py
    │   └── line.py
    ├── lines_finder
    │   ├── __init__.py
    │   └── lines_finder.py
    ├── point
    │   ├── __init__.py
    │   └── point.py
    ├── tests
    │   ├── __init__.py
    │   ├── line
    │   │   ├── __init__.py
    │   │   └── test_line.py
    │   ├── lines_finder
    │   │   ├── __init__.py
    │   │   └── test_lines_finder.py
    │   └── point
    │       ├── __init__.py
    │       └── test_point.py
    ├── LICENSE.md
    ├── README.md
```
Let me explain what each directory does:  
* lines_finder 
    * This dir contains the LinesFinder class. This class contains a method called:  
get_lines_intersect_three_or_more_points. This method returns a distinct list 
of Line objects that intersect with 3 or more points from the input set.  

* point
    * The point dir contains the Point class. This class is going to store, and validate the X, Y input points.

* line
    * The line dir contains the Line class. This class is going to compute, validate, and format Line objects.

* tests
    * This dir contains tests that cover %100 of the code base. Every test 
file tests a single python module. To know what each file is testing, simply 
look at what follows test_. For example, test_lines_finder.py ensures that 
lines_finder.py is working correctly. This naming convention makes it easy to know what each test is testing.   

 

## Built With

* [Python 3.7](https://www.python.org) 


## Author

* **Mohammad Mahjoub** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

