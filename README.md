## django_button
### How to run project:
* Create folder for project
* Create virtual environment for python3: virtualenv nameofvenv
* cd nameofvenv
* Clone repo in created folder: git clone https://github.com/Bonskeeper/django_button.git
* Install requrements: pip install -r requirements.txt
* Create database for project: python manage.py migrate
* Start web-server: python manage.py runserver
### Descriprion:
It's just a button. If u push the button it sends post-request with hard-coded parameters and saves response. All responses will be displayed in table below the button.
If you want to see response with error - change one or more of first four parameters in variable "new_order" in file "views.py".
