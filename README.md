# b.well Django challenge

#### Summary:
Load a public dataset from into a SQLite database and build a RESTful API interface using Django REST Framework in Django version 4.02 and Python3.9.

#### Dataset:
- Baseball Player Data

#### Requested tasks:
- [x] For the dataset above, download the data in an appropriate dataset file and evaluate the contents
- [x] Create a Django app to serve information about each player
- Create models in a SQLite database to hold the data with the following conditions:
- [x] Write a management command or migration to load the data from the dataset file into the database using the models
- Create REST-ful endpoints via Django REST Framework which provide the following:
  - [x] Detail page for a facility with all data
- [x] Please try to write all API end-points to be as performant as possible while still using the Django ORM
 > 1. using select_related, prefetch_related for joining querysets to avoid issues with nested serializers where
 extra hits to database might inadvertently occur.

 > 4. performance monitoring - Overrided dispatch method to count number of hits to db to confirm. This shows up on django server output under ***** # of Queries: 3 *********
 > 5. performance monitoring - django-debug-toolbar will show up on the right side of browser and even show you sql queries executed

#### Stretch goals:
- [x] Paged listing of facilities with subset of data with 50 results per page
 > Done automagically, using pagination library.

- [x] Write unit tests for all above end-points and CRUD operations

#### Please deliver a zip file containing:
- Your Django project in its own directory
- A copy of your SQLite database with all data loaded
- A requirements.txt file
- [x] Instructions on how to load the data, and a brief explanation of how to use the API endpoints

  > Place the CVS input file in data directory located in baseDir of application.

  > 0. delete db.sqlite3, player/migrations/0001_initial.py because player table uses primary key.
  > 1. python manage.py makemigrations
  > 2. python manage.py migrate --run-syncdb
  > 3. python manage.py uploadcsv --filename PlayerData.csv
  
  > Read the data
  > 1. python manage.py shell
      Python 3.9.9 (main, Nov 21 2021, 03:23:42) 
      [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
      Type "help", "copyright", "credits" or "license" for more information.
      (InteractiveConsole)
  > 2. >>> from player.models import Player
  > 3. >>> Player.objects.all()
  > 4. >>> p = Player.objects.get(pk="abadijo01")
  > 5. >>> p.playerID
  > 6. >>> p.birthYear

  > Setting up admin
  > 1. python manage.py createsuperuser
  > 2. provide user/password admin/admin

  > 1. I have included postman collections in the postman folder under the base dir
  > 2. API endpoints can also be tested using Swagger document, make sure django application is running.
  [Swagger document ](http://localhost:8000/swagger/)


- [x] Any docker file or other manifest file that would help us run the application
> 1. docker build .
> 2. docker-compose up

- A document in which you describe the following:
  - [x] What assumptions you made, and how those assumptions might affect the project.

   > I begrudgingly created records using update_or_create option. I also added warning prompt for user that they were reloading on top of existing data, since a reload would wipe out any manual updates.

   > 2. Versioned the url **api/v1/facilties** for possible future version changes.

   > 3. Could not do a prefetch on the update method in Serializer because I could not save updates on the loc/desc tables. I ended up doing a separate Fetch for each object.

    
  - [x] Any trade offs you made based on the assumptions above.

   > 1. To save time, I didnt research further if the later records were truly updates or not because the
     use case of this test doesnt specify that data needs to be accurate realtime. Normally at work I would
     take the time and do the proper research to confirm that data integrity is not jeopardized.

   > 2. In regards to performance testing, some people say that it is better to wait until your website recieves
     alot of traffic before you implement - premature optimization. Adding indexes and cache seems like overkill
     on this project but would definitely make more sense on a production website, but cache in memory will be 
     expensive form of horizontal scaling and has to be evaluated properly while indexing will require more disc space.

   > 3. Viewsets over Views really made a difference for me. It helped development time and encouraged me to rely on
     the best practices inherent in how serializers are setup and called and still allows me to configure the queryset
     for different use cases. The concept of Dry is a big win for me in this case.





  - [x] The most difficult aspect of the project.

  > Nothing really difficult, because instructions were very clear and explanations were meaningful.

  >  1. I had some difficulty getting nested serialization to work in the viewset. 
  > Finally figured out I needed a many=True kwargs to make it work. Also doing create/update 
  > in serialization with nested data required some thought.








