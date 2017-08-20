#! /usr/bin/env python3

import psycopg2
DB = "news"

# 1. What are the most popular three articles of all time?

query1 = (
    "select title, count(*) as views "
    "from articles join log on log.path "
    "like concat('%', articles.slug) "
    "where log.status like '200%' "
    "group by title, log.path "
    "order by views desc limit 3")

query_1 = dict()
query_1['title'] = "\n1.The most popular three articles of all the time are:"

# 2. Who are the most popular article authors of all time?

query2 = (
    "select name, count(*) as views from articles "
    "join authors on articles.author = authors.id join log "
    "on log.path like concat('%', articles.slug) where "
    "log.status like '200%' group "
    "by name order by views desc")

query_2 = dict()
query_2['title'] = "\n2.The most popular article authors of all the time are:"

# 3. On which days did more than 1% of requests lead to errors?

query3 = (
    "select * from (select date(time),round(100.0*sum(case log.status "
    "when '200 OK'then 0 else 1 end)/count(log.status),2) as "
    "\"Error\" from log group by date(time) "
    "order by \"Error\" desc) as final where \"Error\" > 1")

query_3 = dict()
query_3['title'] = "\n3.Days more than 1% of request that lead to an error:"


def get_result(query):
    # returns results
    db = psycopg2.connect(database=DB)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_results(query_result):
    # print results
    print (query_result['title'])
    for view in query_result['results']:
        print ('\t' + str(view[0]) + ' - ' + str(view[1]) + ' views')


def print_error_results(query_result):
    # print errors result
    print (query_result['title'])
    for view in query_result['results']:
        print ('\t' + str(view[0]) + ' - ' + str(view[1]) + '% errors')


# store results

query_1['results'] = get_result(query1)
query_2['results'] = get_result(query2)
query_3['results'] = get_result(query3)


# print output

print_results(query_1)
print_results(query_2)
print_error_results(query_3)
