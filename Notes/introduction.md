## Django

Django follows the MVT design patter (Model View Template)
#### 1. Model
- the data you want to present, usually data from a database
In Django, data is delvered as an ORM (Object Relational Mapping), which is a techniqe designed to make it easier to work with DBs. Django, with ORM makes to easier to communicate witht eh DB without having to write complex SQL statements. The models are usually located in models.py

##### Object Relational Mapping
- addresses the bridge between OOP and relational DBs. It is useful in data interaction simplification, code optimixation and smooth blending of applications and databases. 
- In ORM, entities are synonymous with the objects or classes in OOP that are bound to tables in relational DBs. The ORM component carries out the transformation of these entities into DB tables. It provides smooth communication between the application and the database beneath it. 
The most common way tp extract data from a DB is SQL. 

#### 2. View 
- a request handler that returns the relevant template and content based on the request from the user.
A view is a function or method that takes http requests as arguments, and imports the relevant model(s), and finds out what data to send to the template. Usually views.py

#### 3. Template 
- a text file (e.g HTML) containing the layout of the web page, with logic on how to display the data (in model)
A template is a file where you describe how the resilt should be displayed/represented. They are often .html files but can also be in other formats to present other results. 

Django uses standard HTML to describe the layout, but uses DJango tags to add logic. The templates of an application are often located in a folder named templates


Once all installations are complete, here's what happens

1. Django receives the url, checks the urls.py file and calls the view that matches the url
2. The view, located in viewspy, checks for relevant models.
3. The models are imported from models.py
5. The temoplate contains HTML and Django tags, and with the data it returns finished HTML content back to the browser



### Project = The whole website/configuration
- the container that holds settings, urls routing, and ties everything together
- you typically have one project per website

### App = a specific feature or functional piece of that website
- meant to do one thing well. e.g blog, users, payments
- contains its own models, views, urls, admin 
- a project can and usually does contain many apps.

*Analogy: think of the project as a restaurant, and apps as departments: kitchen, bar, front-of-house. Each deparment handles its own stuff, but they all operate under one same roof (the project) and share the same overall settings (like business hours, address, etc).*
