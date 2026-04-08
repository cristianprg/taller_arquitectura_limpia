from adapters.repository import PatientRepository
from adapters.notifier import NotificationService, EmailNotifier, SMSNotifier
from adapters.insurance_adapter import InsuranceAdapter
from adapters.billing_factory import billing_factory

from frameworks.external_api import ExternalInsuranceAPI

from use_cases.hospital_use_cases import HospitalService


repo = PatientRepository()

notifier = NotificationService()
notifier.subscribe(EmailNotifier())
notifier.subscribe(SMSNotifier())

insurance_adapter = InsuranceAdapter(ExternalInsuranceAPI())

hospital = HospitalService(
    repo=repo,
    notifier=notifier,
    billing_factory=billing_factory,
    insurance_service=insurance_adapter
)

print(hospital.register_patient("Juan"))
print(hospital.register_patient("Maria"))
print(hospital.register_patient("Carlos"))

hospital.update_clinical_record("Juan", "Receta: Paracetamol 400mg")

print(hospital.bill_patient("Juan", 1000, "private"))
print(hospital.bill_patient("Maria", 2000, "insurance"))
print(hospital.bill_patient("Carlos", 1500, "agreement"))