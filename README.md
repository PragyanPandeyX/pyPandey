<p align="center">
  <img src="./resources/extras/logo_readme.jpg" alt="TeamPandey Logo">
</p>
<h1 align="center">
  <b>Pandey - UserBot</b>
</h1>

<b>A stable pluggable Telegram userbot + Voice & Video Call music bot, based on Telethon.</b>

[![](https://img.shields.io/badge/Pandey-v0.8-crimson)](#)
[![Stars](https://img.shields.io/github/stars/TeamPandey/Pandey?style=flat-square&color=yellow)](https://github.com/TeamPandey/Pandey/stargazers)
[![Forks](https://img.shields.io/github/forks/TeamPandey/Pandey?style=flat-square&color=orange)](https://github.com/TeamPandey/Pandey/fork)
[![Size](https://img.shields.io/github/repo-size/TeamPandey/Pandey?style=flat-square&color=green)](https://github.com/TeamPandey/Pandey/)   
[![Python](https://img.shields.io/badge/Python-v3.10.3-blue)](https://www.python.org/)
[![CodeFactor](https://www.codefactor.io/repository/github/teamPragyan/Pragyan/badge/main)](https://www.codefactor.io/repository/github/teamPragyan/Pragyan/overview/main)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/TeamPandey/Pandey/graphs/commit-activity)
[![Docker Pulls](https://img.shields.io/docker/pulls/theteamPragyan/Pragyan?style=flat-square)](https://img.shields.io/docker/pulls/theteamPragyan/Pragyan?style=flat-square)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/TeamPandey/Pandey)
[![Contributors](https://img.shields.io/github/contributors/TeamPandey/Pandey?style=flat-square&color=green)](https://github.com/TeamPandey/Pandey/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/TeamPandey/Pandey/blob/main/LICENSE)   
[![Sparkline](https://stars.medv.io/TeamPragyan/Pandey.svg)](https://stars.medv.io/TeamPandey/Pandey)
----

# Deploy
- [Heroku](#deploy-to-heroku)
- [Okteto](#deploy-to-okteto)
- [Local Machine](#deploy-locally)

# Documentation 
[![Documentation](https://img.shields.io/badge/Documentation-Pandey-blue)](http://Pragyan.tech/)

# Tutorial 
- Full Tutorial - [![Full Tutorial](https://img.shields.io/badge/Watch%20Now-blue)](https://www.youtube.com/watch?v=0wAV7pUzhDQ)

- Tutorial to get Redis URL and password - [here.](./resources/extras/redistut.md)
---

## Deploy to Heroku
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://deploy.Pragyan.tech)

## Deploy to Okteto
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/TeamPandey/Pandey)

## Deploy Locally
- [Traditional Method](#local-deploy---traditional-method)
- [Easy Method](#local-deploy---easy-method)
- [Pandey CLI](#Pragyan-cli)

### Local Deploy - Easy Method
- Linux - `wget -O locals.py https://git.io/JY9UM && python3 locals.py`
- Windows - `cd desktop ; wget https://git.io/JY9UM -o locals.py ; python locals.py`
- Termux - `wget -O install-termux https://tiny.Pragyan.tech/termux && bash install-termux`

### Local Deploy - Traditional Method
- Get your [Necessary Variables](#Necessary-Variables)
- Clone the repository:    
`git clone https://github.com/TeamPandey/Pandey.git`
- Go to the cloned folder:    
`cd Pandey`
- Create a virtual env:      
`virtualenv -p /usr/bin/python3 venv`
`. ./venv/bin/activate`
- Install the requirements:      
`pip(3) install -U -r re*/st*/optional-requirements.txt`
`pip(3) install -U -r requirements.txt`
- Generate your `SESSION`:
  - For Linux users:
    `bash sessiongen`
     or
    `wget -O session.py https://git.io/JY9JI && python3 session.py`
  - For Termux users:
    `wget -O session.py https://git.io/JY9JI && python session.py`
  - For Windows Users:
    `cd desktop ; wget https://git.io/JY9JI -o Pragyan.py ; python Pragyan.py`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/TeamPandey/Pandey/blob/main/.env.sample).
(You can either edit and rename the file or make a new file named `.env`.)
- Run the bot:
  - Linux Users:
   `bash startup`
  - Windows Users:
    `python(3) -m pyPandey`

---
## Necessary Variables
- `SESSION` - SessionString for your accounts login session. Get it from [here](#Session-String)

One of the following database:
- For **Redis** (tutorial [here](./resources/extras/redistut.md))
  - `REDIS_URI` - Redis endpoint URL, from [redislabs](http://redislabs.com/).
  - `REDIS_PASSWORD` - Redis endpoint Password, from [redislabs](http://redislabs.com/).
- For **MONGODB**
  - `MONGO_URI` - Get it from [mongodb](https://mongodb.com/atlas).
- For **SQLDB**
  - `DATABASE_URL`- Get it from [elephantsql](https://elephantsql.com).

## Session String
Different ways to get your `SESSION`:
* [![Run on Repl.it](https://replit.com/badge/github/TeamPandey/Pandey)](https://replit.com/@TeamPandey/PandeyStringSession)
* Linux : `wget -O session.py https://git.io/JY9JI && python3 session.py`
* PowerShell : `cd desktop ; wget https://git.io/JY9JI ; python Pragyan.py`
* Termux : `wget -O session.py https://git.io/JY9JI && python session.py`
* TelegramBot : [@SessionGeneratorBot](https://t.me/SessionGeneratorBot)

---

# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
Pandey is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

---

# Credits
* [![TeamPandey-Devs](https://img.shields.io/static/v1?label=TeamPragyan&message=devs&color=critical)](https://t.me/PandeyDevs)
* [Lonami](https://github.com/LonamiWebs/) for [Telethon.](https://github.com/LonamiWebs/Telethon)
* [MarshalX](https://github.com/MarshalX) for [PyTgCalls.](https://github.com/MarshalX/tgcalls)

> Made with 💕 by [@TeamPandey](https://t.me/TeamPandey).    




# the steps are simple...
#### if your using screen you open your screen first!

#### You git clone the repo

### git clone https://github.com/TeamPandey/PandeyBackup.git

### cd PandeyBackup

### virtualenv -p /usr/bin/python3 venv

### pip3 install -U -r re*/st*/optional-requirements.txt

### pip3 install -U -r requirements.txt

####then you make sure your .env is filled out 


### python3 -m pyPandey &

if on vps
### deactivate
### exit

if using screen
deatch screen
