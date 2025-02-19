# Bord's Weblog Hosting Site by Team Bord

## Roster with Roles:
Justin Zou, Hebe Huang: Styling (CSS)

Austin Ngan: Creation/editing blogs (Python and Database)

Mark Zhu: Personal blog page and blog pages of others (HTML templates and Flask to connect the database to the webpage)

Roshani Shrestha: Login/Register Page (HTML templates and Flask sessions)

Thomas Yu (Project Manager): Assisting with HTML templates and database work (user accounts and blogs)

## Notable things involving CSS:
- Commentting can be done with `/* <COMMENT> */`
- We can add in animations with the transition keyword with the keyframes auto generated  
    - We can also use the animation property and `@keyframes`
- We can see if a user has clicked a text area with :focus which can give us different results  
- We can use :not to specify elements that are not in a certain state  
    - ie `input:not(:focus)`
- We can select HTML elements by their attributes   
    - ie differentiating input types with `input[type = ""]`
- The ordering of CSS rules matters. If multiple rules on the same property of the same element are declared, the last rule declared is the one applied.  
    - There are more rules on precedence: http://tutorials.jenkov.com/css/precedence.html

## Description of Website/App:
Bord's Weblog Hosting Site allows the user to create their own blogs and view the blogs of others. To use Bord's Weblog Hosting Site, you need an account, so make sure to register! Logging in takes a user to their personal blog page, where they can create a new blog or view an old one. Within each blog they can add, edit, and remove entries. They are also able to edit or remove the blog itself. Lastly, users are able view the blogs and blog entries of other users.

## Launch Codes
Launch Virtual Environment:

To create a virtual environment run the command:

`$ python3 -m venv <path_to_virtual_environment>`

Activate the Virtual Environment:

`$ . <path_to_virtual_environment>/bin/activate`

If your machine uses Windows, replace `bin` with `Scripts`


Clone the Repository:

`(venv) $ git clone https://github.com/thomasyu21/Team-Bord-p00.git`


Change Directory and Install Requirements

With a virtual environment launched, run the commands:

`(venv) $ cd Team-Bord-p00`

`(venv) $ pip3 install -r requirements.txt`


Change Directory and Run Python Script:

`(venv) $ cd app`

`(venv) $ python3 __init__.py`


Open webpage at http://127.0.0.1:5000/
