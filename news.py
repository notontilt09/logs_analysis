#!/usr/bin/env python 3
import psycopg2

""" 1. What are the most popular three articles of all time?"""

query1 = "select articles.title, count(*) as views from \
articles, log where '/article/' || articles.slug = log.path \
group by articles.title order by views desc limit 3;"

""" 2. Who are the most popular article authors of all time? """

query2 = "select authors.name, count(*) as views from authors, articles, log \
where log.path = '/article/' || articles.slug and authors.id = \
articles.author group by authors.name order by views desc;"

""" 3. On which days did more than 1 percent of requests lead to errors"""

query3 = "select errors.date, ROUND(errors.errors*100/hits.hits::numeric, \
2) as percentage_of_errors from errors, hits where errors.date = hits.date \
and (errors.errors*100/hits.hits::numeric) >= 1;"


def get_top_articles():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query1)
    result = c.fetchall()
    db.close
    x = result[0][0] + " - " + str(result[0][1])
    y = result[1][0] + " - " + str(result[1][1])
    z = result[2][0] + " - " + str(result[2][1])
    print(x)
    print(y)
    print(z)
    return ""


print("Top 3 Articles by Views")
print(get_top_articles())


def get_top_authors():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query2)
    result = c.fetchall()
    db.close
    x = result[0][0] + " - " + str(result[0][1])
    y = result[1][0] + " - " + str(result[1][1])
    z = result[2][0] + " - " + str(result[2][1])
    zz = result[3][0] + " - " + str(result[3][1])
    print(x)
    print(y)
    print(z)
    print(zz)
    return ""


print("Top Authors by Article Views")
print(get_top_authors())


def get_errors():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query3)
    result = c.fetchall()
    db.close
    return str(result[0][0]) + " - " + str(result[0][1]) + "% errors"


print("Days with Over 1% page view errors")
print(get_errors())
