import sqlite3

class DBase:
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()

    def user_check(self, user_id):
        with self.con:
            res = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(res))
        
    def add_user(self, user_id):
        with self.con:
            return self.con.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

    def add_reg_user(self, active, user_id):
        with self.con:
            return self.con.execute("UPDATE users SET active = ? WHERE user_id = ?", (active ,user_id,))

    def user_check_reg(self, user_id):
        with self.con:
            try:
                user = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
                if int(user[2] != 0):
                    return True
                else:
                  return False
            except:
                return False

    def user_check_phone(self, user_phone):
        with self.con:
            res = self.cursor.execute("SELECT * FROM users WHERE number = ?", (user_phone,)).fetchall()
            return bool(len(res))

       #ban panel     
    # def user_ban(self, user_id):
    #     with self.con:
    #         return self.con.execute("UPDATE users SET ban = ?  WHERE user_id = ?", (1, user_id,))
        
    # def user_check_ban(self, user_id):
    #     with self.con:
    #          user = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    #          if int(user[4] != 0):
    #             return True
    #          else:
    #             return False