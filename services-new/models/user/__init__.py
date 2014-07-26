from config import *

user_table = 'users'

def get(user_id=None, user_login=None):
    user = None
    if user_id is None:
        user = db.where(user_table, user_login=user_login)
    else:
        user = db.where(user_table, id=user_id)
    return None if len(user) == 0 else user[0]
    
def save(user, user_id=None):
    user.nick_name = None if user.nick_name is None or len(user.nick_name) == 0 else user.nick_name
    if user_id is None:
        user_id = db.insert(user_table,
                user_login=user.user_login,
                id_url=user.id_url,
                first_name=user.first_name,
                last_name=user.last_name,
                nick_name=user.nick_name
            )
        return user_id
    else:
        db.update(user_table,
                where='id=%s' % user.id,
                id_url=user.id_url,
                first_name=user.first_name,
                last_name=user.last_name,
                nick_name=user.nick_name
            )
        return get(user.id)