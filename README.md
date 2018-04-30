# Contents

news.py is a python file using the Python DB-API to connect to the newsdata.sql database in order to perform log analysis.

3 questions are answered in the file:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Run the file by navigating to the repository directory and run:
```
python news.py
```

## Views

Two views were created in psql to make the queries a bit easier to digest.

### Errors View
```
create view errrs as select date(time), count(*) as errors
from log where status = '404 NOT FOUND'
group by date;
```

This view creates a table of total errors in navigating the website grouped by day

### Hits View
```
create view hits as select date(time), count(*) as hits
from log group by date;
```

This view creates a table of total hits by day
