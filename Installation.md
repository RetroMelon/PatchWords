# Patchwords installation guide

An installation guide for patchwords, detailing the software dependencies and method.

#Dependencies
 - Django 1.7
 - Django Registration Redux 1.1
 - Pillow 2.7
 - argparse 1.2
 - wsgi ref 0.1.2
 
#Method

Clone the project from the repo using:

`git clone https://github.com/retromelon/patchwords`

A folder named patchwords with the readme, requirements, patchwords_project folder, etc. should appear in the current directory.

Make the patchwords folder into a virtual environment:

`virtualenv patchwords`

Navigate in to the "patchwords" folder and activate the virtual environment:

`source bin/activate`

Install the dependencies from the requirements.txt file using pip:

`pip install -r requirements.txt`


Django and the other requirements are now installed. Navigate in to the "patchwords_project" folder and create the database:

`python manage.py migrate`

Populate the database with some initial test users and categories using the population script:

`python production_populate.py`

The django server is now ready to run using:

`python manage.py runserver`

NOTE: If the webapp is running in production, it is worth generating a new secret key for the `settings.py` file. The allowed_hosts should also be changed according to the address the app is being hosted on.
