class Users:
    users = {}

    @classmethod
    def __init__(cls, data):
        cls.users.update({"name": data["name"]})
        cls.users.update({"twitter_id": data["twitter_username"]})
        cls.users.update({"unique_external_id": str(data["id"])})

    @classmethod
    def get_user_data(cls):
        return cls.users
