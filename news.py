#! /usr/bin/env python3
import psycopg2

DBNAME = "news"


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
       count(*) AS num
FROM authors
JOIN articles
ON authors.id = articles.author
JOIN log
ON log.path like concat('/article/%', articles.slug)
GROUP BY authors.name
ORDER BY num DESC;
"""

query_3 = """
select * from (
    select a.day,
    round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)
    as errp from
    (select date(time) as day, count(*) as hits from log group by day) as a
    inner join
    (select date(time) as day, count(*) as hits from log where status
    like '%404%' group by day) as b
    on a.day = b.day)
    as t where errp > 1.0;
"""


def connect(database_name="news"):
    try:
        db = psycopg2.connect(dbname=DBNAME)
        cursor = db.cursor()
        return db, cursor()
    except:
        print("<error message>")


def get_query_results(query):
    db = psycopg2.connect(dbname=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results


def article(queries):
    db = psycopg2.connect(dbname=DBNAME)
    cursor = db.cursor()
    cursor.execute(query_1)
    results = cursor.fetchall()
    for res in results:
        print('{title} - {count} views'.format(title=res[0], count=res[1]))


def author():
    results = get_query_results(query_2)
    for row in results:
        print row[0], "-", row[1], "views"


def error():
    results = get_query_results(query_3)
    for row in results:
        print row[0], "-", row[1], "%"


if __name__ == '__main__':
    print("\nPopular 3 articles\n")
    article(query_1)
    print("\npopular 4 authors\n")
    author()
    print("\n Days in which more than 1 %")
    error()
