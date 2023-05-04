# Scratcher
Simple script to create scratch accounts using selenium.

## Usage

### Installing requirements

Create a virtual environment with any tool and install all the requirements listed in the `requirements.txt` file.

### Setting up

Modify any of the configurable params such as the email, the birth month/year or the country. 
Also change the default CSV delimiter if your csv does not use the default one: `;`.

### Running

Place your csv file in the root of this project and run the `main.py` script using python.
You will probably need to complete a captcha manually after creating a certaing number of users.
You can also use a proxy-list to add the proxy capability everytime that the driver is started (On each row of the excel). This will avoid the captcha most of the times.
A log file called `accounts.log` will be created at the root of this project after the execution.
