# project_yurtah
test django project

##Инструкция по запуску(для MacOS):

Убедитесь, что версия Вашего python 2.7.15+


Создайте виртуальное окружение python3 -m venv env и активируйте его source env/bin/activate

В командной строке (в Терминале) наберите https://github.com/ainurabek/project_yurtah

Заходим через Терминал в папку project_yurtah (cd project_yurtah) и через pip необходимо установить все библиотеки из requirements.txt через команду pip install –r requirements.txt

Необходимо установить postgreSQL через команду brew install postgres, запустить через команду psql postgres, затем создать нового пользователя через команду CREATE ROLE LOGIN PASSWORD ; И после нажатия Enter должно появится CREATE ROLE

Необходимо создать новую базу данных с помощью команды CREATE DATABASE WITH OWNER = ; И после нажатия Enter должно появится CREATE DATABASE;

Заходим в папку project_yurtah/yurtah/ 

затем в Терминале там где находится файл manage.py вписать python manage.py migrate

После этого можно возвращаться к первому Терминалу и набрать там где находится файл manage.py следующую команду python manage.py runserver. Вы запустили проект локально, вы можете посмотреть пройдя по ссылке http://127.0.0.1:8000.

Далее необходимо создать суперюзера через команду python manage.py createsuperuser ввести Логин Емайл и Пароль и затем у вас появится доступ к админ странице http://127.0.0.1:8000/admin/
Затем открываем папку blog, затем файл urls.py и согласно URL-адресам проверять комнады через добавления /api/

#For Linux To run this project:

Clone this repository https://github.com/ainurabek/project_yurtah

Activate virtual environment:

 - pip install pipenv
 - pipenv --python 3
 - pipenv shell
 - pipenv install
Create private .env file inside of project directory. Copy all data from .env_example and paste inside of .env file. Note: Change the values of secrets to yours.

This project uses Postgresql, so, create Postgresql database:

sudo apt-get update sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib sudo su - postgres

Enter postgres console:

posgres psql postgres=# CREATE ROLE user LOGIN PASSWORD 'password'; CREATE ROLE postgres=# CREATE DATABASE name_db WITH OWNER = user; CREATE DATABASE postgres=# \q

Finally, run project with command: python3 manage.py runserver

Create a superuser and get into admin panel
Then we open the blog folder, then the urls.py file and, according to the URL, check the comments by adding / api /

PROFIT!
