import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    areacode = areacode_entry.get()
    rest = rest_entry.get()
    password = password_entry.get()
    password1 = password_entry1.get()

    if not name or not areacode or not rest or not password:
        messagebox.showwarning("Warning", "Please fill in all fields")
    elif  password != password1:
          messagebox.showwarning("wrong", "password and reinput of it are not same")
    else:
        # You can perform further actions here, like saving to a database or displaying the information
        formatted_data = f"     \n Name: {name}, areacode: {areacode}, rest of phone: {rest}, Password: {password}\n,"

        with open("user_data.txt", "a") as file:
            file.write(formatted_data)
        messagebox.showinfo("Submission Successful", f"Name: {name}\n areacode: {areacode}\n restofphone: {rest}/n")
        name_entry.delete(0, tk.END)
        areacode_entry.delete(0, tk.END)
        rest_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        password_entry1.delete(0, tk.END)
# Create the main window
app = tk.Tk()
app.title("Collection Informations from clients")
app.geometry("400x300")

# Name
name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
name_entry = tk.Entry(app,width=30)
name_entry.grid(row=0, column=1, padx=20, pady=5)

# areacode
areacode_label = tk.Label(app, text="areacode:")
areacode_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
areacode_entry = tk.Entry(app)
areacode_entry.grid(row=1, column=1, padx=10, pady=5)

# rest
rest_label = tk.Label(app, text="rest:")
rest_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
rest_entry = tk.Entry(app)
rest_entry.grid(row=2, column=1, padx=10, pady=5)

# Password
password_label = tk.Label(app, text="Password:")
password_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.N)
password_entry = tk.Entry(app, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)

# password confirmation
# Password
password_label1 = tk.Label(app, text="Pass:")
password_label1.grid(row=4, column=0, padx=10, pady=5)
password_entry1 = tk.Entry(app)
password_entry1.grid(row=4, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(app, text="find me a freind!",width=15,height=2 ,command=submit)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)


# Run the application
app.mainloop()





