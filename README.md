Rock Paper Scissors Lizard Spock
================================

[![Build Status](https://travis-ci.com/AJ8GH/rock-paper-scissors-lizard-spock.svg?branch=main)](https://travis-ci.com/AJ8GH/rock-paper-scissors-lizard-spock) [![codecov](https://codecov.io/gh/AJ8GH/rock-paper-scissors-lizard-spock/branch/main/graph/badge.svg?token=RQBF1D03HY)](https://codecov.io/gh/AJ8GH/rock-paper-scissors-lizard-spock) [![Maintainability](https://api.codeclimate.com/v1/badges/d6fdb7d04a1d7549515f/maintainability)](https://codeclimate.com/github/AJ8GH/rock-paper-scissors-lizard-spock/maintainability) [![BCH compliance](https://bettercodehub.com/edge/badge/AJ8GH/rock-paper-scissors-lizard-spock?branch=main)](https://bettercodehub.com/)

Built with Python and Flask

## Getting Started

This project uses Python 3.9 and pip as a package manager. You can download python, either using [Homebrew](https://docs.brew.sh/Homebrew-and-Python), or a version manager such as [pyenv](https://github.com/pyenv/pyenv), which is useful for managing multiple versions on your machine.

Clone this Repository and navigate to the root of the project.

```shell
git clone https://github.com/AJ8GH/rock-paper-scissors-lizard-spock
cd rock-paper-scissors-lizard-spock
```

Optionally, create a virtual environment.

```shell
pip install virtualenv
virtualenv env
source env/bin/activate
```

Install dependencies.

```shell
pip install -r requirements.txt
```

## Running Tests

* Run all tests with `pytest`
* Run feature tests only with `pytest test/features`
* Run unit tests only with `pytest test/models`

## Dependencies

*From requirements.txt*

* `attrs==21.2.0`
* `click==8.0.0`
* `coverage==5.5`
* `Flask==2.0.0`
* `iniconfig==1.1.1`
* `itsdangerous==2.0.1`
* `Jinja2==3.0.1`
* `MarkupSafe==2.0.1`
* `packaging==20.9`
* `pluggy==0.13.1`
* `py==1.10.0`
* `pyparsing==2.4.7`
* `pytest==6.2.4`
* `selenium==3.141.0`
* `six==1.16.0`
* `splinter==0.14.0`
* `toml==0.10.2`
* `urllib3==1.26.4`
* `Werkzeug==2.0.1`

## Specification

- user should be able to enter their name before the game
- user will be presented the choices (rock, paper, scissors, lizard, spock)
- user can choose one option
- the game will choose a random option
- a winner will be declared

## User Stories

As a user,
So that I can see my name displayed when I win,
I want to be able to enter my name

As a user,
So that I can choose an option,
I want to be presented with the 5 choices
