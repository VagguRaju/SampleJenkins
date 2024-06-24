import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'demo'
username = 'postgres'
passwd = '0000'
port_id = 5432

conn = None

try:
   with psycopg2.connect(
        dbname=database,
        user=username,
        password=passwd,
        host=hostname,
        port=port_id
    ) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            create_script = '''
            CREATE TABLE IF NOT EXISTS employee (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            salary INT,
            dept_id INT
        )
        '''
            cur.execute('DROP TABLE IF EXISTS employee')
            cur.execute(create_script)

            insert_script = 'INSERT INTO employee (name, salary, dept_id) VALUES (%s, %s, %s)'
            insert_values = [
            ('Raj', 20000, 101),
            ('Somesh', 10000, 102),
            ('Ram', 20000, 103),
            ('Sukesh', 30000, 104)
                            ]

            '''for record in insert_values:
                cur.execute(insert_script, record)'''
            cur.executemany(insert_script,insert_values)

            # conn.commit()

            cur.execute('SELECT * FROM employee')
            for record in cur.fetchall():
                print(record['id'], record['name'], record['salary'], record['dept_id'])

except psycopg2.Error as e:
    print("Error during database operation:", e)

finally:
    if conn is not None:
        conn.close()
