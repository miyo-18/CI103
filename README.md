(These instructions are for Windows)
-Please ensure you have Python 3.4+
(In your cloned repository)
-Use 'pip install virtualenv' if you do not already have virtualenv
-Use mkvirtualenv 'NAME' to make virtual environment
-Use the command: 'source NAME/Scripts/activate' to activate virtual environment
-Run 'pip install -r requirements.txt' to install dependencies in your virtual environment
-Run 'python manage.py runserver' to run test server on localhost:8000

Other Notes:
-To debug, change DEBUG = FALSE in settings.py to DEBUG = TRUE (NEVER DEPLOY TO HEROKU WITH DEBUG = TRUE)
-Use command 'deactivate' from anywhere to deactivate virtual environment
- You MUST be in the virtual environment for runserver to work, so when you deactivate the virtual environment you must reactivate it.