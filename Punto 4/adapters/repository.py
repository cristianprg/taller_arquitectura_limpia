class PatientRepository:
    def __init__(self):
        self.patients = {}
        
    def add(self, patient):
        self.patients[patient.name] = patient
    
    def get(self, name):
        return self.patients.get(name)