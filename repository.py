from database import get_connection


def create_task(title):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO tasks (title)
        VALUES (%s)
        RETURNING id, title, done;
        """,
        (title,)
    )

    row = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }

def get_all_tasks():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
        SELECT id, title, done
        FROM tasks
        ORDER BY id;
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "id": row[0],
            "title": row[1],
            "done": row[2]
        }
        for row in rows
    ]
def get_task_by_id(task_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, title, done
        FROM tasks
        WHERE id = %s;
        """,
        (task_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }
def update_task(task_id, title, done):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE tasks
        SET title = %s,
            done = %s
        WHERE id = %s
        RETURNING id, title, done;
        """,
        (title, done, task_id)
    )

    row = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }
def delete_task(task_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM tasks
        WHERE id = %s
        RETURNING id;
        """,
        (task_id,)
    )

    row = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    return row is not None