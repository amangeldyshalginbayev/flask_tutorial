# Flaskblog

This repository created for learning Flask framework by building blogging web application. The application is deployed to DigitalOcean VPS and can be accessed via this IP address: http://178.128.145.253/.

## Technology stack used in production:
* **Ubuntu 20.04** - VPS server OS
* **Nginx** - reverse proxy
* **Gunicorn** - Python WSGI HTTP Server
* **SQLite** - database engine
* **Flask** - Python web framework

# Key functionalities of the application

## Users
* User registration via email. After registration account activation link sent to your email, you need to visit this link to activate your account. When trying to login with account that not yet activated, application notifies and sends activation link again to registered email
* Login
* Logout
* Upload profile picture
* Change username and email
* Resetting your password via email
* Link mobile phone number to your account. Currently, implemented only 3 countires: United Kingdom, Kazakhstan, Estonia. SMS PIN code sent to your number via [Messente-API](https://messente.com/documentation/omnichannel-api). You can send sms from your application using HTTP all around the world using this service.

## Posts
* Create
* Update
* Delete
* Like
* Cancel like

## Comments
* Create
* Update
* Delete

For demonstration purposes you can use this account I already created. Email: geldy2016@yandex.kz, Password: Letmein1!

## Key Python packages used
The application developed and tested in **Python3.8**.
* Flask - micro-framework for web application development
* messente-api - for sending sms pin codes
* Jinga2 - templating engine
* SQLAlchemy - ORM (Object Relational Mapper)
* Flask-Migrate - SQLAlchemy database migrations for Flask using Alembic.
* Flask-Bcrypt - password hashing
* Flask-Login - user session management for Flask 
* Flask-WTF - simplifies working with forms by integrating Flask and WTForms
* yagmail - GMAIL/SMTP client for Python
* Pillow - for image resizing
* gunicorn - Python WSGI HTTP Server
* ItsDangerous - securely signs data to ensure its integrity
* pycodestyle - checking python code for PEP-8
* pytest - framework for testing Python code

## Database
For local development and testing **SQLite** database management system is used.

## Installation

To run the applicatin in local environment. Create new directory:

```bash
$ mkdir myproject
$ cd myproject
```
Create virtual environment with built-in python3 venv module and activate it:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
Clone the repository with command:
```bash
(venv)$ git clone git@github.com:amangeldyshalginbayev/Blogging_Application.git
```
Install all dependencies of the project via pip:
```bash
(venv)$ pip install -r requirements.txt
```
You can check all installed dependencies via command:
```bash
(venv)$ pip list
```
To run the application you need to create [Gmail](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp) account, [Messente](https://dashboard.messente.com/register) account and get your API keys, fill configuration.cfg file inside flaskblog package with the following values:

myproject/flaskblog/configuration.cfg
```bash
SECRET_KEY='top secret'
SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS=False
GMAIL_USERNAME='gmail username'
GMAIL_PASSWORD='gmail password'
MESSENTE_API_USERNAME='messente api username'
MESSENTE_API_PASSWORD='messente api password'
```
For security reasons, this file excluded from version control and used only for local development and testing. After creating this configuration file and filling all values, you need to initialize database. For creating SQLite database and all tables flask command line function has been implemented. Run the following command in the root directory of the project:
```bash
(venv)myproject$ flask init-db 
```
After running this command, SQLite database file is created called site.db under flaskblog folder. Now you can run your application with the following command:
```bash
(venv)myproject$ flask run
```
You should see that the application is running:
```bash
 * Serving Flask app "flaskblog" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 326-842-537
```
## Tests
To run unit tests type the following command from application root folder or under tests folder:
```python
(venv)myproject$ pytest
 or
(venv)tests$ pytest
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)