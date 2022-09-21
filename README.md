# UCSD WebReg Bot🤖
This is an automated web program for UCSD's online course enrollment system (webreg).

## What can it do
* Constantly refreshing webreg to check if there are new seats avaliable
* Automatically enroll the class if there is vacancy
* Timer for specific duration (developing)
* Go backwards to the "go" page to ensure the page is refreshed (developing)

## Prerequisities
* Python 3.x
* Selenium
```pip install selenium```
* openpyxl
```pip install openyxl```

## How does it work
1. Put your UCSD username & password in B1 and B2 cell inside ```config.xlsx```
2. Check your webreg and record all courses you like to enroll\
   Format:
   
|   |   |   |   |   |   |
|---|---|---|---|---|---|
| Username | Name Here | --- | --- | --- | --- |
| Password | PW Here | --- | --- | --- | --- |
| MMW16 | 12345 | 12346 | 12347 | 12348 | ...... |
| MMW17 | 024680 | 024681 | 024682 | 024683 | ...... |

> **Notice**\
> There is no space between the letters and numbers of courses\
> No need to add 0 before numbers as it is a hard thing to do in xlsx files

3. Run the bot.py file
4. Prepare to authorize SSO login
5. Leave the program running
6. When the bot finds a vacancy, it will enroll and the program exists
