# lang-simplification-algorithm
A simple implementation of the Lang simplification algorithm.

## Overview

The Lang algorithm belongs to the family of the line simplification algorithms. More info about it can be found e.g.
[here](http://psimpl.sourceforge.net/lang.html).

The code included in this repository presents a simple implementation of this idea that (hopefully) should work properly
for two-dimensional problems but probably does not handle tricky corner cases, nor is superbly optimised. However, it
does contain a test script (to be run with `pytest`), examples of use (the images - together with a script to generate
them - are included in the [examples](https://github.com/adrzystek/lang-simplification-algorithm/tree/master/examples/)
folder), and a facility to run the program easily via the command line - either directly or with Docker.

## How to use

### directly

Pull the repository, set up the virtual environment (`requirements.txt` is provided) and run ```python main.py```. As
the displayed help message should inform, the program needs a set of parameters to work, here is the exemplary command:
```
python main.py -p 3 5 -p 5 8 -p 10 10 -p 16 9 -p 19 3 -p 26 4 -p 31 7 -p 32 11 -t 5 -l 4
```

### with Docker

Pull the repository and run

```
docker image build --tag lang .
docker container run -it --rm lang
```

As the displayed help message should inform, the program needs a set of parameters to work, here is the exemplary
command:

```
docker container run -it --rm lang -p 3 5 -p 5 8 -p 10 10 -p 16 9 -p 19 3 -p 26 4 -p 31 7 -p 32 11 -t 5 -l 4
```
