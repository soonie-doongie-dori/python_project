import sqlite3 as sql


def gyms_insert():
    gyms_list = [
        ['SkyGym', 'На площади Собина'],
        ['X-Fit', 'На Московском шоссе'],
        ['KingGym', 'На Дмитровском шоссе']
    ]
    with sql.connect('db.db') as db:
        curs = db.cursor()

        request = """insert into gyms (name, address)
                    values (?,?);"""
        curs.executemany(request,
                         gyms_list)
        db.commit()
