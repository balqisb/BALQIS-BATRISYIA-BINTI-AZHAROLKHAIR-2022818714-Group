import tkinter as tk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sport_centre"
)

cursor = mydb.cursor()

class MainMenu(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main Menu")
        self.geometry('400x300')
        self.configure(bg='#660000')

        label = tk.Label(self, text='SPORT CENTRE', font=("Montserrat Medium", 28, "bold"), bg='#660000', fg='tan')
        label.pack(ipadx=10, ipady=10)

        #Buttons
        buttons = [
            ("Registration", self.show_registration),
            ("Facility Rental", self.show_facility_rental),
            ("Damage Reporting", self.show_damage_reporting)
        ]

        for text, command in buttons:
            button = tk.Button(self, text=text, command=command, bg='#660000', fg='tan', font=("Georgia", 10))
            button.pack(pady=10, ipadx=10, ipady=5)

    def show_registration(self):
        RegistrationWindow(self)

    def show_damage_reporting(self):
        DamageReportingWindow(self)

    def show_facility_rental(self):
        FacilityRentalWindow(self)

class RegistrationWindow(tk.Toplevel):
    def __init__(self, main_menu):
        tk.Toplevel.__init__(self)
        self.main_menu = main_menu
        self.title("Registration Form")
        self.geometry('350x300')
        self.configure(bg='#660000') 

        self.label_name = tk.Label(self, text="Name:", bg='#660000', fg='white', font=("Georgia",8))
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.label_id = tk.Label(self, text="ID:", bg='#660000', fg='white', font=("Georgia",8))
        self.label_id.grid(row=1, column=0, padx=10, pady=10)
        self.label_phone = tk.Label(self, text="Phone:", bg='#660000', fg='white', font=("Georgia",8))
        self.label_phone.grid(row=2, column=0, padx=10, pady=10)
        self.label_email = tk.Label(self, text="Email:", bg='#660000', fg='white', font=("Georgia",8))
        self.label_email.grid(row=3, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        self.entry_id = tk.Entry(self)
        self.entry_id.grid(row=1, column=1, padx=10, pady=10)
        self.entry_phone = tk.Entry(self)
        self.entry_phone.grid(row=2, column=1, padx=10, pady=10)
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        self.btn_insert = tk.Button(self, text="Insert", command=self.insert_data, bg='tan', fg='black', font=("Georgia", 8))
        self.btn_insert.grid(row=4, column=0, padx=5, pady=10)

        self.btn_update = tk.Button(self, text="Update", command=self.update_data, bg='tan', fg='black', font=("Georgia", 8))
        self.btn_update.grid(row=4, column=1, padx=5, pady=10)

        self.btn_delete = tk.Button(self, text="Delete", command=self.delete_data, bg='tan', fg='black', font=("Georgia", 8))
        self.btn_delete.grid(row=4, column=2, padx=5, pady=10)

    def insert_data(self):
        id = self.entry_id.get()
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()

        if not name or not phone or not email:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
            
        sql = "INSERT INTO registration (ID, Name, Phone, Email) VALUES (%s, %s, %s, %s)"
        val = (id, name, phone, email)

        print(f"Executing SQL: {sql} with values {val}")
        
        try:
            cursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Success", "Record inserted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error inserting record: {err}")

    def update_data(self):
        id = self.entry_id.get()
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()

        if not id or not name or not phone or not email:
            messagebox.showerror("Error", "Please fill in all fields, including ID.")
            return

        sql = "UPDATE registration SET Name=%s, Phone=%s, Email=%s WHERE ID=%s"
        val = (name, phone, email, id)

        print(f"Executing SQL: {sql} with values {val}")
        
        try:
            cursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Success", "Record updated successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error updating record: {err}")

    def delete_data(self):
        id = self.entry_id.get()

        if not id:
            messagebox.showerror("Error", "Please fill in the ID field.")
            return

        sql = "DELETE FROM registration WHERE ID=%s"
        val = (id,)

        print(f"Executing SQL: {sql} with values {val}")

        try:
            cursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Success", "Record deleted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error deleting record: {err}")

           
class FacilityRentalWindow(tk.Toplevel):
    def __init__(self, main_menu):
        tk.Toplevel.__init__(self)
        self.main_menu = main_menu
        self.title("Facility Management")
        self.geometry('800x600')
        self.configure(bg='#660000') 

        # Add the rest of the facility rental code here...
        label = tk.Label(self, text='SPORT CENTRE', font=("Montserrat Medium", 28, "bold"), bg='#660000', fg='tan')
        label.pack(ipadx=10, ipady=10)

        items_text = tk.Text(self, height=12, width=55, bg='tan') 
        items_text.pack(pady=10)

        items_text.insert(tk.END, "RENT PRICES!\n\n")
        items_text.insert(tk.END, "1. Badminton Racket: RM3\n\n")
        items_text.insert(tk.END, "2. Tennis Racket   : RM3\n\n")
        items_text.insert(tk.END, "3. Pingpong Racket : RM3\n\n")
        items_text.insert(tk.END, "4. Bicycle         : RM8\n\n")
        items_text.insert(tk.END, "5. Netball         : RM5\n\n")
        items_text.insert(tk.END, "6. Basketball      : RM5\n\n")
        items_text.insert(tk.END, "7. Rugby           : RM5\n\n")
        items_text.insert(tk.END, "8. Soccer Ball     : RM5\n\n")
        items_text.insert(tk.END, "9. Court           : RM1\n\n")
        items_text.insert(tk.END, "10. Field          : RM1\n\n")
        items_text.configure(state='disabled')

        frame = tk.Frame(self, bg='tan') 
        frame.pack()

        rental_frame = tk.LabelFrame(frame, text="Rental", bg='tan')
        rental_frame.grid(row=0, column=6, padx=12, pady=8)

        # Dropdown court input
        court_label = tk.Label(rental_frame, text="Court:", bg='tan')
        court_label.pack()

        self.court_var = tk.StringVar(rental_frame)
        self.court_var.set("Select")  # Set a default value
        court_options = ["No", "Court A", "Court B", "Court C", "Court D", "Court E", "Field"]
        court_dropdown = tk.OptionMenu(rental_frame, self.court_var, *court_options)
        court_dropdown.config(bg='tan')  
        court_dropdown.pack()

        # Dropdown items input
        items_label = tk.Label(rental_frame, text="Items:", bg='tan')
        items_label.pack()

        self.items_var = tk.StringVar(rental_frame)
        self.items_var.set("Select")  # Set a default value
        items_dropdown = tk.OptionMenu(rental_frame, self.items_var, "No", "Tennis Racket", "Pingpong Racket","Bicycle", "Netball", "Basketball", "Rugby", "Soccer")
        items_dropdown.config(bg='tan')
        items_dropdown.pack()

        # Count items input
        count_items_label = tk.Label(rental_frame, text="Count Items:", bg='tan')
        count_items_label.pack()
        self.count_items_spinbox = tk.Spinbox(rental_frame, from_=0, to=10)
        self.count_items_spinbox.config(bg='tan')
        self.count_items_spinbox.pack()

        # Dropdown day input
        day_label = tk.Label(rental_frame, text="Day to Rent:", bg='tan')
        day_label.pack()

        # Numeric values for days
        self.day_var = tk.StringVar(self)  # Make day_var an instance variable
        day_options = [f"{i} day" for i in range(0, 31)]
        self.day_var.set(day_options[0])
        day_dropdown = tk.OptionMenu(rental_frame, self.day_var, *day_options)
        day_dropdown.config(bg='tan')
        day_dropdown.pack()

        # Submit button
        submit_button = tk.Button(self, text="Submit Rental", command=self.collect_data, bg='#660000', fg='tan')  
        submit_button.pack(pady=15)

        # Output Label & result
        output_label = tk.Label(self, text="", bg='#660000', fg='#FFFFFF')  
        output_label.pack()

    def collect_data(self):
        # Check if Day_str is not empty before attempting conversion
        Court = self.court_var.get()
        Items = self.items_var.get()
        Count_Items = int(self.count_items_spinbox.get())
        Day_str = self.day_var.get()

        # Extract numerical part from the selected string
        Day = int(''.join(filter(str.isdigit, Day_str)))

        if not Court:
            messagebox.showwarning("Input Error", "Please select Court.")
            return

        if not Items:
            messagebox.showwarning("Input Error", "Please select Items.")
            return

        if Count_Items == 0:
            messagebox.showwarning("Input Error", "Please select Count Items.")
            return
            
        if Day == 0:
            messagebox.showwarning("Input Error", "Please select Day to Rent.")
            return
        
        # Prices for each item
        prices = {
            "Badminton Racket": 3,
            "Tennis Racket": 3,
            "Pingpong Racket": 2,
            "Bicycle": 8,
            "Soccer Ball": 5,
            "Netball": 5,
            "Basketball": 5,
            "Rugby": 5,
            "No": 0,
            "Court A,B,C,D,E,F": 1,
            "Field": 1
        }

        day_price = 1  # Price per day
        item_price = prices[Items]
            
        total_price = (Count_Items * item_price) + (Day * day_price)

        # Insert rental details into the database
        sql = "INSERT INTO rental (Court, Items, Count_Items, Day, Total_Price) VALUES (%s, %s, %s, %s, %s)"
        val = (Court, Items, Count_Items, Day, total_price)
        print(f"Executing SQL: {sql} with values {val}")
        cursor.execute(sql, val)
        mydb.commit()

        # Show confirmation message
        messagebox.showinfo("Confirmation", "Your rental details submitted successfully!")

        # Show bill window
        self.show_bill(Court, Items, Count_Items, Day, total_price)

    def show_bill(court, items, count_items, day, total_price):  
        bill_window = tk.Toplevel()
        bill_window.title("Rental Bill")

        bill_text = tk.Text(bill_window, height=10, width=30,)
        bill_text.pack(pady=10)

        bill_text.insert(tk.END, "Rental Details:\n\n")
        bill_text.insert(tk.END, f"Court: {court}\n")
        bill_text.insert(tk.END, f"Items: {items}\n")
        bill_text.insert(tk.END, f"Count Items: {count_items}\n")
        bill_text.insert(tk.END, f"Day: {day}\n")
        bill_text.insert(tk.END, f"Total Price: RM {total_price}\n")
            
class DamageReportingWindow(tk.Toplevel):
    def __init__(self, main_menu):
        tk.Toplevel.__init__(self)
        self.main_menu = main_menu
        self.title("Damage Reporting")
        self.geometry('600x600')
        self.configure(bg='#660000') 

        prices_text = tk.Text(self, height=18, width=45, bg='tan')
        prices_text.pack(pady=20)

        prices_text.insert(tk.END, "Item & price:\n\n")
        prices_text.insert(tk.END, "badminton racket: RM20\n\n")
        prices_text.insert(tk.END, "tennis racket:    RM30\n\n")
        prices_text.insert(tk.END, "pingpong racket:  RM20\n\n")
        prices_text.insert(tk.END, "bicycle:          RM200\n\n")
        prices_text.insert(tk.END, "soccer ball:      RM40\n\n")
        prices_text.insert(tk.END, "netball:          RM40\n\n")
        prices_text.insert(tk.END, "basketball:       RM40\n\n")
        prices_text.insert(tk.END, "rugby:            RM50\n\n")
        prices_text.configure(state='disabled')

        # Item Type Dropdown
        self.item_var = tk.StringVar(self)
        self.item_var.set("Select Item") 
        trip_dropdown = tk.OptionMenu(self, self.item_var, "badminton racket", "tennis racket", "pingpong racket", "bicycle", "soccer ball", "netball", "basketball", "rugby")
        trip_dropdown.config(bg='tan', fg='black') 
        trip_dropdown.pack(pady=10)

        # Total damaged item spinbox
        item_label = tk.Label(self, text="Total damage:", bg='tan', fg='black', font=("Georgia", 8))
        item_label.pack()
        self.damaged_item_entry = tk.Spinbox(self, from_=0, to=100, bg='tan', fg='black', font=("Georgia", 8) )
        self.damaged_item_entry.pack(pady=10)

        # Save Button
        save_button = tk.Button(self, text="Calculate", command=self.collect_data, bg='tan', fg='black', font=("Georgia", 8))
        save_button.pack(pady=10)

        # Output
        label = tk.Label(self, text='Total price:', bg='tan', fg='black', font=("Georgia", 8))
        label.pack(ipadx=10, ipady=10)
        self.output_label = tk.Label(self, text="", bg='tan', fg='black', font=("Georgia", 8))
        self.output_label.pack()
               
    def collect_data(self):
        global Total_Price  
        Item = self.item_var.get()
        Total_Damaged = int(self.damaged_item_entry.get()) 

        # prices dictionary
        prices = {
            "badminton racket": 20,
            "tennis racket": 30,
            "pingpong racket": 20,
            "bicycle": 200,
            "soccer ball": 40,
            "netball": 40,
            "basketball": 40,
            "rugby": 50,
        }

        Item_Price = prices[Item]
        Total_Price = Total_Damaged * Item_Price
        
        sql = "INSERT INTO `damage` (Item, Total_Damaged, Item_Price, Total_Price) VALUES (%s, %s, %s, %s)"
        val = (Item, Total_Damaged, Item_Price, Total_Price)
        print(f"Executing SQL: {sql} with values {val}")
        cursor.execute(sql, val)
        mydb.commit()

        self.output_label.config(text=f"Item: {Item}, Total damage: {Total_Damaged}\n\n Total Price: RM{Total_Price}")

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()