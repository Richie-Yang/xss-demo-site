import sqlite3


def connect_db():
    db = sqlite3.connect('xss_database.db')
    db.cursor().execute('CREATE TABLE IF NOT EXISTS comments '
                        '(id INTEGER PRIMARY KEY, '
                        'comment TEXT, datetime TEXT)')
    db.commit()
    return db


def add_comment(comment, datetime):
    db = connect_db()
    db.cursor().execute('INSERT INTO comments (comment, datetime) '
                        'VALUES (?,?)', (comment, datetime))
    db.commit()


def get_comments(search_query=None):
    db = connect_db()
    results = []
    get_all_query = 'SELECT comment, datetime FROM comments'
    for (comment, datetime) in db.cursor().execute(get_all_query).fetchall():
        if search_query is None or search_query in comment:
            results.append("%s <span style='font-size: 10px'>at %s</span>" % (comment, datetime))
    return results


def delete_comments():
    db = connect_db()
    db.cursor().execute('DELETE FROM comments')
    db.commit()

