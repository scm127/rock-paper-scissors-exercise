# rock-paper-scissors-exercise
This Readme.md is adopted from Professor Rosetti's "Run the App Exercise". It explains how to clone the application, set up a username in a local development enviorment, and play rock, paper, scissors.  

# Prerequisites:
Anaconda 3.7+
Python 3.7+
Pip

# Installing the Repository
Fork this remote repository under your own control, then "clone" or download your remote copy onto your local computer.

Navigate to the repository from the command line (subsequent commands assume you are running them from the local repository's root directory). If you saved the repository to your desktop use the following code or else you will have to adjust the code to wherevere the repository is saved:

cd ~/Desktop/rock-paper-scissors-exercise

# Create and activate virtual enviorment
Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

conda create -n my-game-env python=3.8
conda activate my-game-env

From inside the virtual environment, install package dependencies. The requirmemnts.txt file has the Dotenv  package which is needed to load enviorment variables:

pip install -r requirements.txt

# Setup Username
In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

PLAYER_NAME="Sean Minson"

# Run the Game Script from the command line:

python game.py



