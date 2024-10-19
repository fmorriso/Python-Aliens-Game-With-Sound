# PyGame Aliens Example (Enhanced)
This is the Aliens example that comes with PyGame with a few enhancements
## Enhancements
* Scaled game size to a percentage of available device screen size instead of using hard-coded 640 x 480.
* Split Alien, Bomb, Explosion, Player, Score and Shot classes into individual files.
* Put common settings, especially scale factors, in a new Settings class.
## Tools Used

| Tool      |  Version |
|:----------|---------:|
| Python    |   3.13.0 |
| PyAutoGUI |   0.9.54 |
| PyGame    |    2.6.1 |
| VSCode    |   1.94.2 |
| PyCharm   | 2024.2.3 |
## References
* [PyGame Aliens example on GitHub](https://github.com/pygame/pygame/tree/main/examples)
* [PyGame: A Primer on Game Programming in Python](https://realpython.com/pygame-a-primer/)
## Change Log

| Date       | Description                                                                        |
|:-----------|:-----------------------------------------------------------------------------------|
| 2024-02-08 | added scaling based on device screen size.                                         |
| 2024-02-09 | changed score display font size to adjust to game size                             |
| 2024-02-10 | Moved Alien, Bomb, Explosion, Player, Score and Shot classes into individual files |
| 2024-02-13 | Moved game constants (MAX_SHOTS, ALIEN_BOMBS, etc.) to Settings class              |
| 2024-07-30 | refactor Settings class to use private instance variables and public properties    |
| 2024-10-18 | verify everything works with python 3.13.0 and other                               |

