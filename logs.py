#!/usr/bin/env python
import psycopg2


DBNAME = "news"

# making a function to handle the queries


def make_query(query):

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()

# 1- What are the most popular three articles of all time?
query1 = (""" select title,count(*) as num from articles,log where
              log.path=CONCAT('/article/',articles.slug)
              group by articles.title order by
              num DESC limit 3; """)

# 2- Who are the most popular article authors of all time?
query2 = ("SELECT authors.name, count(*) as views"
          "     FROM articles JOIN authors ON"
          "     articles.author = authors.id"
          "     JOIN log ON articles.slug = substring(log.path, 10)"
          "     WHERE log.status LIKE '200 OK' "
          "     GROUP BY authors.name ORDER BY views DESC;")

# 3-which days did more than 1% of requests lead to errors?
query3 = (" select * from ("
          "  SELECT TO_CHAR(date, 'Mon DD, YYYY'),round(100.0*sum(case log.status"
          "  when '200 OK'  then 0 else 1 end)/count(log.status),3) as error"
          "  from log group by date(time)"
          "  order by error desc) as subq where error > 1; ")


# Functions for print each query

def print_query_1(query):
    results = make_query(query)
    print('\n1. The 3 most popular articles of all time are:\n')
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + '   views')


def print_query_2(query):
    results = make_query(query)
    print('\n2. The most popular article authors of all time are:\n')
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + '   views')


def print_query_3(query):
    results = make_query(query)
    print('\n3. Days with more than 1% of request that lead to an error:\n')
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + '   %')

# print the result
print_query_1(query1)
print_query_2(query2)
print_query_3(query3)
