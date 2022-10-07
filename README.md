# library
create a django application for learning a CRUD operation.
Python web app creation flow.

1-create new environment.
  python3 -m venv <environment_name>
2-active environment
  source <environment_name>/bin/activate

3-create new project
	django-admin startproject <project_name>
	cd project_name

4-migrate the application.
	python3 manage.py makemigrations
	python3 manage.py migrate

5-create a new app in project directory.
	python3 manage.py startapp <app_name>

6-create a new folder static and template for html view.
	add application into project/setting.py in INSTALLED_APPS(array)
    '<app-name>.apps.HomeConfig'
  add template into project/setting.py in template(array)
    'DIRS': [BASE_DIR / "templates"],

7-create superadmin user.
python3 manage.py createsuperuser
