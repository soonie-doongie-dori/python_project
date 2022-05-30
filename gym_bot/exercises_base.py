import sqlite3 as sql


def exercises_insert():
    with sql.connect('db.db') as db:
        curs = db.cursor()

        chest = [
            'Жим гантелей на фитболе',
            'Жим гантелей на наклонной скамье',
            'Разводка на наклонной скамье',
            'Жим в хаммере',
            'Сведение рук в тренажере',
            'Подъёмы гантелей в стороны',

        ]

        for i in chest:
            curs.execute("""INSERT INTO exercises (muscle, name) 
                        values (?,?)""",
                         ['chest', i])
            db.commit()

        back = [
            'Тяга вниз широким хватом',
            'Румынская тяга',
            'Тяга гантели в наклоне',
            'Подтягивания в гравитроне',
            'Гиперэкстензия',
            'Гимнастический ролик',
        ]

        for i in back:
            curs.execute("""INSERT INTO exercises (muscle, name) 
                        values (?,?)""",
                         ['back', i])
            db.commit()

        legs = [
            'Жим ногами',
            'Тренировка ног в Гакк-машине',
            'Сведение ног в тренажере',
        ]

        for i in legs:
            curs.execute("""INSERT INTO exercises (muscle, name) 
                        values (?,?)""",
                         ['legs', i])
            db.commit()

        biceps = [
            'Подъем гантелей сидя'

        ]

        for i in biceps:
            curs.execute("""INSERT INTO exercises (muscle, name) 
                        values (?,?)""",
                         ['biceps', i])
            db.commit()

        triceps = [
            'Разгибания на трицепс',

        ]

        for i in triceps:
            curs.execute("""INSERT INTO exercises (muscle, name) 
                        values (?,?)""",
                         ['triceps', i])
            db.commit()

        stomach = [
            'Скручивания на фитболе',

        ]

        for i in stomach:
            curs.execute("""INSERT INTO exercises (muscle, name) 
                        values (?,?)""",
                         ['stomach', i])
            db.commit()

        shoulders = [
            'Жим гантелей от плеч',
            'Подъем гантелей в стороны',
            'Подъем гантелей вперед',
            'Подъем гантелей в наклоне',
        ]

        for i in shoulders:
            curs.execute("""INSERT INTO exercises (muscle, name) 
                        values (?,?)""",
                         ['shoulders', i])
            db.commit()

        warmup = [
            'Вращения плечами',
            'Вращения тазом',
            'Наклоны',
            'Махи ногами',
            'Выпады и перекаты'
        ]

        for i in warmup:
            curs.execute("""INSERT INTO exercises (muscle, name) 
                        values (?,?)""",
                         ['warmup', i])
            db.commit()
