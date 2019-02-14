
Introduction :
This is my first project in Full stack nano degree at udacity
it’s review my skills in their course
“the Relational Databases course”

Download the data base :
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Overview :
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, my code will answer questions about the site's user activity.

Questions are :
    • Most popular three articles of all time.
	
    • Most popular article authors of all time. 	
	
    • Days on which more than 1% of requests lead to errors. 
    
    
The database includes three tables:
    • Authors table 	
	
    • Articles table 	
	
    • Log table 	

    
Technologies that am used in :
1- vagrant
2-virtualBox
3-python3
4-sublime3 Editor and pycharm
5- pyschog2 lib
6- unix shell “linux terminal”
7- use programe that style the code format 





First to Run

Download the data base :
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip



then launch Vagrant VM by running vagrant up, then log in with vagrant ssh
To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.

to connect a database and run the necessary SQL statements
Run python3 logs.py and the output will be displayed in terminal

If you'd like to revert the news database to its original form, you can do that by dropping each of the tables, then re-importing the data from the newsdata.sql file.

In psql:

drop table log;
drop table articles;
drop table authors;


Python file (logs.py) contain those steps :
#making a function to handle the queries
# 1- answering the first question : What are the most popular three articles of all time?
# 2- answering the second question : Who are the most popular article authors of all time?
# 3- answering the second question : which days did more than 1% of requests lead to errors?
#Functions for print each query
#print the result
# To show result  Run in both pycharm and  in terminal by → $ python logs.py



