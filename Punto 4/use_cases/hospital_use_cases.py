from domain.entities.factory import PersonFactory

class HospitalService:
    def __init__(self, repo, notifier, billing_factory, insurance_service):
        self.repo = repo
        self.notifier = notifier
        self.billing_factory = billing_factory
        self.insurance_service = insurance_service

    def register_patient(self, name):
        patient = PersonFactory.create_person("patient", name)
        self.repo.add(patient)
        return f"Paciente registrado: {name}"

    def update_clinical_record(self, name, record):
        patient = self.repo.get(name)
        if patient:
            message = f"Registro clínico actualizado para {name}: {record}"
            self.notifier.notify(message)

    def bill_patient(self, name, amount, billing_type):
        strategy = self.billing_factory(billing_type)
        cost = strategy.calculate(amount)

        patient = self.repo.get(name)

        result = f"Costo final para {name}: {cost}"

        if billing_type == "insurance":
            self.insurance_service.process_claim(patient, cost)

        return result