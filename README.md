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

Then, go to http://localhost:8000/admin in your browser of choice. Sign in with the same details that you used to create the superuser.

## Images

### Register/Login Screens

![Registration screen](docs/assets/auth/registration.png)
![Login screen](docs/assets/auth/login.png)

### Homepage Screen

![Homepage 1](docs/assets/homepage/1.png)
![Homepage 2](docs/assets/homepage/2.png)
![Homepage 3](docs/assets/homepage/3.png)

### Opportunity Screens

![Opportunity 1](docs/assets/opportunity/1.png)
![Opportunity 2](docs/assets/opportunity/2.png)
![Opportunity 3](docs/assets/opportunity/3.png)
![Opportunity 4](docs/assets/opportunity/4.png)

### Profile Screens

![Profile 1](docs/assets/profile/1.png)
![Profile 2](docs/assets/profile/2.png)
