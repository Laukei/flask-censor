# flask-censor
A profanity censor by Rob Heath with hooks for Flask and Jinja2, based on `profanity` by Ben Friedland and `flask-recaptcha` by mardix.

## Installation

`pip install flask-censor`

## Usage

The module can be used standalone (as `profanity` is), or can be integrated into a Flask app for use in Jinja2 templates.

### Flask

In your Flask code, link flask-censor to your Flask app as so:

```python
from flask import Flask
from flask_censor import Censor

app = Flask(__name__)
censor = Censor(app=app)

# or if adding app later:

censor = Censor()
censor.init_app(app)
```

### Jinja2

When integrated with Flask the module provides a template filter `censor` accessible through Jinja2 templates using the filter pipe:

```jinja
<h1> {{ data_from_flask|censor }} </h1>
```

## Config

If integrated with Flask, the following config variables control behaviour:

`CENSOR_WORDLIST`: path to file from which to read the word list for censorship

`CENSOR_CHARACTERS`: string of values to use in place of censored word

If not integrating with Flask, these can be set using the keyword arguments `wordlist` and `censorchars` when instantiating the class.

## API

**censor.init_app(app=app)** initialises flask-censor to a Flask app instance

**censor.import_wordlist(wordlist)** imports a new word list from the file at path `wordlist`

**censor.censor(input_string)** goes over the input string, replacing sub-strings from the word list with sensor characters from the censor character pool

**censor.set_censorchars(censorchars)** sets the pool of characters to use for censoring words from the word list