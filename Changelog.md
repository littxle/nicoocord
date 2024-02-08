# Changelog

## Version 2.1.5

* Added `get` method to the bot class to get a item from the `nicoocord.json`

## Version 2.0.0

* Removed FastSelect.
* Made a custom cog loader, now the object of a cog is now `nicoocord.Bot` instead of `discord.Bot`.
* Added `nicoocord.json` instead of passing the arguments direct to the bot class.
* change the `exec` method to `run`, token is now an optional argument.
* Added docstrings to all methods in the bot class.
* Added a custom error.
* Added `try-except` to the version checker.
* Added a full bot example for `nicoocord 2.0.0`.
* Added the `Log` class to the `__init__` so you can use the logger too.
