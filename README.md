![W][W]![O][O]![R][R]![D][D]  
![P][P]![L][L]![A][A]![Y][Y]

---
A hands on project to build a wordplay solver with a web service API

# Contents
- [Overview](#overview)
- [Dev Environment Setup](#devsetup)
  - [Pipenv Setup](#pipenv)
  - [Alternative: Python `venv` and Pip](#venv_pip)
  - [Verify Flask](#verify_flask)
- [Development Milestones](#milestones)

<a name="overview"></a>

# Overview

This project provides an opportunity for the aspiring Pythonista to get hands-on experience with some of common tools used in the Python development ecosystem.  

Libraries and tools used include: 
- [PyTest](https://docs.pytest.org/en/latest/)
- [Flask](http://flask.pocoo.org/)
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [Git](https://git-scm.com/) and [GitHub](https://github.com/)

Our goal is to build a web service with a few endpoints all revolving around a wordplay solver theme:

| Endpoint URL | HTTP Verb | Description |
|--------------|-----------|-------------|
| /api/score?l={letters} | GET | Returns the scrabble score of the letters
| /api/word/{word} | GET | Returns whether word is in lexicon and scrabble score
| /api/matches/{letters} | GET | Performs word matching in lexicon, sorted by scrabble score

## Letter Scoring

Default scoring is to be calculated using Scrabble letter point values.

| Point Value | Letters                      |
|-------------|------------------------------|
| 1           | A, E, I, L, N, O, R, S, T, U |
| 2           | D, G                         |
| 3           | B, C, M, P                   |
| 4           | F, H, V, W, Y                |
| 5           | K                            |
| 8           | J, X                         |
| 10          | Q, Z                         |

<a name="devsetup"></a>
# Dev Environment Setup

This project makes use of third-party packages that do not ship with Python standard library.  It is recommended a [Python virtual environment][about_python_virtualenv] be configured to prevent the installed packages from conflicting with other Python projects on the host machine.

I recommend starting with `pipenv` and falling back to alternative tools if needed. Pipenv is a convenience tool that facilitates both managing a virtual environment as well as installing packages.  Its usage is consistent across Windows and unix systems.

Alternernatively the virtual environment and packages can be configured separatetly using the Python `venv` library and the `pip` tool.

<a name="pipenv"></a>
## Set Up Using `pipenv`

The `pipenv` tool serves 2 roles: 
1) creating and "activating" a virtual environment
2) installing 3rd party packages

Pipenv does not ship with Python and needs to be installed from the command line using pip (a.k.a. `pip3`).

_*The following commands need to be run from your command line shell.*_

    pip3 install pipenv

Activate the virtual environment from within the repo directory:

    # change to the project directory you cloned
    cd wordplay
    pipenv shell

Install the 3rd party packages:

    pipenv install --dev

This will install Flask and PyTest libraries.

Confirm `pytest` is available by running the following from the command line:

    pytest .

<a name="venv_pip"></a>
## Alternative Set Up: Python `venv` and Pip

Change into the project directory you cloned and create a new virtual environment using the `venv` library:

    # change to the project directory you cloned
    cd wordplay
    python3 -m venv venv

Activate the virtual environment.

- On Windows:

    venv\Scripts\activate.bat

- On Mac/Linux

    source venv/bin/activate

Install the 3rd party packages using `pip3`

    pip3 install -r requirements.txt

Try running the tests:

    pytest .

<a name="verify_flask"></a>
## Verify Flask

Verify Flask launches:

    python3 app.py

Open your browser to http://127.0.0.1:5000/


<a name="milestones"></a>
# Milestones

1) Set up your developer environment.  Confirm Flask and PyTest are installed
2) Edit `wordplay.py` and get `score_word()` functional so that the tests pass.
3) Play with Flask.  Try modifying the `/` URL to load from a template instead of the hardcoded response string.
4) Write a function to read in the lexicon file `sowpods.txt` and return the contents as a list.  
  The loader function should skip any empty lines or lines that start with `#`
  The words should be converted to lowercase.  
5) ...

[W]: readme_assets/letter_tile_w.jpg
[O]: readme_assets/letter_tile_o.jpg
[R]: readme_assets/letter_tile_r.jpg
[D]: readme_assets/letter_tile_d.jpg  
[P]: readme_assets/letter_tile_p.jpg
[L]: readme_assets/letter_tile_l.jpg
[A]: readme_assets/letter_tile_a.jpg
[Y]: readme_assets/letter_tile_y.jpg

[about_python_virtualenv]: https://docs.python.org/3/tutorial/venv.html
