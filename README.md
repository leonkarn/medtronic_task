In order to run the service you have to install Docker installed. After, start Docker and 
run the commands below:

First, run this:
~~~
docker-compose build && docker-compose up
~~~
After the services are up, try, running this command below in a new terminal (you should first run this
to try the endpoints):

~~~
docker-compose run web_app python etl.py
~~~
Try to run this until it works because the dbs might not receive connections. 

After this works and the data is ingested successfully in the analytics db, open
the local host on port 5000 so:

~~~
localhost:5000
~~~
You can the results there from analytics db.

Also you can try add a date to filter the distinct hobbies by adding it in the endpoint, like this:
~~~
localhost:5000/2019
~~~

Another endpoint is for the count that count for the year the distinct hobbies. 
~~~
localhost:5000/count/2019
~~~

We could add an extra column for the data ingestion date and do a validation if the data was 
ingested in analytics_db for the current or previous date.

To run the test, simply run :
~~~
docker-compose run web_app python test_main.py
~~~

All the endpoints are supposed to be used by the customers and only hit the analytics db
and the etl process is going to run based on schedule. 