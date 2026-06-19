def calculate_bill(qty, price):
    subtotal = qty * price

    cgst = subtotal * 0.025
    sgst = subtotal * 0.025

    total = subtotal + cgst + sgst

    return {
        "subtotal": subtotal,
        "cgst": cgst,
        "sgst": sgst,
        "total": total
    }