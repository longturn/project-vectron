# project-vectron
New Tileset for Freeciv21. Code name Project Vectron.

## Contribute to the Project

Linux is preferred development platform.

Fork this repository to your personal GitHub account.

Perform SSH based clone: `git clone git@github.com:[user-name]/project-vectron.git`.

Enter project directory: `cd project-vectron`.

Add upstream: `git remote add upstream https://github.com/longturn/project-vectron.git`.

## Prerequisites

Vectron needs to be compiled before being used. For this, you need [GNU Make](https://www.gnu.org/software/make/), [Python](https://www.python.org/) (used to generate some sprites), and [rsvg-convert](https://gitlab.gnome.org/GNOME/librsvg/-/tree/main/) (to render sprites as PNG). On Ubuntu, the following command will give you the dependencies:

    sudo apt install make librsvg2-bin


## Install

Install Freeciv21 - https://longturn.readthedocs.io/en/latest/General/install.html

Capture the location of the `share/freeciv21` directory.

Add the local setup above to an environment variable:

* Edit `.bashrc`: `nano ~/.bashrc`
* Add something like this to the bottom: `export FREECIV_DATA_PATH=~/some/path/project-vectron:~/install/freeciv21/share/freeciv21`
* Source the file: `. ~/.bashrc`

As changes are made to the `*.svg` files, export them to `*.png` files:

* `.../project-vectron$ make`
