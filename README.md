# yamdb_final
Here I train using Github Actions to automatically test and deploy my project at Yandex Could.

![my badge](https://github.com/KartashevaAnna/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

The project is available through [admin panel](http://84.201.157.9/admin/).

If you wish to deploy it locally, please, clone it from https://github.com/KartashevaAnna/yamdb_final.
Create an .env file and fill it with the data to connect to Postgres as required by the settings file.
Install docker
Go to yamdb_final\api_yamdb folder.
Open the command line or git bash and run docker-compose up -d --build
Then you need to apply migrations: docker-compose exec web python manage.py migrate
After that you shall collect static: docker-compose exec web python manage.py collectstatic --no-input
Finally, you create a superuser and access the admin panel: docker-compose exec web python manage.py createsuperuser

The overall project description is available at https://github.com/KartashevaAnna/api_final_yatube/blob/master/README.md.
This is the link to the same project (without code to deploy it in docker): https://github.com/KartashevaAnna/api_final_yatube.


Stack:
Python
Django
Django REST Framework
Postgres
Simple JWT
Docker
Gunicorn
Nginx
Github actions
