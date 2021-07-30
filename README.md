# SuperheroCreator
Django web application focused on superheroes

## Installation and use instructions
To install with git, navigate to the desired directory and run the command 'git clone https://github.com/rnandon/SuperheroCreator'

To install manually, download the .zip from the green 'Code' button. Unpack the .zip into the desired directory.

### Dependencies
There are four dependencies for this project:
- Pipenv
- Django
- MySQL Connector for Python
- MySQL Database titled 'superhero_creator'

To install Pipenv, run the command 'pip install pipenv' and follow any prompts.

To install the remaining python dependencies through the command line, open the project directory in a terminal and enter the 'pipenv shell' command followed by 'pipenv sync'. This will create a new virtual environment and install the needed packages into the environment. Note- running with different versions of these packages may cause issues.

### Setup
If not already done, download MySQL and create a database titled 'superhero_creator'. This is the local data storage referenced by the application.

A new file will need to be added to the project in order to run. Create 'local_settings.py' in '~/superhero_creator/superhero_creator'. Within this file, secret key and database objects will need to be created. To create these objects, write the following information in the file:

`SECRET_KEY = <your secret key here>

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'superhero_creator'  // Note: if you created a database with a different name, use that name here!
        'USER': <the username you registered with the install of MySQL>
        'PASSWORD': <the password you registered with the install of MySQL>
        'HOST': <the connection address of your database>
        'PORT': <the connection port of your database>
        'OPTIONS': {
            'autocommit': True
        }
    }
}`

Save the file.

Within the terminal, navigate to the outer 'superhero_creator' folder. A few more setup commands are required in order to run the application.

Run the command '$ python manage.py migrate' to create the necessary tables in the database.
Run the command '$ python manage.py createsuperuser' and follow the prompts to add a new local admin.

### Launch the application
At this point, the setup procedure should be complete. Run the command 'python manage.py runserver' to launch the application. If setup was successful, a message should appear with the line 'Starting development server at <local address>'. Enter this address into the url bar of a browser, and explore the application!


### Application usage
On the first launch of the program, there will be no heroes to display on the home page. As new heroes are created, this page will update and display the names of all available heroes. Clicking on the name of a hero will bring you to a detail page, where all the supplied information about that hero is displayed, alongside an edit, delete, and select new hero button.

To create a new hero, click the "Create New Hero" button on the home page. 
Provide the requested information about the hero, and click submit. If you would like to cancel the operation, instead click cancel.

To view the details of a hero, click the name of a hero on the main page. This will bring you to a detail screen with the information associated with that hero, along with three buttons. You can use these buttons to edit, delete, and return to the home screen.

To edit a hero, view their details and click the "Edit" button at the bottom of the page. This will bring you to an edit screen, where you can change any details about the hero you would like. Click "Update" to save the changes, or "Cancel" to return to the detail screen.

To delete a hero, view their details and click the "Delete" button at the bottom of the page. You will be prompted to verify the action before removing the hero from the database. NOTE: All deletions are permanent. Any entries removed this way will need to be manually recreated!

