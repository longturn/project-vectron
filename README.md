# project-vectron
New Tileset for Freeciv21. Code name Project Vectron.

## Contribute to the Project

Linux is preferred development platform. Inkscape is expected to be installed.

For Debian or Debian based (e.g. Ubuntu) systems: `sudo apt install inkscape`

Fork this repository to your personal GitHut account.

Perform SSH based clone: `git clone git@github.com:[user-name]/project-vectron.git`.

Enter project directory: `cd project-vectron`.

Add upstream: `git remote add upstream https://github.com/longturn/project-vectron.git`.

## Install

Install Freeciv21 - https://longturn.readthedocs.io/en/latest/General/install.html

Capture the location of the `share/freeciv21` directory.

Add the local setup above to an environment variable:

* Edit `.bashrc`: `nano ~/.bashrc`
* Add something like this to the bottom: `export FREECIV_DATA_PATH=~/some/path/project-vectron:~/install/freeciv21/share/freeciv21`
* Source the file: `. ~/.bashrc`

As changes are made to the `*.svg` files, export them to `*.png` files:

* `.../project-vectron$ make`
