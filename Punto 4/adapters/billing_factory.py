from domain.entities.billing import (
    InsuranceBilling,
    PrivateBilling,
    AgreementBilling
)

def billing_factory(billing_type):
    strategies = {
        "insurance": InsuranceBilling(),
        "private": PrivateBilling(),
        "agreement": AgreementBilling()
    }
    return strategies[billing_type]