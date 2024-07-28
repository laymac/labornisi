class BillingInfo:
    def __init__(self, customer_id, billing_address, billing_phone, billing_email):
        self.customer_id = customer_id
        self.billing_address = billing_address
        self.billing_phone = billing_phone
        self.billing_email = billing_email

# Example usage
billing_info = BillingInfo(
    customer_id=12345,
    billing_address="123 Main St, Anytown, USA",
    billing_phone="+1-800-555-1234",
    billing_email="customer@example.com"
)
