import tkinter as tk
from tkinter import messagebox
import json

# File to store contact data
CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    
    if name:
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
        
        # Clear the entry fields
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Name cannot be empty.")

def view_contacts():
    contact_list = ""
    if contacts:
        for name, details in contacts.items():
            contact_list += f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n\n"
    else:
        contact_list = "No contacts available."
    messagebox.showinfo("Contact List", contact_list)

def search_contact():
    search_term = search_entry.get().strip()
    
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            # Populate the entry fields with the found contact details
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
            
            name_entry.insert(0, name)
            phone_entry.insert(0, details['phone'])
            email_entry.insert(0, details['email'])
            address_entry.insert(0, details['address'])
            
            messagebox.showinfo("Search Result", f"Contact '{name}' found and details populated.")
            found = True
            break
    
    if not found:
        messagebox.showwarning("Search Result", "No matching contact found.")

def update_contact():
    name = name_entry.get().strip()
    
    if name in contacts:
        phone = phone_entry.get().strip()
        email = email_entry.get().strip()
        address = address_entry.get().strip()
        
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact '{name}' updated successfully.")
        
        # Clear the entry fields
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Update Error", "Please search for a contact first.")

def delete_contact():
    name = name_entry.get().strip()
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
        
        # Clear the entry fields
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Delete Error", "Please search for a contact first.")

def exit_application():
    save_contacts(contacts)
    root.destroy()

contacts = load_contacts()

# Setting up the main window
root = tk.Tk()
root.title("Contact Book")
root.configure(bg="#f0f0f0")  # Set background color of the window

# Create a mobile-like frame with contrasting background color
frame = tk.Frame(root, padx=10, pady=10, width=300, bg="#ffffff", bd=2, relief=tk.SOLID)
frame.pack(padx=10, pady=10)

# Name Entry
tk.Label(frame, text="Name:", font=('Arial', 12), bg="#ffffff").grid(row=0, column=0, sticky=tk.W)
name_entry = tk.Entry(frame, font=('Arial', 12), bg="#f0f0f0")  # Light gray background
name_entry.grid(row=0, column=1, pady=5)

# Phone Entry
tk.Label(frame, text="Phone:", font=('Arial', 12), bg="#ffffff").grid(row=1, column=0, sticky=tk.W)
phone_entry = tk.Entry(frame, font=('Arial', 12), bg="#f0f0f0")  # Light gray background
phone_entry.grid(row=1, column=1, pady=5)

# Email Entry
tk.Label(frame, text="Email:", font=('Arial', 12), bg="#ffffff").grid(row=2, column=0, sticky=tk.W)
email_entry = tk.Entry(frame, font=('Arial', 12), bg="#f0f0f0")  # Light gray background
email_entry.grid(row=2, column=1, pady=5)

# Address Entry
tk.Label(frame, text="Address:", font=('Arial', 12), bg="#ffffff").grid(row=3, column=0, sticky=tk.W)
address_entry = tk.Entry(frame, font=('Arial', 12), bg="#f0f0f0")  # Light gray background
address_entry.grid(row=3, column=1, pady=5)

# Add Contact and View Contacts Buttons
tk.Button(frame, text="Add Contact", command=add_contact, font=('Arial', 12), width=13, bg="#4CAF50", fg="white").grid(row=4, column=0, padx=5, pady=5)
tk.Button(frame, text="View Contacts", command=view_contacts, font=('Arial', 12), width=13, bg="#2196F3", fg="white").grid(row=4, column=1, padx=5, pady=5)

# Search Frame
search_frame = tk.Frame(frame, bg="#ffffff")
search_frame.grid(row=5, column=0, columnspan=2, pady=5)

tk.Label(search_frame, text="Search:", font=('Arial', 12), bg="#ffffff").grid(row=0, column=0, sticky=tk.W)
search_entry = tk.Entry(search_frame, font=('Arial', 12), bg="#f0f0f0")  # Light gray background
search_entry.grid(row=0, column=1, padx=5)
tk.Button(search_frame, text="Search Contact", command=search_contact, font=('Arial', 12), width=13, bg="#FFC107", fg="black").grid(row=0, column=2, padx=5)

# Update and Delete Buttons
tk.Button(frame, text="Update Contact", command=update_contact, font=('Arial', 12), width=13, bg="#FF9800", fg="white").grid(row=6, column=0, padx=5, pady=5)
tk.Button(frame, text="Delete Contact", command=delete_contact, font=('Arial', 12), width=13, bg="#F44336", fg="white").grid(row=6, column=1, padx=5, pady=5)

# Exit Button
tk.Button(frame, text="Exit", command=exit_application, font=('Arial', 12), width=28, bg="#9E9E9E", fg="white").grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
