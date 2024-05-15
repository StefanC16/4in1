import requests
import tkinter
from tkinter import messagebox


def convert_currency():
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()
    amount = float(amount_entry.get())

    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

    converted_amount = response.json()['rates'][to_currency]
    result_label.config(text=f"Conversia sumei de {amount} {
                        from_currency} = {converted_amount} {to_currency}")


window = tkinter.Tk()
window.title("Currency Converter")
window.geometry("850x600")
window.configure(bg='#333333')
frame = tkinter.Frame(bg='#333333')

# Creare de widget-uri
header_label = tkinter.Label(
    frame, text="Convertor valutar", bg='#333333', fg="#F5BF33", font=("Arial", 30))
from_currency_label = tkinter.Label(
    frame, text="Din moneda:", bg='#333333', fg="#F5BF33", font=("Arial", 16))
from_currency_entry = tkinter.Entry(frame, bg='#333333', font=("Arial", 16))

to_currency_entry = tkinter.Entry(frame, bg='#333333', font=("Arial", 16))
to_currency_label = tkinter.Label(
    frame, text="In moneda:", bg='#333333', fg="#F5BF33", font=("Arial", 16))

amount_entry = tkinter.Entry(frame, bg='#333333', font=("Arial", 16))
amount_label = tkinter.Label(
    frame, text="Valoare:", bg='#333333', fg="#F5BF33", font=("Arial", 16))

convert_button = tkinter.Button(frame, text="Converteaza", bg="#333333", fg="#F5BF33", font=(
    "Arial", 16), command=convert_currency)

result_label = tkinter.Label(
    frame, bg='#333333', fg="#F5BF33", font=("Arial", 16))

# Orientarea si plasarea widgets-urilor pe fereastra
header_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
from_currency_label.grid(row=1, column=0)
from_currency_entry.grid(row=1, column=1, pady=10)
to_currency_label.grid(row=2, column=0)
to_currency_entry.grid(row=2, column=1, pady=10)
amount_label.grid(row=3, column=0)
amount_entry.grid(row=3, column=1, pady=10)
convert_button.grid(row=4, column=1, columnspan=2, pady=20)
result_label.grid(row=5, column=0, pady=10)

frame.pack()

window.mainloop()
