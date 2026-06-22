from fastapi import FastAPI
from pydantic import BaseModel

from automation.email_sender import send_email
from automation.gst_calculator import calculate_bill
from automation.invoice_generator import generate_invoice

app = FastAPI(title="InvoiceFlow")


class Order(BaseModel):
    customer_name: str
    email: str
    item: str
    qty: int
    price: float


@app.get("/")
def home():
    return {
        "project": "InvoiceFlow",
        "status": "running"
    }


@app.post("/new-order")
def new_order(order: Order):

    # Calculate bill
    bill = calculate_bill(
        order.qty,
        order.price
    )

    # Generate PDF invoice
    pdf = generate_invoice(
        order.customer_name,
        order.item,
        order.qty,
        order.price,
        bill
    )

    # Send email
    try:
        send_email(order.email, pdf)
        print(f"Email sent to {order.email}")
    except Exception as e:
        print("Email Error:", e)

    return {
        "status": "success",
        "customer": order.customer_name,
        "invoice": pdf,
        "total": bill["total"]
    }