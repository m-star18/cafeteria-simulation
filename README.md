# cafeteria-simulation

Python package for cafeteria simulation

![Python package](https://github.com/m-star18/cafeteria-simulation/workflows/Python%20package/badge.svg)
[![Github issues](https://img.shields.io/github/issues/m-star18/cafeteria-simulation)](https://github.com/m-star18/cafeteria-simulation/issues)
[![Github license](https://img.shields.io/github/license/m-star18/cafeteria-simulation)](https://github.com/m-star18/cafeteria-simulation/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cafeteria-simulation.

```bash
pip install cafeteria-simulation
```

## Usage

The easiest simulation to perform

```python
from cafe import Cafeteria, TOYOTA


TIME = 300

env = Cafeteria(TOYOTA.data, TIME)
for _ in range(TIME):
    env.run([])

# A graph showing the change in scores
env.show()
```

You can specify it by assigning the coordinates [table number, seat number] to run().

Also, you can refer to the number of people in group_member up to 10 groups.

### Sample

- [greedy.py](https://github.com/m-star18/cafeteria-simulation/blob/master/sample/greedy.py)
- [basic.py](https://github.com/m-star18/cafeteria-simulation/blob/master/sample/basic.py)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contributors

- [m-star18](https://github.com/m-star18)

## License

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
