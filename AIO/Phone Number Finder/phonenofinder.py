import requests
import tkinter
from tkinter import messagebox, filedialog
from tkinter import *
import phonenumbers
from phonenumbers import geocoder, carrier


def preprocess_phone_number(phone_number):
    # Replace '+' with '00' if present at the beginning of the phone number
    if phone_number.startswith('+'):
        return '00' + phone_number[1:]
    return phone_number


def phone_finder():
    # Retrieve the phone number from the entry widget
    phone_number = phone_number_entry.get()
    print("Raw phone number:", phone_number)
    # Preprocess the phone number to handle international format
    phone_number = preprocess_phone_number(phone_number)
    print("Processed phone number:", phone_number)
    try:
        # Parse the phone number with Romania as the default region
        parsed_number = phonenumbers.parse(phone_number, "RO")
        country_name = geocoder.description_for_number(parsed_number, 'en')
        service_provider = carrier.name_for_number(parsed_number, 'en')

        # Update the result label with the parsed phone number details
        result_label.config(text=f"Prefixul numarului de telefon {phone_number} este din {
                            country_name} si a fost inregistrat in reteaua {service_provider}")
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print("Error parsing phone number:", e)
        result_label.config(text="Numar de telefon invalid!")


window = tkinter.Tk()
window.title("PhoneFinder PK1.0")
window.geometry("1500x850")
window.configure(bg='#333333')
frame = tkinter.Frame(bg='#333333')

# Create widgets
header_label = tkinter.Label(
    frame, text="PhoneFinder", bg='#333333', fg="#F5BF33", font=("Arial", 30))
phone_number_label = tkinter.Label(
    frame, text="Introduceti numarul de telefon:", bg='#333333', fg="#F5BF33", font=("Arial", 16), width=25)
phone_number_entry = tkinter.Entry(
    frame, bg='#333333', font=("Arial", 16))

find_button = tkinter.Button(frame, text="Cauta!", bg="#333333", fg="#F5BF33", font=(
    "Arial", 16), command=phone_finder)

result_label = tkinter.Label(
    frame, bg='#333333', fg="#F5BF33", font=("Arial", 16))

# Orient and place widgets on the window
header_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
phone_number_label.grid(row=1, column=0)
phone_number_entry.grid(row=1, column=1, pady=10)
find_button.grid(row=4, column=1, columnspan=2, pady=20)
result_label.grid(row=5, column=0, columnspan=2, pady=10)


frame.pack()

window.mainloop()
