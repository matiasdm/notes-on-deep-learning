# Notes on deep learning  

This repository collects a number of random thought and experiments about deep learning. It is intended to support my own research and teaching.  

copyright matias di martino (c) 2019 -- matias.di.martino.uy@gmail.com  


## Index:
* file_A
* file_B
* file_C


## License information.

## Installation Instructions.
0. Prerequisited:
- Python 3, pip, and virtualenvwrapper (if you don't have them installed look at the next section for instructions). 
1. Prepare your python environment.  
$mkvirtualenv ENVNAME -p python3 &nbsp; &nbsp; &nbsp; _create your virtual environment_.  
$workon ENVNAME &nbsp; &nbsp; &nbsp; _use your brand new virtual environment_.  
$pip install -r requirements.txt &nbsp; &nbsp; &nbsp; _install python libraries_.  
**only if you are using GPUs, install also:**  
$pip install tensorflow-gpu==1.13.1 &nbsp; &nbsp; &nbsp; _only if you have GPUs!_  
2. Get our code.  
$git clone XXXXXX  

## References.

emphasis, aka italics, with *asterisks* or _underscores_.  
Strong emphasis, aka bold, with **asterisks** or __underscores__.  
Combined emphasis with **asterisks and _underscores_**.  
Strikethrough uses two tildes. ~~Scratch this.~~  


## Installing pre-requisites: (this is for mac, if you are in linux is similar, in windows idk)
Install python:
$brew install python
Check that it is correctly installed
$python3 --version 
$Python 3.x.x

Install pip:
$sudo easy_install pip

Install virtualenvwrapper:
$sudo pip install virtualenvwrapper   (maybe you have to use pip3 to install it in python3)

Finally add Shell Startup File
Add three lines to your shell startup file (.zshrc, .bashrc, .profile, etc.) to set the location where the virtual environments should live, the location of your development project directories, and the location of the script installed with this package:

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
