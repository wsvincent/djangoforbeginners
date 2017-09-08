# Django Hello World App
Code for creating a Django "Simple app". Read table the full tutorial at [Django for Beginners: Chapter 3](https://djangoforbeginners.com/book/chapter-three/).

## Quick Setup
1) Clone the repo to your computer

```
$ git clone git@github.com:wsvincent/djangoforbeginners/ch3-simple-app.git
```

2) Create and enter a new virtual environment

```
$ python3 -m venv ~/.virtualenvs/simple
$ source ~/.virtualenvs/simple/bin/activate
```

3) Install the requirements

```
$ pip install -r requirements.txt
```

4) Run the local webserver

```
$ python manage.py runserver
```

5) Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about) to see the result.

![Homepage](https://djangoforbeginners.com/assets/images/book/03_staticpages_homepage_header.png)

![About page](https://djangoforbeginners.com/assets/images/book/03_staticpages_about_header.png)
