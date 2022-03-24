# Python-API-Project
I created a command line Python program, which retrieves the information of a GitHub User and creates a new Contact or updates an existing contact in Freshdesk, using their respective APIs.
1.  Before run the program, you must set values for both environment variables 
in the terminal -> GITHUB_TOKEN and FRESHDESK_TOKEN. These values are API keys.
> Environmental variables are set as follows:
> 
>     export FRESHDESK_TOKEN=APIkey
>     export GITHUB_TOKEN=APIkey
To run the program (main.py), you must enter the following command in the terminal:
>     python3 main.py first_argument second_argument
where first_argument is the correct GitHub username, second_argument is the correct Freshdesk subdomain.

## Unit Tests
To run the unit tests (TestAPIs.py), you must run the following command:
>     python3 -m unittest TestAPIs.py
