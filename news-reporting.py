#!/usr/bin/env python3

import psycopg2

DB_NAME = "news"

pop_article = (
    "select title, count(*) as views "
    "from articles join log on log.path = concat('/article/', articles.slug) "
    "where log.status like '%200%' "
    "group by title order by views desc limit 3")


pop_author = (
    "select authors.name, count(*) as views "
    "from articles join authors on authors.id = articles.author "
    "join log on log.path = concat('/article/', articles.slug) "
    "where log.status like '%200%' group by name order by views desc")


error_request = (
    "select error_request.date, "
    "error_request.views * 100.0 / total_request.views as error "
    "from total_request join error_request on "
    "total_request.date=error_request.date "
    "where error_request.views * 100.0 / total_request.views >1.00")


def connect_result(query):

    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    analys = c.fetchall()
    db.close()
    return analys


def print_article(analys):
    print ("\nI. Three most popular articles all time:\n")
    for i in range(len(analys)):
        print ("  " + str(i+1) + ". " + analys[i][0] +
               " - " + str(analys[i][1]) + " views")


def print_author(analys):
    print ("\nII. Most popular authors of articles all time:\n")
    for i in range(len(analys)):
        print ("  " + str(i+1) + ". " + analys[i][0] +
               " - " + str(analys[i][1]) + " views")


def print_error(analys):
    print ("\nIII. Most error occurred day all time:\n")
    for i in analys:
        print "  " + str(i[0]) + " - ", round(i[1], 2), "% errors"

print_article(connect_result(pop_article))
print_author(connect_result(pop_author))
print_error(connect_result(error_request))
