# django-user-model-boilerplate
This is a boilerplate repository for a backend in Django, user model is ready to use. You can use classes like IsAdmin to create authenticated endpoints.

## Development environment build-up
### Prerequisites
- Python 3.10
- Git
- Docker
- Make (optional)
- Pycharm or VsCode (optional)
- Postman (optional)
- PgAdmin (optional)

### Steps to run dev server
Before start, create a virtual environment and activate it. You can use your IDE, virtualenv or pipenv.

Install dependencies inside the virtual environment `pip install -r requirements.txt`

Make sure you have docker installed and running. You can check it by running `docker ps` command.

Make sure you have a `.env_dev` file in the root directory. You can get it from team-mates.

Next step is to run make script to start the postgres instance in docker. This will create a docker instance and 
run the postgres server in it. You can also run the docker command inside the make file to run the postgres instance.
The postgre instance will cahce the data into your local folder under `.docker` folder. 
You can use pgadmin to view the database or use another tool of your choice. The next step is to run the django server.
You can run the django server in debug mode `python manage.py runserver`, create a debug configuration on your IDE choice.



You can configure your IDE to run on debug mode. Show the `manage.py` as the script path and `runserver` command
as the parameter.d
