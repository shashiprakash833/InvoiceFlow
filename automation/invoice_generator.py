from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
import os

def generate_invoice(customer_name, item, qty, price, bill):

    os.makedirs("invoices", exist_ok=True)

    invoice_no = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    filename = f"invoices/{invoice_no}.pdf"

    c = canvas.Canvas(filename)

    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, 800, "INVOICE")

    # Restaurant Details
    c.setFont("Helvetica", 12)
    c.drawString(50, 760, "Restaurant Name: Demo Restaurant")
    c.drawString(50, 740, "GSTIN: 36ABCDE1234F1Z5")

    # Invoice Info
    c.drawString(400, 760, f"Invoice No: {invoice_no}")
    c.drawString(400, 740, f"Date: {datetime.now().strftime('%d-%m-%Y')}")

    # Customer
    c.drawString(50, 700, f"Customer: {customer_name}")

    # Table Header
    c.line(50, 670, 550, 670)

    c.drawString(50, 650, "Item")
    c.drawString(250, 650, "Qty")
    c.drawString(350, 650, "Price")
    c.drawString(450, 650, "Amount")

    c.line(50, 640, 550, 640)

    amount = qty * price

    c.drawString(50, 620, item)
    c.drawString(250, 620, str(qty))
    c.drawString(350, 620, str(price))
    c.drawString(450, 620, str(amount))

    # Totals
    c.drawString(350, 550, f"Subtotal: ₹{bill['subtotal']:.2f}")
    c.drawString(350, 530, f"CGST: ₹{bill['cgst']:.2f}")
    c.drawString(350, 510, f"SGST: ₹{bill['sgst']:.2f}")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(350, 480, f"Grand Total: ₹{bill['total']:.2f}")

    c.drawString(350, 430, "Authorized Signature")

    c.save()

    return filename