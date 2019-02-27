#! /usr/bin/env python3
import psycopg2

DBNAME = "news"


def article():
    db = psycopg2.connect(database=DBNAME)
    v = db.cursor()
    v.execute(query_1)
    results = v.fetchall()
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        print("%s--%d" % (title, views))
    db.close()


def authors():
    db = psycopg2.connect(database=DBNAME)
    v = db.cursor()
    v.execute(query_2)
    results = v.fetchall()
    for i in range(len(results)):
        name = results[i][0]
        views = results[i][1]
        print("%s--%d" % (name, views))
    db.close()


def errperc():
    db = psycopg2.connect(database=DBNAME)
    v = db.cursor()
    v.execute(query_3)
    results = v.fetchall()
    for i in range(len(results)):
        date = results[i][0]
        err_prc = results[i][1]
        print("%s -- %.1f %%" % (date, err_prc))

query_1 = """
SELECT articles.title,
       count(*)
FROM log,
     articles
WHERE log.path = '/article/' || articles.slug
GROUP BY articles.title
ORDER BY count(*) DESC
LIMIT 3;
"""

query_2 = """
SELECT authors.name,
       count(*)
FROM log,
     articles,
     authors
WHERE log.path = '/article/' || articles.slug
GROUP BY authors.name
ORDER BY count(*) DESC;
"""

query_3 = """SELECT day, perc FROM (
           SELECT day, round((sum(requests)/(SELECT count(*) FROM log WHERE 
           substring(cast(log.time as text), 0, 11) = day) * 100), 2) as 
           perc FROM (select substring(cast(log.time as text), 0, 11) as 
           day, count(*) as requests FROM log 
           WHERE status like '%404%' GROUP by day) 
           as log_percentage GROUP by day ORDER by perc desc) as final_query 
           WHERE perc >= 1"""

if __name__ == '__main__':
    print("\nPopular 3 articles\n")
    article()
    print("\npopular 4 authors\n")
    authors()
    print("\n Days in which more than 1 %")
    errperc()
