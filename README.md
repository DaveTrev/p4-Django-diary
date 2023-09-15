# Eye|Contribute - CPD Diary
(Developer: David Trevaskis)

![Mockup image](static/Media/amiresponsive.png)

**Live Site:**

[Live webpage](https://cpddiary-bd5599156530.herokuapp.com/)

**Link to Repository:**

[Repository](https://github.com/DaveTrev/p4-Django-diary)

**Developed by: David Trevaskis**

- [EyeContribute Diary](#EyeContribute-diary)
  - [Table of Content](#table-of-content)
  - [Introduction](#introduction)
    - [Project Goals](#project-goals)
    - [Data Base Design](#data-base-design)
   - [User Experience - UX](#user-experience)
   - [User Stories](#user-stories)
   - [Agile Methodology](#agile-methodology)
   - [The Scope](#the-scope)
  - [Agile Development](#agile-development)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Python Modules \& Packages](#python-modulespackages-used)
    - [Frameworks \& Tools](#frameworks--tools)
  - [Testing and Validation](#testing-and-validation)
  - [Deployment \& Development](#deployment--development)
  - [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
  - [Acknowledgements](#acknowledgements)


## Introduction


Introduction

Eye|Contribute Cpd Diary is a simple online diary to log continued education for Dispensing Opticians and Optometrists in Ireland. Under the regulatory body CORU, each member must keep a diary of all learning carried out in a year.

On registration with Eye|Contribute, it allows each user to create a personal journal of their learning activities and track their cpd credits in a easy to follow centralised manner.
Each diary entry, covers the information required by CORU, such as time spent and activities undertaken.

Users can set up an account that allows them to add, edit and delete entries. 
The project was designed as the 4th portfolio project of the Code Institutes Full Stack Diploma Program. It was built using

-   Django
    
-   Python
    
-   Js
    
-   CSS
    
-   HTML
    
-   Postgresql

### Project Goals

The goal of the project was to fulfil a need (and want) in my life as a Dispensing Optician, to build an easy to use online diary for logging continued learning for optical professionals.
Each diary entry must have the correct layout as required by the regulations set out by CORU.
The site allows users to register and create private diary entries, the purpose, to collate and log all learning undertaken in a simple to use digital diary.
Each diary enter is private to that specific user, only they can create, edit or delete entries.
My main objective was to make this  as mobile friendly as possible, enabling users to log conversations, topics they have encountered on their day in practice easily. 

### Data Base Design

The Entity Relationship Diagram (ERD) shows the database's structure, which is essential to this site's functionality:

![ERD](static/Media/erd(no_background).png)

A User Model is provided by Django, Allauth is used to handle registration and user authentication. The custom model "Entry" is used to log entries to the CPD diary.

The fields required by the Entry model is as follows.

-   Date (Automatically generated from the day of entry)
    
-   Title
    
-   Learning outcome
    
-   Activity type
    
-   Cpd credits
    
-   Time spent
    
-   Impact on practice.

A `User` Model is provided by Django, and the `Entry Model` stores the details of users CPD diary entries. The user can add many additions to their diary, in order to store notes to refer back to should they need it. 

The `Entry` model is based on the personal diary walkthrough project by Real Python. However, the models were significantly altered to fit the needs of this project. The `Entry` model has added fields of 'Learning Outcome', 'Activity Type, 'Time Spent', 'Cpd Credits' and 'Practice Impact'. 

**Future Models**

In the future, the developer would like to add additional models, a custom user profile, allowing users to tailor their personal details on the site.

As part of the entry model, the developer would like to add an additional feature of uploading supporting documents to the diary database, to provide evidence and reference for the user.

## User Stories

* As a website user, I can:

1. As a "site user " I can register on "the site" to access features and diary.
2. As a "site user" I can see multiple options to register for the site and what its use it.
3. As a "site user " I read up on what is required with logging CPD.

* As an authenticated website user, I can:

1. As a "site user " I can create a new diary entry in the cpd log
2. As a "site user" I can edit the diary entries
3. As a "site user" I can see the previous entries made
4. As a "site user" I can delete the diary entries

## Agile Methodology


The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board which can be seen here -

[Project Board Link](https://github.com/users/DaveTrev/projects/3)

![Kanban](static/Media/kanban.png)


Through the use of the Kanban board in the projects view in Github, the project was divided into a few different sections:
* To do
* In Progress
* Done
* Future Updates

User Stories and any other project-related fixes or updates were created using Github issues.

8 enhancement features or features I would liek to add were not completed and left as Future updates to complete.

**Epic 1: User Authentication**

-   User Story 1: As a site user, I want to register on the site to access features and the diary.
    
    -   Task 1: Install Allauth
    -   Task 2: Style registration and login pages
    -   Task 3: Implement user registration functionality
  

**Epic 2: Diary Entry Management**

-   User Story 2: As a site user, I want to create a new diary entry in the CPD log.
    
    -   Task 1: Create the diary entry form
    -   Task 2: Implement diary entry creation functionality

-   User Story 3: As a site user, I want to edit my diary entries.
    
    -   Task 1: Create the diary entry editing page
    -   Task 2: Style the diary entry editing page
    -   Task 3: Implement diary entry editing functionality

-   User Story 4: As a site user, I want to see my previous diary entries.
    
    -   Task 1: Create a page to display previous diary entries
    -   Task 2: Style the diary entry display page
    -   Task 3: Implement functionality to fetch and display previous entries

**Epic 3: Site Navigation**

-   User Story 5: As a user, I want clear navigation to find the information I need.
    -   Task 1: Create a responsive navigation bar using Bootstrap
    -   Task 2: Add relevant links to the navigation bar
    -   Task 3: Test the navigation bar's responsiveness
    -   Task 4: Adjust the navigation bar for logged-in users

**Epic 4: Error Handling**

-   User Story 6: As a developer, I want to create status error templates to secure views and notify users of issues.
    -   Task 1: Create 404, and 500 error pages extending from Base.html
    -   Task 2: Style the error pages

**Epic 5: Documentation**

-   User Story 7: As a developer, I want to create documentation for fellow developers.
    -   Task 1: Write a site overview
    -   Task 2: Write a table of contents
    -   Task 3: Write sections for the table of contents
    -   Task 4: Create GIFs/screenshots of the site

**Epic 8: Testing**

-   User Story 8: As a developer, I want to create TESTING.md files.

    -   Task 1: Complete HTML, CSS, JS, and Python validation
    -   Task 2: Complete manual testing
    -   Task 3: Create screenshots for TESTING.md

**Epic 9: Deployment**

-   User Story 9: As a developer, I want to set up Django and deploy the project on Heroku.
    -   Task 1: Install Django
    -   Task 2: Create project
    -   Task 3: Create environment variables and secure them in env.py
    -   Task 4: Create an app on Heroku
    -   Task 5: Edit config vars
    -   Task 6: Link Heroku to the GitHub repository

**Epic 10: Site Design**

-   User Story 10: As a developer, I want to design a visually appealing homepage.
    -   Task 1: Design the homepage to match the site theme

**Epic 11: User Management**
-   User Story 11: As a developer, I want to provide account/profile creation functionality.

    -   Task 1: Using AllAuth, handle user registration
    -   Task 2: Implement user registration, login, and logout functionality

-   User Story 17: As a user, I want to sign up, log in, and log out to access features available to registered users.
    
    -   Task 1: Style signup, login, and logout pages
    -   Task 2: Implement user authentication functionality

**Epic 13: Footer**

-   User Story 18: Create a footer containing social links to the developer.

**Epic 14: Kanban Board**

-   User Story 19: Set up a Kanban board to track project tasks.




















Continuing Professional Development Diary


CLEARED BOILERPLATE README

TODO
ADD PLANNING / AGILE - done
ERD DIAGRAM - todo-
TESTING.MD - todo
DESIGN / WIREFRAMES - done but need to add to repo

bootstrap for mbile!
TIMEBOX doesnt indicate measurement of time!! minutes or hours?
CPD points box, adjust to whole numbers and halfs
FOOTER covers cancel box ant bottom of page


FIX NEGATIVE NUMBERS IN TIME SPENT AND CPD POints!!


add all auth instead of from django.contrib.auth.views import LoginView
https://django-allauth.readthedocs.io/en/latest/


django 3.2 

Use https://summernote.org/ for text editor for diary entry
create about page with model / possible seperate app
https://www.dennisivy.com/django-class-based-views
https://www.dennisivy.com/django-class-based-views

creating user registration, login and logout with django
https://ordinarycoders.com/blog/article/django-user-register-login-logout

dennis ivy django todo app
https://www.youtube.com/watch?v=llbtoQTt4qw

build a personal diary with django
https://realpython.com/django-diary-project-python/#step-2-adding-your-diary-entries-to-the-back-end

crud
https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp

working with forms 
https://docs.djangoproject.com/en/3.1/topics/forms/#working-with-form-templates

mixin messages
https://www.youtube.com/watch?v=pOXqvzVCeSM

getbootstrap
https://getbootstrap.com/

bootstrap cheat sheet
https://getbootstrap.com/docs/5.0/examples/cheatsheet/

bootstrap grid system
https://www.youtube.com/watch?v=Wqu-d_b3K-0

https://docs.djangoproject.com/en/3.2/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data

https://stackoverflow.com/questions/70749958/user-specific-page-in-todo-list
https://stackoverflow.com/questions/46846198/django-class-based-view-with-get-queryset
https://medium.com/@hassanraza/when-to-use-get-get-queryset-get-context-data-in-django-952df6be036a#:~:text=get_context_data(),to%20display%20in%20your%20templates.
https://rasulkireev.com/django-get-context-data/
https://stackoverflow.com/questions/49027544/how-to-properly-use-get-context-data-with-listview-to-fetch-related-instances-init 

class based views - dennis ivy
https://www.dennisivy.com/django-class-based-views

https://www.valentinog.com/blog/get-context-data/

https://djangoforbeginners.com/

DEFENSIVE DESIGN
https://forum.djangoproject.com/t/how-to-restrict-django-staff-user-to-edit-or-delete-others-staff-user-post-from-admin-panel/7887/5
https://stackoverflow.com/questions/72980454/defensive-programming-for-delete-function-in-views-django

Crispy forms how to
https://www.youtube.com/watch?v=MZwKoi0wu2Q

fade out with js 
https://stackoverflow.com/questions/6121203/how-to-do-fade-in-and-fade-out-with-javascript-and-css
https://jsfiddle.net/sunnypmody/XDaEk/

pagination with class based views
https://dontrepeatyourself.org/post/django-pagination-with-class-based-view/

pagination with filtering
https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/

pagination -> with filter and search
https://stackoverflow.com/questions/64618631/how-to-filter-and-paginate-in-listview-django

404 page how to https://www.geeksforgeeks.org/django-creating-a-404-error-page/

form validation - dark hamster
https://www.dark-hamster.com/application/how-to-display-form-error-in-django/

crispy forms how to 
https://www.youtube.com/watch?v=MZwKoi0wu2Q&t=369s

unsplash images for index page
https://unsplash.com/photos/wpi3sDUrSEk
https://unsplash.com/photos/G1iYCeCW2EI
https://unsplash.com/photos/ZI2Lv7jxmEM
https://unsplash.com/photos/6qThS1x6P6A
https://unsplash.com/photos/AjcVTjCz310
https://unsplash.com/photos/57USw1-h50k
broken glasses - https://unsplash.com/photos/jgPcjw2tBVc

used https://cleanup.pictures/ to remove pencil from picture

cropping images https://www.iloveimg.com/crop-image

Code Institute - codestar blog / I think therefore I blog lessons

user stories
i want to have a user arrive at the site, be given the choice to log in / register
on the individual login, they can enter a diary entry
that will save, and they can see their previous entrys

Potential User Stories
Install Django
Create Project
Create Environment Variables and secure (env.py)
Create App on Heroku
Edit Config Vars
Link Heroku to Github Repository
Responsive layout so its viewable on a number of devices
Clear Navigation Bar
Footer containing social links to the developer
Create and Style Sign Up/User Profile Pages
Create User Profile
View User Profile
Edit User Profile
Delete User Profile
User Login/Logout with their account details
Restrict reviewing/rating to registered users
Style Login/Logout pages
Provide alerts to indicate actions

user login / logout / signup
Task 1 - Install Allauth
Task 2 - Style pages to match site theme
Task 3 - Alter Navbar so relevant views are displayed to registered Users

NavBar 
Task 1 - Use Bootstrap to create the Navbar
Task 2 - Add relevant links for the site pages to the Navbar
Task 3 - Test responsive Navbar on Chrome Dev Tools
Task 4 - Adjust Navbar view for Logged In users i.e. Profile Link/Reviews

profile template
Task 1 - Create the Profile Page - extend from Base.html
Task 2 - Style the page to match site theme
Task 3 - Add "CTA" Buttons to allow for CRUD functionality

user profile
Task 1 - Create the model for the Profile
Task 2 - Write the view code for the Profile page
Task 3 - Add CRUD functionality to the view code

Status error page
Create 403 error page
Create 404 error page
Create 500 error page

403 page
Task 1 - Create 403 page and extend from Base.html
Task 2 - Style inline with site theme
404 page
Task 1 - Create 404 page and extend from Base.html
Task 2 - Style inline with site theme
500 page
Task 1 - Create 500 page and extend from Base.html
Task 2 - Style inline with site theme

Readme 
Task 1 - Write site overview
Task 2 - Write Table of Contents
Task 3 - Write sections for Table of Contents
Task 4 - Create Gifs/Screenshots of site

testing
Task 1 - Complete HTML Validation
Task 2 - Complete CSS Validation
Task 3 - Complete JS Validation
Task 4 - Complete Python Validation
Task 5 - Provide Unit testing
Task 6 - Complete Manual Testing
Task 7 - Create screenshots for TESTING.md

email verification
Task 1 - Update allauth email settings in settings.py
Task 2 - Update site name in Django admin view
Task 3 - Store private email keys in env.py
Task 4 - Style templates

user stories?				
As a "site user " i can register on "the site" to access features and diary				
as a "site user" i can edit my profile so that i can change my registered name and email address				
As a "site user " i can create a new diary entry in the cpd log				
As a "site user" I can edit the diary entries				
As a "site user" i can see the previous entries made				
As a "site user" I can contact the admin via a contact page				
As a Developer, I can setup Django and start project, so that I can develop the site				
As a Developer, I can deploy my site with Heroku, so that user's can view and interact with the site				
As a Developer, I can provide account/profile creation functionality, so that user can create/read/update or delete their account/profile				
As a Developer, I can provide Signup/Login/Logout functionality, so that user can safely signup/login/logout and prevent access to their profile				
As a Developer, I can design a nice aesthetically pleasing Homepage, so that the user has an enjoyable experience when navigating site				
As a User I want to see a clear way of navigating the site so that I can find the information relative to my needs	
As a User I want to Sign Up/Login and Logout so that I can see what features are available to registered users like reviewing/commenting				
As a Developer I can create an aesthetically pleasing display of the User's Profile so that the experience of viewing their Profile is a pleasant one				
As a User I would like access to my Profile so that I can upload an image or alter my details where needed				
As a Developer, I can create documentation, so that fellow developers can understand what the site is and how it was built				
As a Developer, I can create Status Error templates, so that I can secure my views and advise User when there is an issue				
As a Developer I can implement a 403 error page to redirect unauthorised users so that I can secure my views				
As a Developer I can implement a 404 error page so that I can alert users when they have accessed a page that doesn't exist				
As a Developer I can implement a 500 error page so that I can alert users when an internal server error occurs				
Create/Write README.md				
Create/Write TESTING.md				
As a Developer I can add functionality to verify email and reset password so that the user has better security over their email being used and can reset password if they forget it	


kanban board todo
inital setup intall django
deploy to heroku
admin setup
user account / profile
user signup / sign out
base html / index page
nav bar
footer
about page
contact us page
delete profile
signup login log out
profile template
user profile 
complete documentation
Status error page
403 page
404 page
500 page
Write readme.md 
write testing md




first bug
python manage.py collectstatic --noinput
       Traceback (most recent call last):
         File "/tmp/build_fdefe8ef/manage.py", line 22, in <module>
           main()
         File "/tmp/build_fdefe8ef/manage.py", line 18, in main
           execute_from_command_line(sys.argv)
         File "/app/.heroku/python/lib/python3.11/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
           utility.execute()
         File "/app/.heroku/python/lib/python3.11/site-packages/django/core/management/__init__.py", line 413, in execute
           self.fetch_command(subcommand).run_from_argv(self.argv)
         File "/app/.heroku/python/lib/python3.11/site-packages/django/core/management/base.py", line 354, in run_from_argv
           self.execute(*args, **cmd_options)
         File "/app/.heroku/python/lib/python3.11/site-packages/django/core/management/base.py", line 398, in execute
           output = self.handle(*args, **options)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         File "/app/.heroku/python/lib/python3.11/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 187, in handle
           collected = self.collect()
                       ^^^^^^^^^^^^^^
         File "/app/.heroku/python/lib/python3.11/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 105, in collect
           for path, storage in finder.list(self.ignore_patterns):
         File "/app/.heroku/python/lib/python3.11/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
           for path in utils.get_files(storage, ignore_patterns):
         File "/app/.heroku/python/lib/python3.11/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
           directories, files = storage.listdir(location)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^
         File "/app/.heroku/python/lib/python3.11/site-packages/django/core/files/storage.py", line 330, in listdir
           for entry in os.scandir(path):
                        ^^^^^^^^^^^^^^^^
       FileNotFoundError: [Errno 2] No such file or directory: '/tmp/build_fdefe8ef/static'
 !     Error while running '$ python manage.py collectstatic --noinput'.
       See traceback above for details.
       You may need to update application code to resolve this error.
       Or, you can disable collectstatic for this application:
          $ heroku config:set DISABLE_COLLECTSTATIC=1
       https://devcenter.heroku.com/articles/django-assets
 !     Push rejected, failed to compile Python app.
 !     Push failed

deploying to heroku
corrected some mispellings, added DISABLE_COLLECTSTATIC to config vars on heroku (this may cause issues with static files but that will be addressed when needed)


trying to restrict users viewing other users entries
    #def get_context_data(self, **kwargs):
        #data = super().get_context_data(**kwargs)

        #if self.request.user.is_authenticated:
            #data['user_posts'] = Entry.object.filter(user_id=self.request.user.id)

        #return data

    #def get_queryset(self):
        #return Entry.objects.filter(user_id=self.request.user.id)

       def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['entry_list'] = context['entry_list'].filter(user=self.request.user)
        #context["entry"] = Entry.objects.all()
        #return context


login = 'login' caused rooting issues
previously created custom login and logout pages, decided to install allauth, 
had to remove, customview, urls and settings code

{% extends base.html %} not working 
created a root templates folder and moved allauth's account folder into it and it appears now our allauth login.html template is connected
When we use the allauth roots in our project, if allauth can't find the templates within our workspace, it substitutes in ones without any styling


installed allauth, downloaded templates
extending base 

forms.py, custom alerts written
alerts not happening?
removing 'cpdCredits': forms.DecimalField(
                label='CPD Credits',
                widget=forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter CPD Credits'}),
                validators=[MinValueValidator(0)]),


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'required': True, 'placeholder':
                                            'Enter a Title'}),
            'learningOutcome': forms.Textarea(
                attrs={'class': 'form-control', 'required': True,
                       'placeholder': 'Enter details on your learning.'}),
            'activityType': forms.Textarea(
                attrs={'class': 'form-control', 'required': True,
                       'placeholder': 'Enter the type of activity.'}),
            'practiceImpact': forms.Textarea(
                attrs={'class': 'form-control', 'required': True,
                       'placeholder':
                       'Enter details on the impact on your practice.'}),
            'timeSpent': forms.TextInput(
                attrs={'class': 'form-control', 'required': True,
                       'placeholder': 'e.g. 3 hours',  'rows': 1, 'cols': 2}),
            'cpdCredits': forms.NumberInput(
                attrs={'class': 'form-control', 'required': True,
                       'placeholder': 'Enter CPD Credits Claimed'}
            ),
        }


    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-control'
        self.helper.layout = Layout(
            Field('title', placeholder='Enter a Title', rows=1, cols=2),
            Field('learningOutcome',
                  placeholder='Enter details on your learning.'),
            Field('activityType', placeholder='Enter the type of activity.'),
            Field('practiceImpact',
                  placeholder='Enter details on the impact on your practice.'),
            Field('timeSpent', placeholder='e.g. 3 hours'),
            Field('cpdCredits', placeholder='Enter CPD Credits Claimed')
        )
        self.helper.form_method = 'post'

            <!--https://getbootstrap.com/docs/4.0/components/forms/-->
    <div class ="form-group">
    <div class="form-group">
        <label for="{{ form.title.id_for_label }}">Title:</label>
        {{ form.title }}
        {{ form.title.errors }}
    </div>
    <div class="form-group">
        <label for="{{ form.learningOutcome.id_for_label }}">Learning Outcome:</label>
        {{ form.learningOutcome }}
        {{ form.learningOutcome.errors }}
    </div>
    <div class="form-group">
        <label for="{{ form.activityType.id_for_label }}">Activity Type:</label>
        {{ form.activityType }}
        {{ form.activityType.errors }}
    </div>
    <div class="form-group">
        <label for="{{ form.timeSpent.id_for_label }}">Time Spent:</label>
        {{ form.timeSpent }}
        {{ form.timeSpent.errors }}
    </div>
    <div class="form-group">
        <label for="{{ form.cpdCredits.id_for_label }}">CPD Credits:</label>
        {{ form.cpdCredits }}
        {{ form.cpdCredits.errors }}
    </div>
    <div class="form-group">
        <label for="{{ form.practiceImpact.id_for_label }}">Practice Impact:</label>
        {{ form.practiceImpact }}
        {{ form.practiceImpact.errors }}
    </div>
    <input type="submit" value="Save">


removed validate positive decimal
migrations failed due to missing validate positive decimal function
removed validators=[cpddiary.models.validate_positive_decimal] from timeSpent and cpdCredits migration file 7
reinstated code, as could not migrate, to return to this bug!! 


styling impacting view on mobile, timespent field, too small
footer is covering save/cancel options for user

alert messages not displaying (mispelling)

BUG TITLE FIELD NOT DISPLAYING ALERT?

installed crispy forms 
had errors, looking for uni forms?
TemplateDoesNotExist at /create/
bootstrap4/uni_form.html


Testing with 
input Date vs auto date

Used it on my phone.
Worked really well...well done you!

Feedback
I put in my name as username then set up my passwords.
When I tried to move on, my user name was rejected as I had a space in it and my passwords were deleted. I would have liked to have known in advance that I could not have spaces in my user name.
When entering a new event, the box beside time has e.g. in it. You cannot see anymore detail.
Small details from a grouchy customer...basically, very impressive!

CORU LINKS ON CPD 
https://www.coru.ie/health-and-social-care-professionals/education/continuing-professional-development/cpd-audit/
https://www.coru.ie/health-and-social-care-professionals/education/continuing-professional-development/cpd-faqs/
https://www.coru.ie/files-education/cpd/orb-guidance-on-continuing-professional-development.pdf
https://www.coru.ie/files-education/cpd/orb-support-for-continuing-professional-development.pdf