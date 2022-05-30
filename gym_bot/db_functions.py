import sqlite3 as sql


def get_gyms_list():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""Select * 
                    from gyms""")

        return curs.fetchall()


def get_exercises_list():
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""select muscle, name
                        from exercises
                        """)
        return curs.fetchall()


def add_exercise(exercise_data: list):
    # Вставляем данные в таблицу
    with sql.connect('db.db') as db:
        curs = db.cursor()
        curs.execute("""INSERT INTO trainings (date, gym_name, exercise_id, minutes, reps)
                          VALUES (?, ?, ?, ?, ?)
                        """,
                     exercise_data)
        db.commit()
