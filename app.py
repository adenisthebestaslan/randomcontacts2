import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import random



def submit():
    name = name_entry.get()
    areacode = areacode_entry.get()
    password3 = password_entry3.get()
        # Open the text file in read mode
    with open('user_data.txt', 'r') as file:
        # Read all lines from the file and store them in a list
        lines = file.readlines()

    # Select a random piece of information
    random_info = random.choice(lines)


    if not name or not areacode:
        messagebox.showwarning("Warning", "Please fill in all fields")
    else:
        # You can perform further actions here, like saving to a database or displaying the information
        formatted_data = f"\nName: {name}, phonenumber: {areacode},  bio: {password3}"

        with open("user_data.txt", "a") as file:
            file.write(formatted_data)
        messagebox.showinfo("Submission Successful", f"Your Random friend is: {random.choice(lines)}")
        name_entry.delete(0, tk.END)
        areacode_entry.delete(0, tk.END)
        password_entry3.delete(0, tk.END)
# Create the main window
app = tk.Tk()
# app.overrideredirect(True)

app.configure(background='purple')


custom_logo = tk.PhotoImage(file=r"C:\Users\adena\Downloads\questionmark.gif")

app.title("signup page")
app.geometry("400x300")


# Image 
image = PhotoImage(file=r"C:\Users\adena\Downloads\questionmark.gif")  
image_label = tk.Label(app, image=image, bg='pink')
image_label.grid(row=0, column=0, columnspan=1, padx=2, pady=0,)

# Name
name_label = tk.Label(app, text="Name:", bg='pink')
name_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E )
name_entry = tk.Entry(app,width=30)
name_entry.grid(row=1, column=1, padx=20, pady=5)

# areacode
areacode_label = tk.Label(app, text="phonenumber:", bg='pink')
areacode_label.grid(row=2, column=0, padx=10, pady=5,sticky=tk.E)
areacode_entry = tk.Entry(app,width=30)
areacode_entry.grid(row=2, column=1, padx=10, pady=5)

#bio

password3 = tk.Label(app, text="bio:",bg='pink')
password3.grid(row=3, column=0, padx=10, pady=5,)
password_entry3 = tk.Entry(app,width=30)
password_entry3.grid(row=3, column=1, padx=10, pady=5)


# Submit button
submit_button = tk.Button(app, text="find ",width=10,height=2 ,bg='pink', command=submit)
submit_button.grid(row=7, column=0, columnspan=2, pady=15)








# Print or use the randomly selected information
app.title("info giving")
submit_button = tk.Button(app, text=f"Random Information:",width=15,height=2 ,command=submit)
# print("Random Information: ", random_info.strip())

app.mainloop()

