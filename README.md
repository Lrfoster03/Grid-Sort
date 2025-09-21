# Grid-Sort

Ever wondered how to sort points from top left to top right? This repository contains the code required to just that!

## Testing

Run the unit tests with the Python interpreter used in this environment. For many macOS setups use:

```
/usr/local/bin/python3 -m unittest tests.test_sort -v
```

Or discover all tests:

```
/usr/local/bin/python3 -m unittest discover -v
```

The repo includes `tests/test_sort.py` which covers the core behaviors of `sort.py`.

### Installation

To install the package in editable mode, run the following command in your terminal:

```
pip install -e .
```

### Example Usage

```python
from grid_sort import sort_by_xy, get_xy, set_xy
# Example usage
points = [...]  # your points here
sorted_points = sort_by_xy(points)
```

## Code Overview

The main functionality is in `sort.py`, which provides functions to sort objects based on their X and Y coordinates. The sorting logic considers a threshold to determine when to switch from sorting by Y to sorting by X.
Key functions include:

- `get_xy(obj)`: Retrieves the X and Y coordinates from an object.
- `set_xy(obj, x, y)`: Sets the X and Y coordinates on an
  object.
- `sort_by_xy(objs, threshold=2.0)`: Sorts a list of objects based on their coordinates, using a specified threshold to determine sorting behavior.
- `point_line_distance(x0, y0, x1, y1, x2, y2)`: Calculates the perpendicular distance from a point to a line segment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Acknowledgements

Thanks to all contributors and users who have provided feedback and improvements.

## Contact

For questions or suggestions, please open an issue on GitHub or contact the maintainer directly.
