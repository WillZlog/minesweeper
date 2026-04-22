# Mine Sweeper

See the full analysis here: [View Results](results.md)

## Table of Contents

- [Mine Sweeper](#mine-sweeper)
  - [Table of Contents](#table-of-contents)
  - [About ](#about-)
  - [Getting Started ](#getting-started-)
    - [Prerequisites](#prerequisites)
  - [Usage ](#usage-)
  - [Testing ](#testing-)

## About <a name = "about"></a>

I made a bot that guesses mine sweeper boards, by using sets, lists, and dicts. see the comments in the code for more info

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You don't need to pip install anything as all packages come built in to the Python Standard Library

``` 
csv, random, time, datetime, typing
```

## Usage <a name = "usage"></a>

Use it to test bots, and run tests yk.

## Testing <a name = "testing"></a>

in order to run tests, make sure pytest in installed and run 
```
pytest
```

if that fails try

```
python3 -m pytest
```

the two tests that exist right now are: 
* test_smartishBot() which tests if smartishBot() works with 0 mines,
* and test_randomBot() which tests if randomBot() works with 0 mines 

tests live inside tests/