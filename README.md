# A Blog created using Django Web Framework 

## Steps to run the project locally
- Clone the project locally<br/>
``` python 
git clone url
```
- Make sure to use a virtual environment if you don't want to mess with your system<br/>
``` python 
python -m venv env 
env\Scripts\activate
```
___👆 Here env is the name of the Virtual Environment___ 
- Go to the blog folder and run the following command<br/>
``` python
cd blog
python manage.py migrate
```
- Test the app<br/>
``` python
python manage.py runserver
```
- You should see the app on your local browser on ***127.0.0.1:8000***
