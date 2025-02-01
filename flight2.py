import sqlite3
import tkinter as tk
from tkinter import ttk,messagebox
 
conn = sqlite3.connect('user_data.db')
 
c=conn.cursor()
 
c.execute('''CREATE TABLE IF NOT EXISTS users(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          email TEXT,
          phone TEXT,
          password TEXT)''')
 
conn.commit()
 
def add_user():
    email=email_entry.get()
    phone = Phone_entry.get()
    password=password_entry.get()
 
    if email and phone and password:
        c.execute("INSERT INTO users(email, phone, password) VALUES(?,?,?)",(email, phone, password))
        conn.commit()
        messagebox.showinfo("Success","User added successfully!")
        view_user()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")
        clear_enteries()
 
def view_user():
    for row in tree.get_children():
        tree.delete(row)
 
    c.execute("SELECT * FROM users")
 
    rows=c.fetchall()
 
    for row in rows:
        tree.insert("",tk.END,values=row)
 
def edit_user():
    user_id=user_id_entry.get()
    email=email_entry.get()
    phone = Phone_entry.get()
    password=password_entry.get()
 
    if user_id and email and phone and password:
        c.execute("UPADTE users SET email=?, phone=?, password=? WHERE id =?",(email,phone, password,user_id))
        conn.commit()
        messagebox.showinfo("Success","User updated successfully!")
        view_user()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")
        clear_enteries()
 
def delete_user():
    user_id=user_id_entry.get()
    if user_id:
        c.execute("DELETE FROM users WHERE id = ?",(user_id))
        conn.commit()
        messagebox.showinfo("Success","User deleted successfully!")
        view_user()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")
        clear_enteries()
 
def clear_enteries():
    user_id_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    Phone_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
 
 
root = tk.Tk()
root.title("User Registration Form")
root.geometry("400x500")
root.configure(bg='#ffcc66')
 
frame=tk.Frame(root,bg="white",padx=20,pady=20)
frame.pack(pady=10)
 
tk.Label(frame, text="User ID (for edit/delete)",font=("Arial",10,"bold"),bg="white").grid(row=0,column=0,sticky="w")
user_id_entry=tk.Entry(frame,width=30,relief="sunken")
user_id_entry.grid(row=1,column=0,columnspan=2,pady=5)
 
 
tk.Label(frame, text="Email",font=("Arial",10,"bold"),bg="white").grid(row=2,column=0,sticky="w")
email_entry=tk.Entry(frame,width=30,relief="sunken")
email_entry.grid(row=3,column=0,columnspan=2,pady=5)
 
 
tk.Label(frame, text="Phone",font=("Arial",10,"bold"),bg="white").grid(row=4,column=0,sticky="w") #w- left, e - right, s - bottom, n- top
Phone_entry=tk.Entry(frame,width=30,relief="sunken")
Phone_entry.grid(row=5,column=0,columnspan=2,pady=5)
 
 
tk.Label(frame, text="Password",font=("Arial",10,"bold"),bg="white").grid(row=6,column=0,sticky="w")
password_entry=tk.Entry(frame,width=30,relief="sunken")
password_entry.grid(row=7,column=0,columnspan=2,pady=5)
 
tk.Button(frame, text="Add",bg="green",fg="white",font=("Arial",12,"bold"),command=add_user).grid(row=8,column=0,pady=10)
tk.Button(frame, text="View",bg="blue",fg="black",font=("Arial",12,"bold"),command=view_user).grid(row=8,column=1,pady=10)
tk.Button(frame, text="Edit",bg="orange",fg="white",font=("Arial",12,"bold"),command=edit_user).grid(row=9,column=0,pady=10)
tk.Button(frame, text="Delete",bg="red",fg="white",font=("Arial",12,"bold"),command=delete_user).grid(row=9,column=1,pady=10)
 
 
columns=('ID','Email','Phone','Password')
tree=ttk.Treeview(root,columns=columns,show='headings')
tree.heading('Email',text='Email')
tree.heading('Phone',text='Phone')
tree.heading('Password',text='Password')
 
tree.pack(pady=20)
 
 
view_user()
 
root.mainloop()
 
conn.close()
 
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
 
# Functions for CRUD operations
def add_flight_data():
    from_city = from_entry.get()
    to_city = to_entry.get()
    departure = departure_entry.get()
    return_date = return_entry.get()
    cabin = cabin_class.get()
    adults = adults_spinbox.get()
   
    if not (from_city and to_city and departure):
        messagebox.showerror("Input Error", "Please fill in all required fields (From, To, Departure).")
        return
 
    # Insert the data into the Treeview
    tree.insert("", "end", values=(from_city, to_city, departure, return_date, cabin, adults))
    clear_fields()
 
 
def delete_flight_data():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select an item to delete.")
        return
    tree.delete(selected_item)
 
 
def update_flight_data():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select an item to update.")
        return
   
    from_city = from_entry.get()
    to_city = to_entry.get()
    departure = departure_entry.get()
    return_date = return_entry.get()
    cabin = cabin_class.get()
    adults = adults_spinbox.get()
 
    tree.item(selected_item, values=(from_city, to_city, departure, return_date, cabin, adults))
    clear_fields()
 
 
def view_selected_data():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select an item to view.")
        return
   
    item_values = tree.item(selected_item)['values']
    from_entry.delete(0, tk.END)
    to_entry.delete(0, tk.END)
    departure_entry.delete(0, tk.END)
    return_entry.delete(0, tk.END)
 
    from_entry.insert(0, item_values[0])
    to_entry.insert(0, item_values[1])
    departure_entry.insert(0, item_values[2])
    return_entry.insert(0, item_values[3])
    cabin_class.set(item_values[4])
    adults_spinbox.set(item_values[5])
 
 
def clear_fields():
    from_entry.delete(0, tk.END)
    to_entry.delete(0, tk.END)
    departure_entry.delete(0, tk.END)
    return_entry.delete(0, tk.END)
    cabin_class.current(0)
    adults_spinbox.set(1)
 
 
def update_background(event=None):
    new_width = root.winfo_width()
    new_height = root.winfo_height()
   
    resized_image = background_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_image_resized = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=bg_image_resized, anchor="nw")
    canvas.bg_image_resized = bg_image_resized  # Keep reference to avoid garbage collection
 
 
# Main Window
root = tk.Tk()
root.title("Flight Booking System")
root.geometry("1200x800")
 
# Load Background Image from URL
url = "https://www.w3schools.com/w3images/mountains.jpg"
response = requests.get(url)
background_image = Image.open(BytesIO(response.content))
 
# Canvas for Background
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)
 
# Bind resizing to update background
root.bind("<Configure>", update_background)
 
# Frame for Inputs
frame = tk.Frame(root, bg="#2a77d2", padx=20, pady=20)
frame.place(relx=0.5, rely=0.3, anchor="center", relwidth=0.5)
 
flight_type_label = tk.Label(frame, text="Flight Type:", bg="#2a77d2", fg="white")
flight_type_label.grid(row=0, column=0, pady=10)
 
flight_type = ttk.Combobox(frame, values=["Round Trip", "One Way", "Multi-City"])
flight_type.grid(row=0, column=1)
flight_type.current(0)
 
from_label = tk.Label(frame, text="From:", bg="#2a77d2", fg="white")
from_label.grid(row=1, column=0, pady=10)
 
from_entry = ttk.Entry(frame)
from_entry.grid(row=1, column=1)
 
to_label = tk.Label(frame, text="To:", bg="#2a77d2", fg="white")
to_label.grid(row=2, column=0, pady=10)
 
to_entry = ttk.Entry(frame)
to_entry.grid(row=2, column=1)
 
departure_label = tk.Label(frame, text="Departure:", bg="#2a77d2", fg="white")
departure_label.grid(row=3, column=0, pady=10)
 
departure_entry = ttk.Entry(frame)
departure_entry.grid(row=3, column=1)
 
return_label = tk.Label(frame, text="Return:", bg="#2a77d2", fg="white")
return_label.grid(row=4, column=0, pady=10)
 
return_entry = ttk.Entry(frame)
return_entry.grid(row=4, column=1)
 
# Buttons for CRUD operations
button_frame = tk.Frame(root)
button_frame.place(relx=0.5, rely=0.5, anchor="center")
 
add_button = tk.Button(button_frame, text="Add", command=add_flight_data)
add_button.grid(row=0, column=0, padx=10)
 
update_button = tk.Button(button_frame, text="Update", command=update_flight_data)
update_button.grid(row=0, column=1, padx=10)
 
delete_button = tk.Button(button_frame, text="Delete", command=delete_flight_data)
delete_button.grid(row=0, column=2, padx=10)
 
view_button = tk.Button(button_frame, text="View", command=view_selected_data)
view_button.grid(row=0, column=3, padx=10)
 
# Treeview for Data Display
tree = ttk.Treeview(root, columns=("From", "To", "Departure", "Return", "Cabin Class", "Adults"), show="headings")
tree.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.9)
 
for col in ("From", "To", "Departure", "Return", "Cabin Class", "Adults"):
    tree.heading(col, text=col)
    tree.column(col, width=150)
 
root.mainloop()
 