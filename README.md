# Volunteering App

A prototype of an app written in Django that allows you to sign up for charity opportunities. Or, rather, a website that looks like a mobile app. I didn't have the time to make a real mobile app, sadly...

This is my first Django project, so please be nice...

## Features

- Login/Registration functionality
- The ability to sign up for volunteering opportunities
- 'Weekly streak' functionality (not really, tbh... you can only change your weekly streak by going into the admin panel yourself)

## Usage

Run the following to start all services:

```sh
git clone https://github.com/dastarruer/volunteering-app
docker compose up -d
```

Then, go to http://localhost:8000 in your browser of choice.

To get access to the admin panel (where you can add your own opportunities, play around with users, etc.), run the following to create a superuser:

```sh
docker compose exec web python manage.py createsuperuser
```

Then, go to http://localhost:8000/admin in your browser of choice.

## Images

### Register/Login Screens

![alt text](docs/assets/image.png)
![alt text](docs/assets/image-2.png)

### Homepage Screen

![alt text](docs/assets/image-1.png)
![alt text](docs/assets/image-3.png)
![alt text](docs/assets/image-4.png)

### Opportunity Screens

![alt text](docs/assets/image-5.png)
![alt text](docs/assets/image-6.png)
![alt text](docs/assets/image-7.png)
![alt text](docs/assets/image-8.png)

### Profile Screens

![alt text](docs/assets/image-9.png)
![alt text](docs/assets/image-10.png)
