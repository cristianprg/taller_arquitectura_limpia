from domain.entities.person import Patient, Doctor, Admin

class PersonFactory:
    @staticmethod
    def create_person(role, name):
        if role == "patient":
            return Patient(name)
        elif role == "doctor":
            return Doctor(name)
        elif role == "admin":
            return Admin(name)
        else:
            raise ValueError("Invalid role specified")