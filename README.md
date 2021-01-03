# Instagram Unfollow Bot
Instagram Unfollow Bot is a program written in python to find which of a users following are not also followers. It also has the ability to unfollow these users.
 
## How it Works
- - - -
This project uses a library for Facebook’s Instagram API by https://github.com/LevPasha/ called InstagramAPI. Using the library, it allows a user to login with their Instagram account information, make GET requests for the users following and followers, and make DELETE requests to unfollow the users that are not in both groups.

## Getting Started
- - - -
### Prerequisites
* python
```
brew install python
```
* virtual environment (*optional*)
```
pip install virtualenv
```

### Setup
* for virtualenv users only
```
virtualenv env
source env/bin/activate 
```
* installing required packages
```
pip install -r requirements.txt
```

### Usage
* enter login credentials into login_keys.py
* run the program
```
python3 main.py
```
