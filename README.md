# AIServer-API
An API based on Django.  
English | [简体中文](README_ch.md)

## Introduction
This is an API project. The original intention is that there is no similar project, so we want to build one. This project will be constantly updated, and is committed to benefiting more people. If you want to join us, welcome! If you have any problems during use, please submit the issue.

## Installation
This is a Python based project, so first make sure you have Python 3.6 or above.
If you do not have python, please go to [the official Python website](https://www.python.org) to download it.
##### Before installation, please **confirm that your pip configuration is OK**, and check the network conditions in your country or region.
```py
pip install -r requirements.txt
```
If you are running with a GPU, you can run the following command.
```py
pip install paddlepaddle-gpu
```

## Operation
The first time you run it, you need to Modify database parameters in [setting.py](https://github.com/MomentQYC/AIServer-API/blob/master/aichat/settings.py), then you need to first run the following command in the root directory of the project:
```py
python3 manage.py migrate
```
The next one is required for each run.
```py
python3 manage.py runserver
```
If you need to make the public network accessible, you need to bring the following parameters:
0.0.0.0: Port
e.g.:
```py
python3 manage.py runserver 0.0.0.0:8000
```

## Features
- [x] Conversation and pornography identification.  
- [ ] Rumor Identification.  
- [ ] Access Key.  
- [ ] More...  
Next, we need to implement more features.

## Donation
### [Buy me a cup of coffee](https://www.patreon.com/yateam)
