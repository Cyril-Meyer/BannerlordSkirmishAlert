# BannerlordSkirmishAlert

Are you tired of watching if a game of skirmish has finally started ?
Let your computer do it for you and let you know the way you prefer.

If you play Bannerlord regularly, you've probably noticed that it's becoming more and more impossible to play skirmish.
The script is there to prevent you from watching your screen and missing the start of a game.

# Usage
```
python SkirmishAlert.py -b -e
```

**Optional arguments**
```
python SkirmishAlert.py [-h] [-b] [-mb] [-e]

  -b, --beep         audio beep when triggered
  -mb, --messagebox  messagebox when triggered
  -e, --exit         exit when triggered
```


# Install

**create venv and install requirements**
```
# create venv
python -m venv venv
# activate venv
call venv\Scripts\activate.bat
# update
pip install -U pip setuptools wheel
# install requirements
pip install -r requirements.txt
```
