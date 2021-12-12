# Awwards
## Author
Albunus Nyalita
### Description
This is a Django web application that allows users to view posted projects and their details. 
### Prerequisites
* Text editor eg Visual Studio Code
* You need to have git installed. You can install it with the following command in your terminal
`$ sudo apt install git-all`
*****
## Setup Instruction
To access this project on your local files, you can clone it using these steps
1. Open your terminal
1. Use this command to clone $ git clone https://github.com/albunus/Awwards
1. This will clone the repositoty into your local folder
*****
### Home page
A user is required to register and login to the application. Upon successful authentication the user is redirected to home page where all projects posted by different users is displayed.
*****
### User Profile
Every user registered in the application has profile associated with their account. Profile contains personal details and projects posted by that particular user.
*****
### View Project details
A user can click on any project image and a page will be displayed containing the project information like ratings, project title, description, live link, repository link and also date posted.  
A user can only see a delete button if they are the owner of the post so they cannot delete a post belonging to another user
*****
### Search Function
A user can search projects and it will return projects matching the search term or display "Found 0 results if no match found by the search function.
*****
