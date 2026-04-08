class HospitalConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = "Hospital Central"
            cls._instance.schedule = "9am - 5pm"
        return cls._instance