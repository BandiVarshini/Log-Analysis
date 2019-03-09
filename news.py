#! /usr/bin/env python3
import psycopg2

DBNAME = "news"


def connect(database_name="news"):
    try:
        db = psycopg2.connect(dbname=DBNAME)
        cursor = db.cursor()
        return db, cursor()
    except:
        print("<error message>")


def get_query_results(query):
    d = psycopg2.connect(dbname=DBNAME)
    cursor = d.cursor()
    cursor.execute(query)
    obtained = cursor.fetchall()
    d.close()
    return obtained

que1 = """
SELECT articles.title,
       count(*)
FROM log,
     articles
WHERE log.path = '/article/' || articles.slug
GROUP BY articles.title
ORDER BY count(*) DESC
LIMIT 3;
"""


def report1():
    d = psycopg2.connect(dbname=DBNAME)
    cursor = d.cursor()
    cursor.execute(que1)
    obtained = cursor.fetchall()
    for res in obtained:
        print('{title} = {count} views'.format(title=res[0], count=res[1]))


que2 = """
SELECT authors.name,
       count(*) AS num
FROM authors
JOIN articles
ON authors.id = articles.author
JOIN log
ON log.path like concat('/article/%', articles.slug)
GROUP BY authors.name
ORDER BY num DESC;
"""


def report2():
    obtained = get_query_results(que2)
    for row in obtained:
        print('{num1} = {num2} views'.format(num1=row[0], num2=row[1]))


que3 = """
select *
FROM (SELECT v.day,
round(cast((100*k.hits) as numeric) / cast(v.hits as numeric), 2)
as err
FROM(SELECT date(time) as day,
count(*) as hits FROM log group by day) as v
INNER JOIN (SELECT date(time) as day, count(*) as hits FROM log
where status like '%404%' group by day) as k
on v.day = k.day)
as t where err > 1.0;
"""


def Error():
    obtained = get_query_results(que3)
    for row in obtained:
        print('{num1} = {num2} % error '.format(num1=row[0], num2=row[1]))


if __name__ == '__main__':
    print("\nPopular 3 articles report\n")
    report1()
    print("\npopular 4 authors report\n")
    report2()
    print("\n Days in which more than 1% error")
    Error()
