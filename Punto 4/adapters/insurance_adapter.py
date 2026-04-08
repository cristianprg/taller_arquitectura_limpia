class InsuranceAdapter:
    def __init__(self, external_api):
        self.external_api = external_api

    def process_claim(self, patient, cost):
        self.external_api.send_data(patient.name, cost)