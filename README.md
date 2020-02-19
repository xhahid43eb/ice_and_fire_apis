# ice_and_fire_apis
Completed Guide to setup project from scratch.
* Covered OS
    * Ubuntu
## Table of Contents
* [Environment Setup](#environment-setup)
    * [Python3.7](#python37)
    * [PIP](#pip)
    * [MySQL](#mysql)
* [Project Setup](#project-setup)
    * [Install, Create and Activate Virtual Environment](#install-create-and-activate-virtual-environment)
    * [Database Setup](#database-setup)
* [Project Execution](#project-execution)
## Environment Setup
> For this project, we need to install following technologies and tools:
### Python3.7
```
$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
$ cd /usr/src
$ sudo wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz
$ sudo tar xzf Python-3.7.6.tgz
$ cd Python-3.7.6/
$ sudo ./configure
$ sudo make altinstall
$ python3.7 -V
```
For details, you can see [link](https://askubuntu.com/questions/682869/how-do-i-install-a-erent-python-version-using-apt-get)
### PIP
```
$ sudo apt-get install python3-pip
```
### MySQL
* Follow this [digital ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04) to install MySQL on Ubuntu
## Project Setup
```
$ git clone https://github.com/xhahid43eb/ice_and_fire_apis.git
```
### Install, Create and Activate Virtual Environment
```
$ pip3 install virtualenv
```
Create new python virtual environment with default python version set to 3.7
```
$ cd path/to/project_dir
$ virtualenv --python=`which python3.7` ./venv
$ source venv/bin/activate
```
### Installing dependencies
```
$ pip install -r requirements.txt
```
#### Database Setup

* Type `mysql -u root -p`, it will prompt MySQL root password, enter password.
* Create databases,
```
mysql> CREATE SCHEMA ice_and_fire DEFAULT CHARACTER SET utf8 ;
```
* Update Database configs in `setting.py` file
### Project Execution
```
$ python manage.py runserver
```

[Back to top](#ice_and_fire_apis)
