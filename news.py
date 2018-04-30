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

query3 = "select hits.date, count(*) as high_errors from hits, errors \
where hits.date = errors.date and errors.errors > (0.01 * hits.hits) \
group by hits.date;"


def get_top_articles():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query1)
    result = c.fetchall()
    db.close
    return result

print(get_top_articles())


def get_top_authors():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query2)
    result = c.fetchall()
    db.close
    return result

print(get_top_authors())


def get_errors():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query3)
    result = c.fetchall()
    db.close
    return result

print(get_errors())
