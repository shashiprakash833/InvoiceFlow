from automation.gst_calculator import calculate_bill
from automation.invoice_generator import generate_invoice

bill = calculate_bill(2, 250)

pdf = generate_invoice(
    "Rahul",
    bill["total"]
)

print("Invoice Generated:", pdf)