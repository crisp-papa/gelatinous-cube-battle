# Gelatinous Cube Battle
Originally coded in 2015 while learning python, Gelatinous Cube Battle (battle.py) was a prototype engine using [d20](https://en.wikipedia.org/wiki/D20_System) inspired rules for battle written in the procedural style.
There is also an updated version written in Python 3 object oriented style.

## Run Battle.py
Play the original simply with `python battle.py`. The script takes no arguments and runs in your terminal. 

## Updated Version
If you would like to build and run the current version, follow these steps. 

## Requirements
### MongoDB

If you need to install Mongo, simply check their [website](https://www.mongodb.com/try/download/community).

You can easily install it on mac os [with brew](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/):
> `brew tap mongodb/brew`
> `brew install mongodb-community`

You can also install it on [linux](https://docs.mongodb.com/manual/administration/install-on-linux/) or [windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/).



### Install Dependencies
Build a virtual environment and activate it
> `python3 -m venv ~/.virtualenvs/gelatinous && . ~/.virtualenvs/gelatinous/bin/activate`

Update pip if you aren't on latest
> `pip install --upgrade pip` 

Install the dependencies
> `python3 -m pip install -r requirements.txt`

Finally, the application can be run as a module from the command line with
> `python3 -m app`