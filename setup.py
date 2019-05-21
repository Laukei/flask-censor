import setuptools
import flask_censor

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "flask-censor",
	version = flask_censor.__version__,
	author = "Robert Heath",
	author_email = "rob@robheath.me.uk",
	description = "A profanity censor with hooks for Flask and Jinja2",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/Laukei/flask-censor",
	packages = ['flask_censor'],
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Development Status :: 3 - Alpha"]
	)