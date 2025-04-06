from connect import create_connection
import random
from faker import Faker



fake = Faker()

def table_is_empty(cursor, table_name):
    cursor.execute(f"SELECT COUNT(1) FROM {table_name};")
    return cursor.fetchone()[0] == 0

def insert_fake_data():
    with create_connection() as conn:
        cur = conn.cursor()

        if table_is_empty(cur, "groups"):
            group_names = ["Group A", "Group B", "Group C"]
            cur.executemany("INSERT INTO groups (name) VALUES (%s) ON CONFLICT DO NOTHING", [(name,) for name in group_names])

        if table_is_empty(cur, "teachers"):
            teachers = ["John Doe"] + [fake.name() for _ in range(3)]
            cur.executemany("INSERT INTO teachers (name) VALUES (%s) RETURNING id", [(name,) for name in teachers])

        cur.execute("SELECT id FROM teachers")
        teacher_ids = [row[0] for row in cur.fetchall()]

        if table_is_empty(cur, "subjects"):
            subjects = ["Math", "Physics", "Chemistry", "Biology", "History", "English", "IT"]
            cur.executemany(
                "INSERT INTO subjects (name, teacher_id) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                [(subj, random.choice(teacher_ids)) for subj in subjects]
            )

        cur.execute("SELECT id FROM groups")
        group_ids = [row[0] for row in cur.fetchall()]

        if table_is_empty(cur, "students"):
            students = [("Ihor", random.choice(group_ids))] + [(fake.name(), random.choice(group_ids)) for _ in range(39)]
            cur.executemany("INSERT INTO students (name, group_id) VALUES (%s, %s) RETURNING id", students)

        cur.execute("SELECT id FROM students")
        student_ids = [row[0] for row in cur.fetchall()]
        cur.execute("SELECT id FROM subjects")
        subject_ids = [row[0] for row in cur.fetchall()]

        if table_is_empty(cur, "grades"):
            grades = [
                (random.choice(student_ids), random.choice(subject_ids), random.randint(50, 100), fake.date_this_decade())
                for _ in range(800)
            ]
            cur.executemany("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s)", grades)

        print("Database successfully populated with fake data!")




if __name__ == "__main__":
    insert_fake_data()
