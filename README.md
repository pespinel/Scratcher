# ScratchBatchAccountCreator
Simple script to create accounts from scratch.mit.edu using selenium.

## Usage

### Installing requirements

Create a virtual environment with any tool and install all the requirements listed in the `requirements.txt` file.

### Setting up

Modify any of the configurable params such as the email, the birth month/year or the country. 
Also change the default CSV delimiter if your csv does not use the default one: `;`.

### Running

Place your csv file in the root of this project and run the `main.py` script using python.
A log file called `accounts.log` will be created at the root of this project after the execution.
