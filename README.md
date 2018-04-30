# Contents

```news.py``` is a python file using the Python DB-API to connect to the newsdata.sql database in order to perform log analysis.

3 questions are answered in the file:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Setup Information
The file ```news.py``` is run inside a virtual machine using VirtualBox and Vagrant to share files between the VM and the local filesystem.

The steps below must be followed to run the log analysis code as written.

1.  Install [VirtualBox](http://www.virtualbox.org)
2.  Install [Vagrant](http://www.vagrantup.com)
3.  Fork and Clone the VM configuration from [Here](https://github.com/udacity/fullstack-nanodegree-vm)
4.  Navigate to the vagrant subdirectory from the directory created in step 3.
5.  Run ```vagrant up``` to start the VM, and wait for Vagrant to download the operating system and setup the VM (may take many minutes)
6.  Run ```vagrant ssh``` to login to the VM
7.  In the shell, cd into the ```/vagrant``` directory
8.  Download the database from [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip the file and put it into the vagrant directory which is shared with the VM
9.  Load the data by changing into the vagrant directory in the VM and using the command ```psql -d news -f newsdata.sql```
10.  Quit the psql command line program by typing ```\q```
11.  Run the log analysis file by navigating to the repository directory and run: ```python news.py```

## Views

Two views were created in psql to make the queries a bit easier to digest.

To recreate these views:
1.  From the ```/vagrant``` directory in the VM, run postgresql on the database using the command ```psql news```
2.  Copy the code from both of the views listed below.

### Errors View
```
create view errrs as select date(time), count(*) as errors from log where status = '404 NOT FOUND' group by date;
```

This view creates a table of total errors in navigating the website grouped by day

### Hits View
```
create view hits as select date(time), count(*) as hits from log group by date;
```

This view creates a table of total hits by day
