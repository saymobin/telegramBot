import psycopg

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="telegram_project",
    user="postgres",
    password="1234"
) as conn:
    with conn.cursor() as cur:
        cur.execute('''SELECT id, telegram_id, username, first_name, is_active
                       FROM users
                       ORDER BY id;''')
        result = cur.fetchall()
        print(result)