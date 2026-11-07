import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="telegram_project",
    user="postgres",
    password="1234"
)

try:
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE users SET username = %s WHERE telegram_id = %s",
            ("mobin_rollback",12345)
        )

    conn.rollback()
            
except psycopg.Error as e:
    conn.rollback()
    print(f"Database error: {e}")

finally:
    conn.close()