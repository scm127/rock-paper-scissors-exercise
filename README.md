# rock-paper-scissors-exercise

This is a Python application that instructs someone to clone the application, set up a username in a local development enviorment, and play rock, paper, scissors.  

Prerequisites:
Anaconda 3.7+
Python 3.7+
Pip

Installation
Fork this remote repository under your own control, then "clone" or download your remote copy onto your local computer.

Navigate to the repository from the command line (subsequent commands assume you are running them from the local repository's root directory):
cd rock-paper-scissors-exercise

Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

conda create -n my-game-env python=3.8
conda activate my-game-env

From inside the virtual environment, install package dependencies:

pip install -r requirements.txt

The requirmemnts.txt has the python-dotenv 
NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial cd step above)

Setup
In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

USER_NAME="Sean Minson"

Run the game script and follow the game instructions:

python game.py

NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the pip command above to ensure that package has been installed into the virtual environment

