# Local Installation

To view the working code locally on your computer, first clone the entire repo.

```
$ git clone https://github.com/wsvincent/djangoforbeginners.git
```

Then `cd` into the directory of your choice. Start the local pipenv environment `pipenv shell` and install local packages `pipenv install`. Then you can use `./manage.py runserver` to run the code locally at [http://localhost:8000/](http://localhost:8000/).

For example, to try out Ch4: Message Board app you'd execute the following commands

```
$ cd ch4-message-board-app
$ pipenv shell
(mb) $ pipenv install
(mb) $ python manage.py runserver
```

Make you type `exit` when done leave your virutal environment.

Any issues? Please submit an issue!
