# Django Blog

This project is a simple articles/categories blog developed with **Visual Studio Code**, using **Django**, **JQuery** and **BootStrap**. The project has been developped using the two web design patterns **REST** and **MVC**. The **REST** classes are in the file *blog/views.py*. The controllers have been implemented with **JQuery** under *blog/static/js/*, the views with **BootStrap** under *blog/templates* and the model with **Django** under *blog/*. The **AJAX** implementation method has also been used for not loading a new page at each request.

## Dependencies

Both **JQuery** and **BootStrap** are already included to the projects.

First of all, you need to make sure that **Python 3** and **PIP** are present on your system. For Debian-based systems, run the following :
```bash
sudo apt install python3 && sudo apt install python3-pip
```
or for macOS users :
```bash
brew install python3
```

Then, you must install **Django**.

For Debian-based systems :
```bash
sudo pip3 install django
```
For macOS users :
```bash
pip3 install django 
```

## Usage

In order to run the project, simply run the *manage.py* file.
```bash
python3 manage.py runserver
```

You will then be able to connect to *localhost:8000*. The articles/categories and the links between the categories and articles can be added using the admin login page. An admin user is already created with the credientials login=*admin* and password=*admin*. On the home page, a search is available on the categories, and on any text pattern in the article. They are sorted from the most recent to the latest. A page indexing has been done to facilitate the navigation. The article details can be reached click on the button *Read more*.
