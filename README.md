# LinkPlant
A link-in-bio tool like Linktree that allows you to create a webpage that has all your links in one place.

You'll be able to create, edit, and delete links and create a landing page that displays all your links to share with the world!

- Built-in class-based generic views
- Generic editing views


![1](https://github.com/Terieyenike/django-projs/assets/25850598/acf58661-9234-4827-93c2-f8b14bdaa63e)
![2](https://github.com/Terieyenike/django-projs/assets/25850598/0f2088ae-2a1d-42fb-86b8-e73f6202977c)
![3](https://github.com/Terieyenike/django-projs/assets/25850598/d72c59b0-0612-4fe7-942c-85fc93e2231b)
![4](https://github.com/Terieyenike/django-projs/assets/25850598/9270ebb2-f038-450a-b22d-73f2027404d2)
![5](https://github.com/Terieyenike/django-projs/assets/25850598/6c364487-e738-4135-a880-e5b9f6257152)

## Tech stack
Django

## How to upload Django Project to Render.com

#### 1. Visit the render.com website and make an account.
#### 2. Select PostgreSQL from the New+ dropdown.
![image](https://github.com/Terieyenike/linktree/assets/57314456/a4519ecf-14b2-4799-a5fc-a7c5ef5e4582)

#### 3. Give a name to that database and then create the database
#### 4. Click on Connect and copy the External Database URL
#### 5. Now go into your project and in settings.py file, download and import dj_database_url
```
pip install dj-database-url
```
#### 6. Now search for DATABASES = {} and below that write down this code
```
DATABASES["default"] = dj_database_url.parse("your External Database URL")
```
#### 7. Then install psycopg2 or psycopg2-binary in your project
```
pip install psycopg2
pip install psycopg2-binary
```
#### 8. Migrate your project, this will admit all the changes made to your project
```
python manage.py migrate
```
Now your database has been connected and now you can check it by using and Postgres application.
#### 9. Now store all your variables in env file so that it doesnt get leaked when you deploy this web service to the internet
#### 10. after making env file and settings things up. now again go to render.com and click new+ to deploy Django application
#### 11. Select the web services options and select the repo in which this project is stored.
#### 12. Now, name the project, choose the runtime language, and also set the build command for the service to run on that server.
#### 13. Now go to your project and also install Gunicorn package first and then push the changes to the GitHub.
```
pip install gunicorn
pip freeze > requirement.txt
git add .
git commit -m "add gunicorn"
git push
```
#### 14. Now in render.com set the start command as "gunicorn project_name.wsgi" as name in the folder of your project
![image](https://github.com/Terieyenike/linktree/assets/57314456/9c12fbfc-315c-4346-8703-b879eeeaecf8)
in this case "linktree" is the name
```
gunicorn linktree.wsgi
```
#### 15. Now click on create Web Service button and now as it deploy there can be some bugs , so fix it on the go, according to your requirements.

Contribute to the page if you need to by cloning this project, raise an issue, or submit a PR.
