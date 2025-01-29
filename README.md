This is a Django project for task management with simple fuctionality.

The project has one app register that is tasks.

 Incoming are handle by the urls file in the app, and routed to the repsective fuction in the views.py.

At the root of the project we have a folder for static fiels. Here we a have stored the htmls,images,css and java scrip  each in their repective folders.

We have an image for the background of our web pages. It is linked to the base html because all other Htmls inherit it.

We have other Html fiels each being render on a specific view for a specific purpose.
Save html gives a wep page for us to create new tasks or update the existing ones.
Tasks html list all our tasks in a clear and easy way to see.

On javascript we have one fuction in place for a adding a next line on description of a tasks in the save html page.This is to ensure we use only required space.

We have used both own css and bootsrap 5 for styling to achieve a repsonsive wep page.

******* Program logic ********

We have one model for our project, The task model with four fields.
This then creates a database table for us to store the fields data for each task.
We also have form.py with a class TaskForm this acts as an interface between our views and our model.
Forms are used to validate user in put a easy reterival of user input.
views.py  
We have two major fuctions defined in our views. One is tasks fuction used for retrieving all tasks from 
our database and rendering throug our html template to be viewed by user.
Second is the save function used to save or update tasks to the database.
