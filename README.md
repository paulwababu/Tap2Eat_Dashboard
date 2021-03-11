# Tap 2 Eat Web Implementation

Please check the github issues page before implementation.

#### Project layout

Path | Description
-----|------------
home/ | Project root (created by django-admin startproject). Home to README.md and Django's manage.py script.
mainapp/ | Application root
mainapp/tap2eat/static/ | Static files (CSS, JS, etc)
mainapp/mainapp/wsgi.py | Python WSGI script for Apache integration


### Basic Installation
* This guide assumes Debian/Ubuntu is the running OS. Administrative rights are obtained using **sudo**.
* Basic installation will get the application up and running, however it is not suitable for production use

1. Clone the repo then Install pip
```bash
$ sudo apt-get install python3 python3-pip
```

2. Update pip3 to latest version (using sudo with pip requires the -H flag)
```bash
$ sudo -H pip3 install --upgrade pip
```

3. Install Requirements.txt file
```bash
$ pip3 install -r requirements.txt
```

4. Edit the following lines of mainapp/settings.py to match your environment
```python
#  Put a random string at least 50 characters long here. This will keep hashed passwords safe.
SECRET_KEY = 'abcdefgsflxushdfmilsdhfidjsnhcfgiksjfgikdhgisldgiemlgnilehw59y349yjwe9'
```

5. At this point, you should have enough configured to run the app using Python's development server. Run the following command and browse to http://hostIp:8000
```bash
/mainapp$ $ sudo python3 manage.py migrate $$ sudo python3 manage.py runserver 0.0.0.0:8000
```
6. Edit the following lines of mainapp/settings.py to add domain name/IP
```python
#add domain or host
ALLOWED_HOSTS = ['tap2eat.co.ke']
```

### Using a production web server
It is highly recommended to use a 'real' web server for running. Install apache2 and LetsEncrypt

1. Update packages
```bash
$ sudo apt-get update

```
2. Install Software Properties
```bash
$ sudo apt-get install software-properties-common

```
3. Add Repository Universe
```bash
$ sudo add-apt-repository universe

```
4. Install certbot
```bash
$ sudo add-apt-repository ppa:certbot/certbot

```
5. Update packages
```bash
$ sudo apt-get update

```
6. Install python-certbot apache
```bash
$ sudo apt-get install python-certbot-apache

```
### ############################ Once you reach this point ############################

1. Edit apache config to use wsgi.py included with static and attachments directories
```bash
$ sudo nano /etc/apache2/sites-enabled/000-default.conf
```

```apacheconf
# Add server name as tap2eat.co.ke
# For now, comment out the following lines(WSGI files) and you will uncomment after you make the new config files successfully, otherwise you will get an error "you are not allowed to duplicate commands":

```
 #WSGIScriptAlias..
 #WSGIDaemonProcess..
 #WSGIProcessGroup..
```
### CONFIG FILE STRUCTURE BELOW

```

<VirtualHost *:80>
        ServerAdmin www.tap2eat.co.ke
        DocumentRoot /var/www/html

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        <Directory /mainapp>
                Options Indexes MultiViews FollowSymLinks
                Require all granted
        </Directory>

        <Directory /mainapp/mainapp>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

		# The real location of these directories can be moved if desired.
        # Remember to update mainapp/settings.py to reflect changes here.
        Alias /static mainapp/tap2eat/static
</VirtualHost>
```

### ######################################################################

2. Edit apache config file

```bash
$ sudo nano /etc/apache2/sites-enabled/000-default.conf
```

```apacheconf
# These lines must be outside of the VirtualHost directive
WSGIScriptAlias / mainapp/mainapp/wsgi.py
WSGIPythonPath /mainapp/mainapp

<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        <Directory /mainapp>
                Options Indexes MultiViews FollowSymLinks
                Require all granted
        </Directory>

        <Directory /mainapp/mainapp>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

		# The real location of these directories can be moved if desired.
        # Remember to update mainapp/settings.py to reflect changes here.
        Alias /static mainapp/tap2eat/static
</VirtualHost>
```
### #######################CONTINUE CONFIGURATION FOR CERTBOT ABOVE#####################

7. Continue installation by installing certbot

```bash
$ sudo certbot --apache
```

10. Edit the 000.conf file and delete, using ctrl + k, the following lines of code since we already have this information in our new configuration file generated
    i.) All Alias lines
    ii.) All Directory lines
    iii.) All WSGI files
* Be Careful not to delete the Rewrite lines in the process    

```
```
9. Edit the new file generated for ssl file at /etc/apache2/sites-available/django_project-le-ssl.conf

```bash
$ sudo nano /etc/apache2/sites-available/django_project-le-ssl.conf

```
10. Uncomment out and save the WSGI Files that we had commented out earlier as this will allow our webserver to communicate with our Django code

```
```
11. Run the following script

```bash
$ sudo apachect1 configtest

```
12. Run the following script to allow https traffic then restart apache

```bash
$ sudo ufw allow https
$ sudo service apache2 restart
```
13. Headover to https://www.tap2eat.co.ke/home to test

```
```

13. Run the following script to create a cronjob to run the renew ssl automatically after 3 months

```bash
$ sudo crontab -e
# Select editor you wish

```
12. Lets say we want to run renew command at 4.30am on the first of everymonth, we would run the following command

# Add the following lines of code at the bottom to represent: 30 for minutes, four for the hour, one for the day of the month then a * for the month and the next * for the day of the week

$ 30 4 1 * * sudo certbot renew --quiet

```
```
# Security Features Enforced

1. Cross site request forgery (CSRF) protection

#Added these lines in settings.py(only do so when HTTPS is enforced)

CSRF_COOKIE_SECURE = True #to avoid transmitting the CSRF cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True #to avoid transmitting the session cookie over HTTP accidentally.

2. Cross-site Scripting (XSS)

#Added this lines to prevent injections from attackers

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

3. SSL Redirect

#Added this line so force all HTTP traffic to HTTPS

SECURE_SSL_REDIRECT = True

4. HTTP Strict Transport Security

#When this policy is set, browsers will refuse to connect to your site for the given time period if you’re not properly serving HTTPS resources, or if your certificate expires.

SECURE_HSTS_SECONDS = 86400  # 1 day
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

5. Content Security Policy (CSP)

#PIP INSTALL DJANGO-CSP
#Edit your project’s settings module, to add the django-csp middleware to MIDDLEWARE, like so:

MIDDLEWARE = (
    # ...
    'csp.middleware.CSPMiddleware',
    # ...
)

#Add the following lines to settings.py
# Content Security Policy
CSP_DEFAULT_SRC = ("'none'", )
CSP_STYLE_SRC = ("'self'", 'paulkiragu621.github.io', 'image.freepik.com', 'img.icons8.com')
CSP_SCRIPT_SRC = ("'self'", 'paulkiragu621.github.io', 'ajax.googleapis.com', 'image.freepik.com', 'https://img.icons8.com')
CSP_IMG_SRC = ("'self'", 'paulkiragu621.github.io', 'image.freepik.com', 'img.icons8.com')
CSP_FONT_SRC = ("'self'", 'paulkiragu621.github.io', 'image.freepik.com', 'img.icons8.com')
CSP_INCLUDE_NONCE_IN = ("script-src", "style-src")
# Sneak Peak

![security](https://user-images.githubusercontent.com/44939805/110807036-af6ea700-8293-11eb-970d-f293ec2fe16d.png)
![security2](https://user-images.githubusercontent.com/44939805/110807147-cb724880-8293-11eb-9ce5-1f1f5c704531.png)
