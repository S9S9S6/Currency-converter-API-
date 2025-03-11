import requests 
import tkinter as tk
from tkinter import ttk 

# API Setup
API_KEY = "f6f710f6f1d65c0ce24f3ba2"  
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest"

# Function to convert currency
def convert_currency():
    try:
        amount = float(amount_entry.get())  # Get amount from entry field
        from_currency = from_currency_var.get()  # Get selected "From" currency
        to_currency = to_currency_var.get()  # Get selected "To" currency

        url = BASE_URL + "/" + from_currency
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            exchange_rate = data["conversion_rates"].get(to_currency)

            if exchange_rate:
                converted_amount = amount * exchange_rate
                result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                result_label.config(text="Invalid currency code")
        else:
            result_label.config(text="Error: API request failed")
    except ValueError:
        result_label.config(text="Enter a valid number!")

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Amount Entry
tk.Label(root, text="Enter Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# Currency Selection (From)
tk.Label(root, text="From Currency:").pack()
from_currency_var = tk.StringVar()
from_currency_dropdown = ttk.Combobox(root, textvariable=from_currency_var)
from_currency_dropdown['values'] = ("USD", "EUR", "GBP", "INR", "JPY", "AUD")  # Add more if needed
from_currency_dropdown.pack()

# Currency Selection (To)
tk.Label(root, text="To Currency:").pack()
to_currency_var = tk.StringVar()
to_currency_dropdown = ttk.Combobox(root, textvariable=to_currency_var)
to_currency_dropdown['values'] = ("USD", "EUR", "GBP", "INR", "JPY", "AUD")  # Add more if needed
to_currency_dropdown.pack()

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Run GUI
root.mainloop()















