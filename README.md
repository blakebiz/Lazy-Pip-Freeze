# Lazy-Pip-Freeze
Place this file in a new environment with your files that need pip installing and call the main function using their file names and this will run them and catch file not found errors then pip install those files and when done pip freeze them to a requirements.txt for you

To run simply open BuildRequirements.py, go to the main() function and replace 'example_file.py' with the name of your file to be ran then just run the BuildRequirements.py file.

The idea behind this is I sometimes install modules I later end up not needing but never go back and uninstall so sometimes my bigger projects accumulate unnecessary modules. With this I can just make a new environment, run this once, and I can be certain I have no unnecessary modules in my environment plus it pip freezes them to a requirements.txt file for you!

*WARNING* This must be used in a new environment if you want the bare minimum modules. If there are any unnecessary modules installed it will not uninstall them, it will only install modules called but not installed.
