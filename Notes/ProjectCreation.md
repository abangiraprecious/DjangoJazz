3. Start project <br>
python3 -m django startproject oas_bay . 
- oas_bay can be whatever project name you choose
- the . puts the manage.py file outside (in the current folder) and not in the project folder

4. Run server <br>
python3 manage.py runserver <br>

control c to stop server 

5. Create App <br>
python3 manage.py startapp appname <br>

This creates the app and multiple files and folders with a specific meaning. <br>
views.py is where we gather the information we need to send back a poper response   