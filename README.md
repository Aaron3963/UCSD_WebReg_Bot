# UCSD WebReg Bot🤖
This is an automated web program for UCSD's online course enrollment system ([webreg](https://act.ucsd.edu/webreg2)).

## Warning
This program is still in its experimental stage\
⚠️USE AT YOUR OWN RISK⚠️

## What can it do
* Constantly refreshing webreg to check if there are new seats avaliable
* Go backwards to the "go" page to ensure the page is refreshed
* Automatically enroll the class if there is vacancy
* Enroll multiple courses
* Timer for specific duration (developing)


## Prerequisities
* [Python 3.x](https://www.python.org/downloads/)
* Selenium
```pip install selenium```
* Web Driver (Best to use [Chrome](https://chromedriver.storage.googleapis.com/index.html))\
  Notice to download the correspond driver version that is the same as your browser version and replace the existing one.

## How does it work
1. Open ```config.json```, enter your UCSD username & password

2. Enter the quarter, formated as same as below
   <img src="img/Quarter.png"  width="70%">

3. Check your webreg and record all courses you like to enroll followed by session IDs


> **Notice**\
> There is no space between the letters and numbers of courses\
> The session ID should be a string (inside "")

4. Run the bot.py file
5. Prepare to authorize SSO login
6. Leave the program running
7. When the bot finds a vacancy for a class, it will enroll automatically and an email notification will be send to your email.
8. When all classes are enrolled, the program exists itself
