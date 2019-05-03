![W][W]![O][O]![R][R]![D][D]![P][P]![L][L]![A][A]![Y][Y]

---
A hands on project to build a wordplay solver with a web service API

# Contents

- [Contents](#contents)
- [Overview](#overview)
  - [Letter Scoring](#letter-scoring)
- [Dev Environment Setup](#dev-environment-setup)
  - [Set Up with Python `venv` and `pip`](#set-up-with-python-venv-and-pip)
      - [Windows](#windows)
      - [Mac/Linux](#maclinux)
  - [Alternative Set Up with `pipenv`](#alternative-set-up-with-pipenv)
  - [Verify Pytest](#verify-pytest)
  - [Verify Flask](#verify-flask)
- [Development Milestones](#development-milestones)

# Overview

This project provides an opportunity to get hands-on experience with some of common tools used in the Python development ecosystem.  

Libraries and tools used include: 
- [PyTest](https://docs.pytest.org/)
- [Flask](http://flask.pocoo.org/)
- [Venv library][venv] and [pip][pip_tool] with virtual environments
- [Pipenv][pipenv]
- [Git](https://git-scm.com/) and [GitHub](https://github.com/)

Our goal is to build a web service with a few endpoints all revolving around a wordplay solver theme:

| Endpoint URL              | HTTP Verb | Description                                                      |
| ------------------------- | --------- | ---------------------------------------------------------------- |
| /api/v1/score?l={letters} | GET       | Returns the scrabble score of the letters                        |
| /api/v1/word/{word}       | GET       | Returns whether word is in lexicon and scrabble score            |
| /api/v1/word/{word}       | POST      | *Optional:* Adds a new word to the lexicon                       |
| /api/v1/matches/{letters} | GET       | Performs word matching against lexicon, sorted by scrabble score |

## Letter Scoring

Default scoring is to be calculated using Scrabble letter point values.

| Point Value | Letters                      |
| ----------- | ---------------------------- |
| 1           | A, E, I, L, N, O, R, S, T, U |
| 2           | D, G                         |
| 3           | B, C, M, P                   |
| 4           | F, H, V, W, Y                |
| 5           | K                            |
| 8           | J, X                         |
| 10          | Q, Z                         |


# Dev Environment Setup

Additional instructions are available for configuring development editors:
- [VS Code instructions][vs_code_setup]
- [PyCharm instructions][pycharm_setup]

This project makes use of third-party packages that do not ship with Python standard library.  It is recommended a [Python virtual environment][venv] be configured to prevent the installed packages from conflicting with other Python projects on the host machine.

I recommend managing the virtual environment using the tools that come with Python 3 (the `venv` library and `pip` tool).  This is the workflow most other tutorials use, so becoming familiar with it has added benefits.

Alternatively, the adventurous might want to try the newer utility `Pipenv`.  [Pipenv][pipenv] is a convenience tool that facilitates both managing a virtual environment as well as installing packages.  Its usage is consistent across Windows and unix systems.

I have experienced some unexpected behavior (infrequent) with a Pipenv environment getting into a weird state that required running pipenv maintenance commands for clean up.   If you would rather not tinker with the latest and greatest, then stick with `venv` and `pip`.


## Set Up with Python `venv` and `pip`

  1. Change directory into where you cloned the project.
  2. Create a new virtual environment using python with the `venv` library.
  3. *Activate* the virtual environment.
  4. Install 3rd party libraries with `pip`

#### Windows

_*Run `CMD.exe` to open a new command shell and execute the following statements from the command line:*_

    cd wordplay

    python -m venv venv

    venv\Scripts\activate.bat

    pip install -r requirements.txt

**NOTE: you need to activate the virtual environment each time you launch a new command line shell.  Do this by re-running the `activate.bat` script.**

    venv\Scripts\activate.bat


#### Mac/Linux

_*Launch `Terminal` to open a new terminal shell and execute the following statements from the command line:*_

    cd wordplay

    python3 -m venv venv

    source venv/bin/activate

    pip install -r requirements.txt

**NOTE: you need to activate the virtual environment each time you launch a new command line shell.  Do this by re-sourcing the `activate` script.**

    source venv/bin/activate


## Alternative Set Up with `pipenv`

The `pipenv` tool serves 2 roles: 
  1. creating and *activating* a virtual environment
  2. installing 3rd party packages

Pipenv does not ship with Python and needs to be installed from the command line using pip (a.k.a. `pip3`).

_*The following commands need to be run from your command line shell.*_

    pip3 install pipenv

Activate the virtual environment from within the repo directory:

    # change to the project directory you cloned
    cd wordplay
    pipenv shell

**NOTE: you need to activate the virtual environment each time you launch a new command line shell by reinvoking `pipenv shell`.**

Install the 3rd party packages:

    pipenv install --dev

This will install Flask and PyTest libraries.


## Verify Pytest

Confirm `pytest` is available by running the following from the command line:

    pytest -v

## Verify Flask

Verify Flask launches from the command line:

    python app.py

Open your browser to http://127.0.0.1:5000/


# Development Milestones

1) Set up your developer environment.  Confirm Flask and PyTest are installed.
2) Edit `wordplay.py` and make `score_word()` functional so that the tests pass.
3) Play with Flask.  Try modifying the `/` URL to load from a template instead of the hardcoded response string.
4) Write a function to read in the lexicon file `sowpods.txt` and return the contents as a list.  
  The loader function should skip any empty lines or lines that start with '`#`'.  
  The words should be converted to lowercase.  
  *Write tests to demostrate this behaves correctly.*
5) Create a class that is initialized using a list of words and provides a means of testing if a word is contained in the list.  
  The result should return back a 2-element tuple: the first element is the scrabble score of the word, the second element is the word itself.  
  If the word is not contained, `None` should be returned or an exception thrown (your choice).  
  *Write tests to demonstrate this object behaves as expected.  The sample word list in the test can be hard coded and does not need to be read from the `sowpods.txt` lexicon file.*
6) Add the `/api/v1/words/{word}` endpoint to your Flask application.  
  The word lookup should be case insensitive.  
  If the word is contained in the lexicon an `HTTP 200` should be returned as well as a JSON response with the word and its scrabble score.  
  If the word is not in the lexicon an `HTTP 404` response should be returned and an appropriate JSON encoded message.  
7) Update the object created in step 5, adding functionality to search for words that can be created using a supplied list of letters.  
  Start with something simple, get it working, then discuss with the group how this can be optimized.  
  *Again, write tests to demonstrate this object behaves as suggested.*
8) Add the `/api/v1/matches/{letters}` endpoint to your Flask application.  
  The matching functionality should be case insensitive.  
  The response JSON should be sorted by score from high to low, with a secondary lexicographic sort by word.





[W]: readme_assets/letter_tile_w_small.jpg
[O]: readme_assets/letter_tile_o_small.jpg
[R]: readme_assets/letter_tile_r_small.jpg
[D]: readme_assets/letter_tile_d_small.jpg  
[P]: readme_assets/letter_tile_p_small.jpg
[L]: readme_assets/letter_tile_l_small.jpg
[A]: readme_assets/letter_tile_a_small.jpg
[Y]: readme_assets/letter_tile_y_small.jpg

[venv]: https://docs.python.org/3/tutorial/venv.html
[pip_tool]: https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip
[pipenv]: https://docs.pipenv.org/
[vs_code_setup]: https://github.com/PDXPythonPirates/wordplay/blob/master/README_VSCODE.md
[pycharm_setup]: https://github.com/PDXPythonPirates/wordplay/blob/master/README_PYCHARM.md

