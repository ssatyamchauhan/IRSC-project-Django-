<h1 align="center">Rendering Google-Drive images directly on html-page</h1>

Hello Guys! Using nodejs I have implemented an api through which rendering google-drive images directly on html page. For google-Api authentication follow this link (https://developers.google.com/drive/api/v3/quickstart/python).
and By ExpressJs doing a get request to obtain the link of the folder's files(images link) after that using ```django.shortcuts import render``` parsing the list of the link to .ejs file to render it on html page.

## Requirements

For linux, install nodejs and npm (node-package-manager) by running following commands in your Terminal.

```
sudo apt-get update
sudo apt install python3
sudo apt install python3-pip
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

```
How to run the command on terminal

# python3 manage.py runserver

then open the chrome or any browser and run the ```http://127.0.0.1:8000/show``` you will get the photos with slider