# AIServer-API
一个基于Django的API。   
[English](README.md) | 简体中文

## 介绍
这是一个API项目。最初创建它的原因是没有类似的项目，所以我们想建造一个。该项目将不断更新，并致力于造福更多的人。如果你想加入我们，欢迎！如果您在使用过程中遇到任何问题，请不要吝惜您的issue。

## 安装
这是一个基于Python的项目，所以开始前请确保您有Python 3.6或更高版本。  
如果您没有Python，请前往[Python官网](https://www.python.org)下载。  
##### 在安装前，请**确保您的pip设置没有问题**，并使pip设置变为符合您所在的国家或地区的网络环境。  
```py
pip install -r requirements.txt
```
如果您使用GPU进行运算，您可以使用以下命令：  
```py
pip install paddlepaddle-gpu
```

## 运行
在初次运行前，您需要设置对应的参数在 [setting.py](https://github.com/MomentQYC/AIServer-API/blob/master/aichat/settings.py)，并在项目根目录下运行以下命令:
```py
python3 manage.py migrate
```
接下来是每次运行都需要执行的命令：
```py
python3 manage.py runserver
```
如果您想部署公网服务，请在命令后附带以下参数：
0.0.0.0: Port
例如:
```py
python3 manage.py runserver 0.0.0.0:8000
```

## 功能
- [x] 交流与鉴黄  
- [ ] 谣言检测  
- [ ] 访问密钥  
- [ ] 以及更多...  
接下来，我们会致力于实现更多功能

## 捐赠
### [如果您觉得这个想法不错，请支持我们(中文为爱发电)](https://afdian.net/@yateam)
