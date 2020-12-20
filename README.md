# A Blog created using Django Web Framework for Inout 7.0

## Steps to run the project locally
- Clone the project locally<br/>
``` bash 
git clone url of repository
```
- Make sure to use a virtual environment if you don't want to mess with your system<br/>
``` bash 
python -m venv env 
env\Scripts\activate
```
___👆 Here env is the name of the Virtual Environment___ 
- Go to the blog folder and run the following command<br/>
``` bash
cd blog
python manage.py migrate
```
- Test the app<br/>
``` bash 
python manage.py runserver
```
- You should see the app on your local browser on ***127.0.0.1:8000***
