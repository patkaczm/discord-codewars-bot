import sqlite3
import helpers.codewars_tasks as helpers

class Database:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        cur = self.conn.cursor()

        tables = cur.execute("SELECT name from sqlite_master WHERE type='table'").fetchall()
        tables = [t[0] for t in tables]

        # @todo test this
        self.__create_rounds_if_needed__(cur, tables)
        self.__create_cw_tasks_if_needed__(cur, tables)
        self.__create_tasks_if_needed__(cur, tables)
        self.__create_participants_if_needed__(cur, tables)

        if len(self.get_cw_tasks()) == 0:
            #@todo just a temp solution
            helpers._add_kyu_6(self.conn)


    def add_participant(self, username, round_id):
        self.conn.cursor().execute(
            f"""INSERT INTO PARTICIPANTS VALUES ('{username}', {round_id})""")
        self.conn.commit()
        return self.conn.cursor().lastrowid

    def get_participants(self, round_id):
        return self.conn.cursor().execute(
            f"""SELECT ROWID, * FROM PARTICIPANTS WHERE round_id = {round_id}"""
        ).fetchall()

    def get_participants(self):
        return self.conn.cursor().execute(
            f"""SELECT ROWID, * FROM PARTICIPANTS"""
        ).fetchall()

    def add_round(self, start_date: str, end_date: str):
        cur = self.conn.cursor()
        cur.execute(
            f"""INSERT INTO ROUNDS VALUES ('{start_date}', '{end_date}')""")
        self.conn.commit()
        return cur.lastrowid

    def get_rounds(self):
        return self.conn.cursor().execute("""SELECT ROWID, * FROM ROUNDS""").fetchall()

    def add_cw_task(self, kyu, cw_id, name):
        self.conn.cursor().execute(
            f"""INSERT INTO CW_TASKS VALUES ({kyu}, '{cw_id}', '{name}')"""
        )
        self.conn.commit()
        return self.conn.cursor().lastrowid

    def get_cw_tasks(self):
        return self.conn.cursor().execute(
            """SELECT ROWID, * FROM CW_TASKS"""
        ).fetchall()

    def add_task(self, round_id, task_id):
        self.conn.cursor().execute(
            f"""INSERT INTO TASKS VALUES ({round_id}, {task_id})"""
        )
        self.conn.commit()
        return self.conn.cursor().lastrowid

    def get_tasks(self):
        return self.conn.cursor().execute(
            f"""SELECT ROWID, * FROM TASKS """
        ).fetchall()

    @staticmethod
    def __create_rounds_if_needed__(cur, tables):
        if 'ROUNDS' not in tables:
            cur.execute("""CREATE TABLE ROUNDS (
                            start_date text NOT NULL,
                            end_date test NOT NULL
                        );""")

    @staticmethod
    def __create_cw_tasks_if_needed__(cur, tables):
        if 'CW_TASKS' not in tables:
            cur.execute("""CREATE TABLE CW_TASKS (
                            kyu INTEGER NOT NULL,
                            cw_id text NOT NULL UNIQUE,
                            name text NOT NULL
                        );""")

    @staticmethod
    def __create_tasks_if_needed__(cur, tables):
        if 'TASKS' not in tables:
            cur.execute("""CREATE TABLE TASKS (
                            round_id INTEGER not null,
                            task_id INTEGER not null,
                            FOREIGN KEY (round_id) REFERENCES ROUNDS (ROWID) ON DELETE CASCADE,
                            FOREIGN KEY (task_id) REFERENCES CW_TASKS (ROWID) ON DELETE CASCADE 
                        );""")

    @staticmethod
    def __create_participants_if_needed__(cur, tables):
        if 'PARTICIPANTS' not in tables:
            cur.execute("""CREATE TABLE PARTICIPANTS (
                            username text NOT NULL,
                            round_id INTEGER NOT NULL,
                            FOREIGN KEY (round_id) REFERENCES ROUNDS (ROWID) ON DELETE CASCADE 
                        );""")
