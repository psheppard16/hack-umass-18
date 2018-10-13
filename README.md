# COMPSCI 326 Web Programming

This is the project repository template that your COMPSCI 326 team
will `fork` and use to begin your semester project work. Please follow
the instructions carefully in each of the project submission
requirements for your team to be successful. This is the structure of
this repository:

* `docs` - this folder is used to store all documents that are
  requested as part of the submission.
* `src` - this folder is used for your project code.

### Configuration ###

##### Clone and Setup Repository
```sh
Clone and enter repo:
$ git clone https://github.com/thomask156/326_project.git
$ cd 326_project
```

##### Configuring and starting vagrant
```sh
Download VirtualBox.

Download Vagrant.

Create environment:
    command line:
        $ vagrant up
    pycharm:
        tools -> vagrant -> up
        tools -> vagrant -> reload
    
    Start ssh session:
    command line:
        $ vagrant ssh
    pycharm:
        tools -> Start SSH session... -> Vagrant at ...
    
Navigating to the project:
$ cd /vagrant
```

##### Install Dependencies
```sh
Update apt-get:
$ sudo apt-get update

Install pip:
$ sudo apt-get install python3-pip

Create and activate virtual environment:
$ sudo pip3 install virtualenv
$ virtualenv --always-copy .venv
$ source .venv/bin/activate

Install pip requirements:
$ cd src
$ pip3 install -r requirements.txt

Install node:
$ curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
$ sudo apt-get install -y nodejs
$ sudo apt-get install npm

Install gulp globally:
$ sudo npm install -g gulp

Set node to development mode
$ sudo npm config set -g production false

Install node requirements:
On mac/linux:
    $ npm install
On windows:
    $ npm install --no-bin-links
    You may need to run:
    $ nodejs node_modules/node-sass/scripts/install.js
    $ npm rebuild node-sass --no-bin-links

Create settings_secret.py using template:
$ cp argue/settings_secret.py.template argue/settings_secret.py

Enter random characters for the 'SECRET_KEY' in `settings_secret.py`:
SECRET_KEY='super random characters'

Collect static resources for main site:
$ gulp (`gulp watch` for continuous collection)

Collect static resources for admin site:
$ python manage.py collectstatic

Run the django site:
source .venv/bin/activate
cd src
python3 manage.py runserver 0.0.0.0:8000
```

##### Database Setup
```sh
Install sqlite3:
$ sudo apt-get install sqlite3

Make the database:
$ cd databases
$ sqlite3 db.sqlite3
sqlite> .exit
$ cd ..

Make migrations: 
$ python manage.py makemigrations

Run migrations: 
$ python manage.py migrate

Create a super user:
$ python manage.py createsuperuser

Populate database with default models:
$ python manage.py configure_argue

```

### Documentation

##### Contributing
```sh
Documentation is written with [Sphinx](http://www.sphinx-doc.org/en/stable/). 
The .rst files are located in the `sphinx` folder.

To open the documentation in your browser:
$ python manage.py open-docs

To build the documentation after changes:
$ python manage.py build-docs
```

### Testing ###

##### Running tests locally
```sh
Run all tests:
$ driver=chrome REMOTE_USER=admin python manage.py --keepdb

Run specific tests: 
$ driver=[driver] REMOTE_USER=admin python manage.py --keepdb testing.[test file].[test class].[test]
```