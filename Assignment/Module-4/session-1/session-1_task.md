											SESSION - 1

1. Explore the folder structure of your 'foodiehub_project' and write down the purpose of each key file: manage.py, settings.py, urls.py, wsgi.py, and asgi.py.
-->
1. manage.py
`manage.py` is a command-line utility that helps manage the Django project. It is used to run the development server, create new apps, apply database migrations, create a superuser, and execute other Django management commands.

2. settings.py
`settings.py` contains all the configuration settings for the Django project. It includes database configuration, installed apps, middleware, templates, static files, security settings, and other project-wide options.

3. urls.py
`urls.py` is responsible for handling the project's URL routing. It maps URLs to their corresponding views, allowing Django to display the correct page when a user visits a specific URL.

4. wsgi.py
`wsgi.py` provides the WSGI (Web Server Gateway Interface) application for the project. It is mainly used when deploying the Django application on traditional web servers such as Gunicorn or uWSGI.

5. asgi.py
`asgi.py` provides the ASGI (Asynchronous Server Gateway Interface) application for the project. It supports asynchronous features such as WebSockets, real-time communication, and async views, making it suitable for modern Django deployments.

----------------------------------------------------------------------------------------------------------------------------

2. Write a short comparison  between Django and Flask, focusing on features and use cases for each. Use an example app you use daily (like Instagram or Zomato) to explain which framework would be better and why.
-->Comparison Between Django and Flask:

Feature: Framework Type
Django: Django is a high-level, full-featured Python web framework.
Flask Flask is a lightweight and minimal Python web framework.

Feature: Built-in Features
Django: It provides built-in authentication, admin panel, ORM, security, form handling, and many other features.
Flask: It provides only basic features. Additional functionality can be added using extensions.

Feature: Development Speed
Django: Faster for developing large and complex applications because many features are already available.
Flask: Faster for small applications, but large projects require more manual setup.

Feature: Flexibility
Django: It follows a fixed project structure, making development organized.
Flask: It is highly flexible, allowing developers to organize the project as they prefer.

Feature: Best Use Cases
Django: Best for large applications such as social media websites, e-commerce platforms, and content management systems.
Flask: Best for small websites, REST APIs, prototypes, and microservices.

Example: Instagram

Instagram is better suited for Django because it requires user authentication, database management, security, media uploads, and the ability to handle millions of users. Django provides these features by default, making development faster, more secure, and easier to maintain. Flask is more suitable for small applications or APIs where only basic functionality is required.

----------------------------------------------------------------------------------------------------------------------------------------------


