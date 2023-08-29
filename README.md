Continuing Professional Development Diary


CLEARED BOILERPLATE README

TODO
ADD PLANNING / AGILE
ERD DIAGRAM
TESTING.MD
DESIGN / WIREFRAMES


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

working with forms 
https://docs.djangoproject.com/en/3.1/topics/forms/#working-with-form-templates

mixin messages
https://www.youtube.com/watch?v=pOXqvzVCeSM

getbootstrap
https://getbootstrap.com/

bootstrap cheat sheet
https://getbootstrap.com/docs/5.0/examples/cheatsheet/

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


user stories
i want to have a user arrive at the site, be given the choice to log in / register
on the individual login, they can enter a diary entry
that will save, and they can see their previous entrys

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
corrected some mispellings, added DISABLE_COLLECTSTATIC to config vars on heroku (this may cause issues with static files but that will be address when needed)


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