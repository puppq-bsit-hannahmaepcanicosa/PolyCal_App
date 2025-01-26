import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox, Toplevel
from tkcalendar import Calendar
import tkinter.messagebox as messagebox
from datetime import datetime
from PIL import Image, ImageTk, ImageOps, ImageDraw
from customtkinter import CTkImage
import threading
import time
import sqlite3
import io
import os
import json

# Geometry of the windows
WIDTH = 1024
HEIGHT = 768

DATABASE_NAME = 'Polytechnic.db'

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    # Create events table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            image BLOB,
            highlight_color TEXT
        )
    ''')
    # Create notes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT,
            username TEXT NOT NULL,
            highlight_color TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Remaining code
ctk.set_appearance_mode("Light")

STUDENT_INFO = [
    {
        "id": "2024-00253-PQ-0", "PUPid": "2024-00253-PQ-0", "name": "Cristian Esplana", "program": "BSIT 1-2", "image_path": "C:/Users/Mae/Desktop/PolyCal/PolyCalendar/Profile/Cristian.png"
    },
    {
        "id": "2024-00002-PQ-0", "PUPid": "2024-00002-PQ-0", "name": "Hannah Canicosa", "program": "BSIT 1-2", "image_path": "C:/Users/Mae/Desktop/PolyCal/PolyCalendar/Profile/Hannah.png"
    },
    {
        "id": "2024-00156-PQ-0", "PUPid": "2024-00156-PQ-0", "name": "Cj Acosta", "program": "BSIT 1-2", "image_path": "C:/Users/Mae/Desktop/PolyCal/PolyCalendar/Profile/Cj.png"
    },
    {
        "id": "2024-00118-PQ-0", "PUPid": "2024-00118-PQ-0", "name": "Nicole Melican", "program": "BSIT 1-2", "image_path": "C:/Users/Mae/Desktop/PolyCal/PolyCalendar/Profile/Nicole.png"
    },
    {
        "id": "2024-00107-PQ-0", "PUPid": "2024-00107-PQ-0", "name": "Edgardo Privaldos Jr", "program": "BSIT 1-2", "image_path": "C:/Users/Mae/Desktop/PolyCal/PolyCalendar/Profile/Edgardo.png"
    },
    {
        "id": "2024-00553-PQ-1", "PUPid": "2024-00553-PQ-1", "name": "Jennylyn Vidal", "program": "BSIT Irregular", "image_path": "C:/Users/Mae/Desktop/PolyCal/PolyCalendar/Profile/Jennylyn.png"
    },
    {
        "id": "2024-00321-PQ-0", "PUPid": "2024-00321-PQ-0", "name": "Malupiton ", "program": "BSIT 1-2", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-00412-PQ-0", "PUPid": "2024-00412-PQ-0", "name": "Taylor Swift", "program": "BSIT 1-2", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-00650-PQ-0", "PUPid": "2024-00650-PQ-0", "name": "Kuya Kim", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-00876-PQ-0", "PUPid": "2024-00876-PQ-0", "name": "Jessa Saragosa", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-00745-PQ-0", "PUPid": "2024-00745-PQ-0", "name": "Mark Logan", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-00901-PQ-0", "PUPid": "2024-00901-PQ-0", "name": "Layla Delima", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-01012-PQ-0", "PUPid": "2024-01012-PQ-0", "name": "John Wick", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-01123-PQ-0", "PUPid": "2024-01123-PQ-0", "name": "Selena Gomez", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-01234-PQ-0", "PUPid": "2024-01234-PQ-0", "name": "Bruno Mars", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-01345-PQ-0", "PUPid": "2024-01345-PQ-0", "name": "Sarah Geronimo", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-01456-PQ-0", "PUPid": "2024-01456-PQ-0", "name": "Joshua Garcia", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-01567-PQ-0", "PUPid": "2024-01567-PQ-0", "name": "Billie Ellish", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-01678-PQ-0", "PUPid": "2024-01678-PQ-0", "name": "Daniel Cesear", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    },
    {
        "id": "2024-01789-PQ-0", "PUPid": "2024-01789-PQ-0", "name": "Ariana Grande", "program": "BSIT 2-1", "image_path": "C:/Users/Mae/Desktop/PolyCal/upload.png"
    }
]

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, on_login_success):
        super().__init__(master)
        self.master = master
        self.on_login_success = on_login_success
        self.login_attempts = 0  # Initialize attempt counter
        
        self.create_background()
        self.create_header()
        self.create_login_section()

    def create_background(self):
        try:
            image_path = "C:/Users/Mae/Desktop/PolyCal/bgimage.png"
            image = Image.open(image_path)
            resized_image = image.resize((1920,1060))
            tk_image = ImageTk.PhotoImage(resized_image)

            background_label = ctk.CTkLabel(self, image=tk_image, text="")
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = tk_image
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image not found: {image_path}")

    def create_header(self):
        header_frame = ctk.CTkFrame(self, height=90, fg_color="#b90101")
        header_frame.pack(fill="x", side="top")

        try:
            image_path = "C:/Users/Mae/Desktop/PolyCal/PUPLogo.png"
            image = Image.open(image_path)
            mask = Image.new("L", (50, 50), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 50, 50), fill=255)

            circular_image = ImageOps.fit(image, (50, 50), centering=(0.5, 0.5))
            circular_image.putalpha(mask)

            tk_image = ImageTk.PhotoImage(circular_image)

            image_label = ctk.CTkLabel(header_frame, image=tk_image, text="")
            image_label.image = tk_image
            image_label.pack(side="left", padx=10, pady=10)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image not found: {image_path}")

        ctk.CTkLabel(
        header_frame,
        text="PolyCal",
        font=("Arial", 30, "bold"),
        text_color="white"
        ).pack(side="left", padx=5)

    def create_login_section(self):
        login_frame = ctk.CTkFrame(self, width=400, height=800, fg_color="#f8f7f2", border_width=2, border_color="#b90101")
        login_frame.pack(fill="y", padx=50, pady=200, side="right")
        
        try:
            image_path = "C:/Users/Mae/Desktop/PolyCal/PUPLogo.png"
            image = Image.open(image_path)
            mask = Image.new("L", (70, 70), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 70, 70), fill=255)

            circular_image = ImageOps.fit(image, (70, 70), centering=(0.5, 0.5))
            circular_image.putalpha(mask)

            tk_image = ImageTk.PhotoImage(circular_image)

            image_label = ctk.CTkLabel(login_frame, image=tk_image, text="")
            image_label.image = tk_image
            image_label.pack(padx=20, pady=30)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image not found: {image_path}")

        ctk.CTkLabel(
            login_frame,
            text="PUP Student Calendar",
            font=("Arial", 18, "bold"),
            text_color="#b90101"
        ).pack(pady=0, padx=35)

        ctk.CTkLabel(
        login_frame,
        text="Sign in to your session",
        font=("Arial", 12, "bold"),
        text_color="#b90101"
        ).pack(pady=0)

        self.studentid_entry = ctk.CTkEntry(
        login_frame,
        placeholder_text="PUP Student ID",
        font=("Arial", 12, "bold"),
        width=200
        )
        self.studentid_entry.pack(padx=10, pady=5)

        login_button = ctk.CTkButton(
        login_frame,
        text="Login",
        font=("Arial", 14, "bold"),
        width=70,
        height=30,
        fg_color="#A8192E",
        text_color="white",
        command=self.validate_login
        )
        login_button.pack(padx=20, pady=10)

        # Bind the Enter key to the validate_login method
        self.studentid_entry.bind("<Return>", lambda event: self.validate_login())
    def validate_login(self):
        student_id = self.studentid_entry.get()
        allowed_ids = [student['PUPid'] for student in STUDENT_INFO]

        if student_id.strip() and student_id in allowed_ids:
            student = next((s for s in STUDENT_INFO if s['PUPid'] == student_id), None)
            self.on_login_success(student['PUPid'])
        elif not student_id.strip():
            messagebox.showerror("Login Failed", "Student ID cannot be empty")
            self.login_attempts += 1
        else:
            self.login_attempts += 1
            remaining_attempts = 5 - self.login_attempts
            if remaining_attempts > 0:
                messagebox.showerror("Login Failed", f"Invalid Student ID\nRemaining attempts: {remaining_attempts}")
            else:
                messagebox.showerror("Login Failed", "Maximum login attempts reached. Application will close.")
                self.master.destroy()

def image_to_binary(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return image_file.read()
    except Exception as e:
        print(f"Error reading image file: {e}")
        return None

def binary_to_image(binary_data):
    try:
        from io import BytesIO
        from PIL import Image
        return Image.open(BytesIO(binary_data))
    except Exception as e:
        print(f"Error converting binary to image: {e}")
        return None

def insert_event(event_date, event_title, event_description, event_image, highlight_color=None):
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO events (date, title, description, image, highlight_color) VALUES (?, ?, ?, ?, ?)
            ''', (event_date, event_title, event_description, event_image, highlight_color))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def insert_note(note_date, note_title, note_content, PUPid, highlight_color=None):
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO notes (date, title, content, username, highlight_color) VALUES (?, ?, ?, ?, ?)
            ''', (note_date, note_title, note_content, PUPid, highlight_color))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def update_event_highlight(event_id, highlight_color):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE events SET highlight_color = ? WHERE id = ?
    ''', (highlight_color, event_id))
    conn.commit()
    conn.close()

def update_note_highlight(note_id, highlight_color):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE notes SET highlight_color = ? WHERE id = ?
    ''', (highlight_color, note_id))
    conn.commit()
    conn.close()

def update_event_description(event_id, description):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE events SET description = ? WHERE id = ?
    ''', (description, event_id))
    conn.commit()
    conn.close()

def fetch_event_highlight_color(event_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT highlight_color FROM events WHERE id = ?
    ''', (event_id,))
    highlight_color = cursor.fetchone()
    conn.close()
    return highlight_color[0] if highlight_color else None

def fetch_note_highlight_color(note_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT highlight_color FROM notes WHERE id = ?
    ''', (note_id,))
    highlight_color = cursor.fetchone()
    conn.close()
    return highlight_color[0] if highlight_color else None

def fetch_event_details(event_title, event_date):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT description, image FROM events WHERE title = ? AND date = ?
    ''', (event_title, event_date))
    event = cursor.fetchone()
    conn.close()
    return event

def fetch_events_by_date(event_date):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title, date, description, image FROM events WHERE date = ?
    ''', (event_date,))
    events = cursor.fetchall()
    conn.close()
    return events

def fetch_notes_by_date(note_date, username):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, title, content, date 
        FROM notes 
        WHERE date = ? AND username = ?
    ''', (note_date, username))
    notes = cursor.fetchall()
    conn.close()
    return notes
def fetch_notes_by_title(title, username):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, title, content, date
        FROM notes 
        WHERE LOWER(title) LIKE LOWER(?) 
        AND username = ?
    ''', ('%' + title + '%', username))
    notes = cursor.fetchall()
    conn.close()
    return notes

def fetch_note_details(note_title, note_date):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT content FROM notes WHERE title = ? AND date = ?
    ''', (note_title, note_date))
    note = cursor.fetchone()
    conn.close()
    return note

def fetch_event_id(title, date):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id FROM events WHERE title = ? AND date = ?
    ''', (title, date))
    event_id = cursor.fetchone()
    conn.close()
    return event_id[0] if event_id else None

def fetch_event_highlight_color(self, event_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT highlight_color FROM events WHERE id = ?
    ''', (event_id,))
    color = cursor.fetchone()
    conn.close()
    return color[0] if color else None

def update_event_highlight(self, event_id, color):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('archive.db')
        cursor = conn.cursor()
            
        # Execute a query to update the event highlight color
        cursor.execute("UPDATE events SET highlight_color = ? WHERE id = ?", (color, event_id))
        
        # Commit the changes and close the database connection
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")

def fetch_events_by_title(title):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title, date, description, image 
        FROM events 
        WHERE LOWER(title) LIKE LOWER(?)
    ''', ('%' + title + '%',))
    events = cursor.fetchall()
    conn.close()
    return events

def fetch_notes_by_title(title, username):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, title, content, date
        FROM notes 
        WHERE LOWER(title) LIKE LOWER(?) 
        AND username = ?
    ''', ('%' + title + '%', username))
    notes = cursor.fetchall()
    conn.close()
    return notes

def fetch_events_by_month(month_query):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title, date, description, image 
        FROM events 
        WHERE strftime('%Y-%m', date) = ?
    ''', (month_query,))
    events = cursor.fetchall()
    conn.close()
    return events

def fetch_notes_by_month(month_query, username):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, title, content, date 
        FROM notes 
        WHERE strftime('%Y-%m', date) = ? AND username = ?
    ''', (month_query, username))
    notes = cursor.fetchall()
    conn.close()
    return notes

def fetch_upcoming_events():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title, date FROM events WHERE date >= date('now') ORDER BY date ASC
    ''')
    events = cursor.fetchall()
    conn.close()
    return events

def fetch_all_events(self):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT date, title FROM events
    ''')
    events = cursor.fetchall()
    conn.close()
    return events

def delete_event(event_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM events WHERE id = ?
    ''', (event_id,))
    conn.commit()
    conn.close()

def delete_note(note_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM notes WHERE id = ?
    ''', (note_id,))
    conn.commit()
    conn.close()

def delete_event_and_refresh(self, event_id, popup):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT date FROM events WHERE id = ?', (event_id,))
    event_date = cursor.fetchone()[0]
    
    # Delete the event
    delete_event(event_id)
    
    # Clear all calendar events first
    for event_id in self.calendar_widget.get_calevents():
        self.calendar_widget.calevent_remove(event_id)
    
    # Refresh calendar markings immediately
    self.mark_event_dates()
    
    conn.close()
    popup.destroy()
    messagebox.showinfo("Success", "Event deleted successfully.")

def delete_note_and_refresh(self, note_id, popup):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT date FROM notes WHERE id = ?', (note_id,))
    note_date = cursor.fetchone()[0]
    
    # Delete the note
    delete_note(note_id)
    
    # Clear all calendar events first
    for event_id in self.calendar_widget.get_calevents():
        self.calendar_widget.calevent_remove(event_id)
    
    # Refresh calendar markings immediately
    self.mark_event_dates()
    
    conn.close()
    popup.destroy()
    messagebox.showinfo("Success", "Note deleted successfully.")
        
class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PolyCal")
        self.geometry(f"{1920}x{1080}")
        self.resizable(True, True)
        self.current_date = datetime.now()
        self.show_login_page()
        self.load_events()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def refresh_calendar(self):
        # Clear existing calendar events
        for event_id in self.calendar_widget.get_calevents():
            self.calendar_widget.calevent_remove(event_id)
        
        # Reload events and refresh markings
        self.load_events()
        self.mark_event_dates()

    def on_closing(self):
        messagebox.showinfo("PolyCal", "Thank you for using PolyCal!")
        self.destroy()

    def insert_event(event_date, event_title, event_description, event_image, highlight_color=None):
        try:
            conn = sqlite3.connect(DATABASE_NAME)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO events (date, title, description, image, highlight_color) VALUES (?, ?, ?, ?, ?)
            ''', (event_date, event_title, event_description, event_image, highlight_color))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
 
    def load_events(self):
        events = self.fetch_all_events()  # Use self to call the method
        for event in events:
            self.add_event(event)  # Implement this method to add events to your UI

    def fetch_all_events(self):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT date, title FROM events')
        events = cursor.fetchall()
        conn.close()
        return events

    def add_event(self, event):
        # Implement this method to add an event
        pass

    def show_login_page(self):
        if hasattr(self, 'main_interface'):
            self.main_interface.pack_forget()
        self.login_page = LoginPage(self, self.on_login_success)
        self.login_page.pack(fill="both", expand=True)

    def on_login_success(self, PUPid):
        self.logged_in_PUPid = PUPid
        self.login_page.pack_forget()
        self.show_main_interface(PUPid)

    def show_main_interface(self, PUPid):
        if hasattr(self, 'main_interface'):
            self.main_interface.pack_forget()

        self.main_interface = ctk.CTkFrame(self)
        self.main_interface.pack(fill="both", expand=True)

        self.create_header()
        self.create_footer()
        self.create_sidebar(PUPid)
        self.create_calendar()

    def create_header(self):
        header_frame = ctk.CTkFrame(self.main_interface, height=90, fg_color="#b90101")
        header_frame.pack(fill="x", side="top")

        try:
            image_path = "C:/Users/Mae/Desktop/PolyCal/PUPLogo.png"
            image = Image.open(image_path)
            mask = Image.new("L", (50, 50), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 50, 50), fill=255)

            circular_image = ImageOps.fit(image, (50, 50), centering=(0.5, 0.5))
            circular_image.putalpha(mask)

            tk_image = ImageTk.PhotoImage(circular_image)

            image_label = ctk.CTkLabel(header_frame, image=tk_image, text="")
            image_label.image = tk_image
            image_label.pack(side="left", padx=10, pady=10)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image not found: {image_path}")
            
        ctk.CTkLabel(
            header_frame,
            text="PolyCal",
            font=("Arial", 30, "bold"),
            text_color="white"
        ).pack(side="left", padx=5)

        self.search_entry = ctk.CTkEntry(
        header_frame, 
        placeholder_text="Search by Date (YYYY-MM-DD) or Title", 
        width=300
        )
        self.search_entry.pack(side="left", padx=10, pady=10)

        search_button = ctk.CTkButton(
            header_frame,
            text="Search",
            font=("Arial", 14, "bold"),
            fg_color="#b90101",
            text_color="white",
            width=20,
            height=20,
            command=self.search_by_date)
        search_button.pack(side="left", padx=0)

        sign_out_button = ctk.CTkButton(
            header_frame,
            text="Sign Out",
            font=("Arial", 14, "bold"),
            width=30,
            height=30,
            fg_color="#b90101",
            text_color="white",
            command=self.sign_out
        )
        sign_out_button.pack(side="right", padx=15)

    def search_by_date(self):
        class SearchResultsDialog(ctk.CTkToplevel):
            def __init__(dialog_self):
                super().__init__(self)
                dialog_self.title("Search Results")
                dialog_self.geometry("800x600")
                dialog_self.configure(bg="#f8f7f2")
                dialog_self.transient(self)
                dialog_self.grab_set()
                dialog_self.focus_set()

                search_query = self.search_entry.get().strip().lower()
                
                if not search_query:
                    messagebox.showerror("Error", "Please enter a date, month, or title to search.")
                    dialog_self.destroy()
                    return

                dialog_self.scrollable_frame = ctk.CTkScrollableFrame(dialog_self, orientation="vertical", width=800, height=600)
                dialog_self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

                try:
                    # Check if query is a specific date (YYYY-MM-DD)
                    date_obj = datetime.strptime(search_query, '%Y-%m-%d')
                    events = fetch_events_by_date(search_query)
                    notes = fetch_notes_by_date(search_query, self.logged_in_username)
                except ValueError:
                    try:
                        # Check if query is a month and year (e.g., January 2025)
                        date_obj = datetime.strptime(search_query, '%B %Y')
                        month_query = date_obj.strftime('%Y-%m')  # Converts to "2025-01"
                        events = fetch_events_by_month(month_query)
                        notes = fetch_notes_by_month(month_query, self.logged_in_username)
                    except ValueError:
                        try:
                            # Check if query is a full date (e.g., January 01 2025)
                            date_obj = datetime.strptime(search_query, '%B %d %Y')
                            formatted_date = date_obj.strftime('%Y-%m-%d')  # Converts to "2025-01-01"
                            events = fetch_events_by_date(formatted_date)
                            notes = fetch_notes_by_date(formatted_date, self.logged_in_username)
                        except ValueError:
                            # Default to searching by title
                            events = fetch_events_by_title(search_query)
                            notes = fetch_notes_by_title(search_query, self.logged_in_username)

                if not events and not notes:
                    no_results_label = ctk.CTkLabel(
                        dialog_self.scrollable_frame,
                        text="No matching events or notes found.",
                        font=("Arial", 14)
                    )
                    no_results_label.pack(pady=20)
                    return

                results_dict = {}
                for event in events:
                    key = event[1]  # Use the event's date as the grouping key
                    if key not in results_dict:
                        results_dict[key] = {'events': [], 'notes': []}
                    results_dict[key]['events'].append(event)

                for note in notes:
                    key = note[3]  # Use the note's date as the grouping key
                    if key not in results_dict:
                        results_dict[key] = {'events': [], 'notes': []}
                    results_dict[key]['notes'].append(note)

                for key, items in results_dict.items():
                    group_frame = ctk.CTkFrame(dialog_self.scrollable_frame, fg_color="#f8f7f2",border_width=5 , corner_radius=10)
                    group_frame.pack(fill="x", padx=5, pady=5)

                    ctk.CTkLabel(group_frame, text=f"Results for {key}", font=("Arial", 18, "bold")).pack(pady=5)

                    for event in items['events']:
                        title, date, description, image_data = event[:4]
                        dialog_self.create_event_frame(title, date, description, image_data, parent=group_frame)

                    for note in items['notes']:
                        note_id, title, content, date = note[:4]
                        dialog_self.create_note_frame(note_id, title, date, content, parent=group_frame)

            def create_event_frame(dialog_self, event_title, event_date, event_description, event_image_data, parent=None):
                parent = parent or dialog_self.scrollable_frame
                event_frame = ctk.CTkFrame(parent, fg_color="#f7f8f2", corner_radius=10, border_width=5, border_color="#fad02c")
                event_frame.pack(fill="x", padx=10, pady=10)

                event_header = ctk.CTkFrame(event_frame, fg_color="#b90101")
                event_header.pack(fill="x", side="top", padx=5, pady=5)

                ctk.CTkLabel(event_header, text=f"{event_title}", font=("Arial", 22, "bold"), text_color="white").pack(pady=5)
                ctk.CTkLabel(event_header, text=f"{event_date}", font=("Arial", 14, "bold"), text_color="white").pack(pady=5)

                event_sidebar = ctk.CTkFrame(event_frame, fg_color="#f8f7f2", corner_radius=10, border_width=2, border_color="#fad02c")
                event_sidebar.pack(side="left", padx=10, pady=10)

                ctk.CTkLabel(event_sidebar, text="Description:", font=("Arial", 16, "bold")).pack(pady=5)
                description_text = ctk.CTkTextbox(event_sidebar, fg_color="lightgray", border_width=1, border_color="#b90101", height=100, width=300)
                description_text.insert("1.0", event_description)
                description_text.pack(pady=5)

                if event_image_data:
                    try:
                        event_image = Image.open(io.BytesIO(event_image_data))
                        ctk_image = CTkImage(light_image=event_image, dark_image=event_image, size=(400, 300))
                        img_label = ctk.CTkLabel(event_frame, image=ctk_image, text="")
                        img_label.image = ctk_image
                        img_label.pack(pady=10)
                    except Exception as e:
                        print(f"Error loading image: {e}")

                ctk.CTkButton(event_sidebar, text="Save Description", 
                            command=lambda: self.save_description(event_title, event_date, description_text.get("1.0", "end-1c"))).pack(pady=5)
                ctk.CTkButton(event_sidebar, text="Delete Event", 
                            command=lambda: self.delete_event_and_refresh(fetch_event_id(event_title, event_date), dialog_self)).pack(pady=5)

            def create_note_frame(dialog_self, note_id, note_title, note_date, note_content, parent=None):
                parent = parent or dialog_self.scrollable_frame
                note_frame = ctk.CTkFrame(parent, fg_color="#f7f8f2", corner_radius=10, border_width=5, border_color="#fad02c")
                note_frame.pack(fill="x", padx=10, pady=10)

                note_header = ctk.CTkFrame(note_frame, fg_color="#b90101")
                note_header.pack(fill="x", side="top", padx=5, pady=5)

                ctk.CTkLabel(note_header, text=f"{note_title}", font=("Arial", 22, "bold"), text_color="white").pack(pady=5)
                ctk.CTkLabel(note_header, text=f"{note_date}", font=("Arial", 14), text_color="white").pack(pady=5)

                ctk.CTkLabel(note_frame, text="Content:", font=("Arial", 16, "bold")).pack(pady=5)
                content_text = ctk.CTkTextbox(note_frame, fg_color="lightgray", border_width=1, border_color="#b90101", height=100, width=300)
                content_text.insert("1.0", note_content)
                content_text.pack(pady=5)

                ctk.CTkButton(note_frame, text="Save Content", 
                            command=lambda: self.save_note_content(note_title, note_date, content_text.get("1.0", "end-1c"))).pack(pady=5)
                ctk.CTkButton(note_frame, text="Delete Note", 
                            command=lambda: self.delete_note_and_refresh(note_id, dialog_self)).pack(pady=5)

        SearchResultsDialog()



    def create_sidebar(self, PUPid):
        sidebar = ctk.CTkFrame(self.main_interface, height=300 ,width=200, fg_color="#f8f7f2", corner_radius=15, border_width=2, border_color="#fad02c")
        sidebar.pack(fill="y", side="left", padx=40, pady=100)
        student = next((s for s in STUDENT_INFO if s['PUPid'] == PUPid), None)

        if student:
            try:
                image_path = student['image_path']
                image = Image.open(image_path)
                circular_image = ImageOps.fit(image, (100, 100), centering=(0.5, 0.5))
                tk_image = ImageTk.PhotoImage(circular_image)

                self.profile_picture_label = ctk.CTkLabel(sidebar, image=tk_image, text="")
                self.profile_picture_label.image = tk_image
                self.profile_picture_label.pack(pady=10)
            except FileNotFoundError:
                messagebox.showerror("Error", f"Image not found: {image_path}")


            ctk.CTkLabel(
                sidebar,
                text=f"  Welcome, {student['name']}!  ",
                font=("Arial", 18, "bold"),
                text_color="#A8192E"
            ).pack(pady=5, padx=20)

            ctk.CTkLabel(
                sidebar,
                text=f"ID: {student['id']}\nProgram: {student['program']}",
                font=("Arial", 14),
                text_color="#A8192E"
            ).pack(pady=10)

            ctk.CTkButton( 
                sidebar,
                text="Add Event",
                font=("Arial", 12, "bold"),
                fg_color="#A8192E",
                text_color="white",
                command=self.option_add
            ).pack(pady=5)

            ctk.CTkButton(
                sidebar,
                text="View Events",
                font=("Arial", 12, "bold"),
                fg_color="#A8192E",
                text_color="white",
                command=self.view_events
            ).pack(pady=5)

            ctk.CTkButton(
                sidebar,
                text="Add Notes",
                font=("Arial", 12, "bold"),
                fg_color="#A8192E",
                text_color="white",
                command=self.add_notes
            ).pack(pady=5)

            ctk.CTkButton(
                sidebar,
                text="View Notes",
                font=("Arial", 12, "bold"),
                fg_color="#A8192E",
                text_color="white",
                command=self.view_notes
            ).pack(pady=5)
        
    def add_notes(self):
        class AddNoteDialog(ctk.CTkToplevel):
            def __init__(dialog_self):
                super().__init__(self)
                dialog_self.title("Add Note")
                dialog_self.geometry("400x400")
                dialog_self.transient(self)
                dialog_self.grab_set()
                dialog_self.focus_set()

                # Note Title
                ctk.CTkLabel(dialog_self, text="Note Title:", font=("Arial", 12, "bold")).pack(pady=(10, 5))
                dialog_self.title_entry = ctk.CTkEntry(dialog_self, width=300)
                dialog_self.title_entry.pack(pady=(0, 10))

                # Note Content
                ctk.CTkLabel(dialog_self, text="Note Content:", font=("Arial", 12, "bold")).pack(pady=(10, 5))
                dialog_self.content_entry = ctk.CTkTextbox(dialog_self, width=300, height=100)
                dialog_self.content_entry.pack(pady=(0, 10))

                # Buttons
                ctk.CTkButton(dialog_self, text="Add Note", fg_color="#A8192E",text_color="white",command=dialog_self.add_note).pack(pady=(20, 5))
                ctk.CTkButton(dialog_self, text="Cancel", fg_color="#A8192E",text_color="white", command=dialog_self.destroy).pack(pady=(5, 10))

            def add_note(dialog_self):
                selected_date = self.calendar_widget.get_date()
                date_obj = datetime.strptime(selected_date, '%m/%d/%y')
                formatted_date = date_obj.strftime('%Y-%m-%d')
                
                note_title = dialog_self.title_entry.get().strip()
                note_content = dialog_self.content_entry.get("1.0", "end").strip()

                if not note_title or not note_content:
                    messagebox.showerror("Error", "Note title and content cannot be empty.")


                # Insert note with formatted date
                insert_note(formatted_date, note_title, note_content, self.logged_in_username)
                messagebox.showinfo("Success", f"Note '{note_title}' added on {formatted_date}.")
                dialog_self.destroy()

        # Open the Add Note dialog
        AddNoteDialog()

    def option_add(self):
        class AddEventDialog(ctk.CTkToplevel):
            def __init__(dialog_self):
                super().__init__(self)
                dialog_self.title("Add Event")
                dialog_self.geometry("400x500")
                dialog_self.transient(self)
                dialog_self.grab_set()
                dialog_self.focus_set()

                # Event Title
                ctk.CTkLabel(dialog_self, text="Event Title:", font=("Arial", 12, "bold")).pack(pady=(10, 5))
                dialog_self.title_entry = ctk.CTkEntry(dialog_self, width=300)
                dialog_self.title_entry.pack(pady=(0, 10))

                # Event Description and the word are limit in 500 characters
                ctk.CTkLabel(dialog_self, text="Event Description:", font=("Arial", 12, "bold")).pack(pady=(10, 5))
                ctk.CTkLabel(dialog_self, text="150 characters only", font=("Arial", 9)).pack(pady=(2))
                dialog_self.description_entry = ctk.CTkEntry(dialog_self, width=300, height=100)
                dialog_self.description_entry.pack(pady=(0, 10))

                # Image Upload
                ctk.CTkButton(dialog_self, text="Upload Image", fg_color="#A8192E",text_color="white",command=dialog_self.upload_image).pack(pady=(10, 5))
                dialog_self.image_label = ctk.CTkLabel(dialog_self, text="No image selected", font=("Arial", 10))
                dialog_self.image_label.pack(pady=(0, 10))

                # Buttons
                ctk.CTkButton(dialog_self, text="Add Event", fg_color="#A8192E", text_color="white",command=dialog_self.add_event).pack(pady=(20, 5))
                ctk.CTkButton(dialog_self, text="Close", fg_color="#A8192E",text_color="white",command=dialog_self.destroy).pack(pady=(5, 10))

                # Internal variables
                dialog_self.image_path = None

            def upload_image(dialog_self):
                dialog_self.image_path = filedialog.askopenfilename(
                    title="Upload Image for the Event",
                    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
                )
                if dialog_self.image_path:
                    dialog_self.image_label.configure(text=f"Selected: {dialog_self.image_path.split('/')[-1]}")

            def add_event(dialog_self):
                selected_date = self.calendar_widget.get_date()
                date_obj = datetime.strptime(selected_date, '%m/%d/%y')
                formatted_date = date_obj.strftime('%Y-%m-%d')
                
                title = dialog_self.title_entry.get().strip()
                description = dialog_self.description_entry.get().strip()
                
                # Add word count validation
                word_count = len(description.split())
                if word_count > 150:
                    messagebox.showerror("Error", "Description cannot exceed 150 words.")
                    return

                if not title:
                    messagebox.showerror("Error", "Event title cannot be empty.")
                    return

                event_image = None
                if dialog_self.image_path:
                    event_image = image_to_binary(dialog_self.image_path)

                insert_event(formatted_date, title, description, event_image)
                self.calendar_widget.calevent_create(date_obj, title, 'event')
                self.calendar_widget.tag_config('event', background='#DF9755')
                self.mark_event_dates()
                
                messagebox.showinfo("Success", f"Event '{title}' added on {formatted_date}.")
                dialog_self.destroy()
        # Open the Add Event dialog
        AddEventDialog()

    def view_events(self):
        class ViewEventsDialog(ctk.CTkToplevel):
            def __init__(dialog_self):
                super().__init__(self)
                dialog_self.title("Event Details")
                dialog_self.geometry("800x600")
                dialog_self.configure(bg="white")
                dialog_self.transient(self)
                dialog_self.grab_set()
                dialog_self.focus_set()

                selected_date = self.calendar_widget.get_date()
                date_obj = datetime.strptime(selected_date, '%m/%d/%y')
                formatted_date = date_obj.strftime('%Y-%m-%d')
                events_on_date = fetch_events_by_date(formatted_date)

                if not events_on_date:
                    messagebox.showinfo("No Event", "No event found for this date.")
                    dialog_self.destroy()
                    return

                dialog_self.scrollable_frame = ctk.CTkScrollableFrame(dialog_self, orientation="vertical", width=800, height=600)
                dialog_self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

                for event_data in events_on_date:
                    event_title = event_data[0]
                    event_details = fetch_event_details(event_title, formatted_date)

                    if event_details:
                        event_description, event_image_data = event_details
                        event_image = None
                        
                        if event_image_data:
                            try:
                                if isinstance(event_image_data, str):
                                    event_image_data = event_image_data.encode()
                                event_image = Image.open(io.BytesIO(event_image_data))
                            except Exception as e:
                                print(f"Error loading image: {e}")
                                event_image = None
                    else:
                        event_description = "No description available."
                        event_image = None

                    dialog_self.create_event_frame(event_title, formatted_date, event_description, event_image)

            def create_event_frame(dialog_self, event_title, selected_date, event_description, event_image):
                event_frame = ctk.CTkFrame(dialog_self.scrollable_frame, fg_color="#f7f8f2", corner_radius=10, border_width=5, border_color="#fad02c")
                event_frame.pack(fill="x", padx=10, pady=10)

                # Event Header
                event_header = ctk.CTkFrame(event_frame, fg_color="#b90101")
                event_header.pack(fill="x", side="top", padx=5, pady=5)

                ctk.CTkLabel(event_header, text=f"{event_title}", font=("Arial", 22, "bold"), text_color="white").pack(pady=5)
                ctk.CTkLabel(event_header, text=f"{selected_date}", font=("Arial", 14, "bold"), text_color="white").pack(pady=5)

                event_sidebar = ctk.CTkFrame(event_frame, fg_color="#f8f7f2", corner_radius=10, border_width=2, border_color="#fad02c")
                event_sidebar.pack(fill="y", side="left", padx=5, pady=5)

                # Event Description
                ctk.CTkLabel(event_sidebar, text="Description:", font=("Arial", 16, "bold"), text_color="black").pack(pady=5)
                description_text = ctk.CTkTextbox(event_sidebar, fg_color="lightgray", border_width=2, border_color="#b90101", height=200, width=300)
                description_text.insert("1.0", event_description)
                description_text.pack(pady=5)

                # Event Image
                if event_image:
                    ctk_image = CTkImage(light_image=event_image, dark_image=event_image, size=(400, 300))
                    img_label = ctk.CTkLabel(event_frame, image=ctk_image, text="")
                    img_label.image = ctk_image
                    img_label.pack(pady=10)

                # Buttons
                ctk.CTkButton(event_sidebar, text="Save Description", font=("Arial", 12, "bold"), text_color="white", fg_color="#A8192E",
                            command=lambda: self.save_description(event_title, selected_date, description_text.get("1.0", "end-1c"))).pack(pady=5)

                ctk.CTkButton(event_sidebar, text="Delete Event", font=("Arial", 12, "bold"), text_color="white", fg_color="#A8192E",
                            command=lambda: dialog_self.confirm_delete_event(event_title, selected_date)).pack(pady=5)

            def confirm_delete_event(dialog_self, title, date):
                if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the event '{title}'?"):
                    event_id = fetch_event_id(title, date)
                    self.delete_event_and_refresh(event_id, dialog_self)
                    messagebox.showinfo("Success", "Event deleted successfully!")
                    dialog_self.destroy()
                    self.view_events()
                else:
                    messagebox.showinfo("Canceled", "Deletion canceled.")

            def delete_event_and_refresh(dialog_self, event_id, dialog_instance):
                # Delete the event and refresh the dialog
                delete_event(event_id)
                messagebox.showinfo("Success", "Event deleted successfully!")
                dialog_instance.destroy()
                self.view_events()

        # Open the View Events dialog
        ViewEventsDialog()


    def view_notes(self):
        class ViewNotesDialog(ctk.CTkToplevel):
            def __init__(dialog_self):
                super().__init__(self)
                dialog_self.title("Notes Details")
                dialog_self.geometry("800x600")
                dialog_self.configure(bg="#f8f7f2")
                dialog_self.transient(self)
                dialog_self.grab_set()
                dialog_self.focus_set()

                selected_date = self.calendar_widget.get_date()
                date_obj = datetime.strptime(selected_date, '%m/%d/%y')
                formatted_date = date_obj.strftime('%Y-%m-%d')
                notes_on_date = fetch_notes_by_date(formatted_date, self.logged_in_username)

                if not notes_on_date:
                    messagebox.showinfo("No Notes", "No notes found for this date.")
                    dialog_self.destroy()
                    return

                dialog_self.scrollable_frame = ctk.CTkScrollableFrame(dialog_self, orientation="vertical", width=800, height=600)
                dialog_self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

                for note_data in notes_on_date:
                    note_id = note_data[0]
                    note_title = note_data[1]
                    note_content = note_data[2]

                    dialog_self.create_note_frame(note_id, note_title, formatted_date, note_content)


            def create_note_frame(dialog_self, note_id, note_title, selected_date, note_content):
                note_frame = ctk.CTkFrame(dialog_self.scrollable_frame, fg_color="#f7f8f2", corner_radius=10, border_width=5, border_color="#fad02c")
                note_frame.pack(fill="x", padx=10, pady=10)

                # Note Header
                note_header = ctk.CTkFrame(note_frame, fg_color="#b90101")
                note_header.pack(fill="x", side="top", padx=5, pady=5)

                ctk.CTkLabel(note_header, text=f"{note_title}", font=("Arial", 22, "bold"), text_color="white").pack(pady=5)
                ctk.CTkLabel(note_header, text=f"{selected_date}", font=("Arial", 14), text_color="white").pack(pady=5)

                # Note Content
                ctk.CTkLabel(note_frame, text="Content:", font=("Arial", 16, "bold")).pack(pady=5)
                content_text = ctk.CTkTextbox(note_frame, fg_color="lightgray", border_width=2, border_color="#b90101", height=200, width=300)
                content_text.insert("1.0", note_content)
                content_text.pack(pady=5)

                # Save Button
                ctk.CTkButton(note_frame, text="Save Content", font=("Arial", 12, "bold"), text_color="white", fg_color="#A8192E",
                            command=lambda: self.save_note_content(note_title, selected_date, content_text.get("1.0", "end-1c"))).pack(pady=5)

                # Delete Button with Confirmation
                ctk.CTkButton(note_frame, text="Delete Note", font=("Arial", 12, "bold"), text_color="white", fg_color="#A8192E",
                            command=lambda: dialog_self.confirm_delete_note(note_id, note_title)).pack(pady=5)

            def confirm_delete_note(dialog_self, note_id, note_title):
                if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the note '{note_title}'?"):
                    self.delete_note_and_refresh(note_id, dialog_self)
                    messagebox.showinfo("Success", "Note deleted successfully!")
                    dialog_self.destroy()
                    self.view_notes()
                else:
                    messagebox.showinfo("Canceled", "Deletion canceled.")

        # Open the View Notes dialog
        ViewNotesDialog()

    def delete_event(self, event_id):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('archive.db')
            cursor = conn.cursor()
            
            # Mark the event as deleted
            cursor.execute("UPDATE events SET deleted = 1 WHERE id = ?", (event_id,))
            
            # Commit the changes and close the database connection
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def delete_note(self, note_id):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('archive.db')
            cursor = conn.cursor()
            
            # Mark the note as deleted
            cursor.execute("UPDATE archive SET deleted = 1 WHERE id = ?", (note_id,))
            
            # Commit the changes and close the database connection
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def delete_event_and_refresh(self, event_id, popup):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT date FROM events WHERE id = ?', (event_id,))
        event_date = cursor.fetchone()[0]
        
        # Delete the event
        delete_event(event_id)
        
        # Clear all calendar events first
        for event_id in self.calendar_widget.get_calevents():
            self.calendar_widget.calevent_remove(event_id)
        
        # Refresh calendar markings immediately
        self.mark_event_dates()
        
        conn.close()
        popup.destroy()
        messagebox.showinfo("Success", "Event deleted successfully.")

    def delete_note_and_refresh(self, note_id, popup):
        try:
            conn = sqlite3.connect(DATABASE_NAME)
            cursor = conn.cursor()
            
            # First verify if the note exists
            cursor.execute('SELECT date FROM notes WHERE id = ?', (note_id,))
            result = cursor.fetchone()
            
            if result:
                note_date = result[0]
                # Delete the note
                delete_note(note_id)
                
                # Clear all calendar events
                for event_id in self.calendar_widget.get_calevents():
                    self.calendar_widget.calevent_remove(event_id)
                
                # Refresh calendar markings
                self.mark_event_dates()
                
                conn.close()
                popup.destroy()
                messagebox.showinfo("Success", "Note deleted successfully.")
            else:
                messagebox.showerror("Error", "Note not found.")
                
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
        finally:
            if conn:
                conn.close()
        
    def save_description(self, event_title, event_date, description):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE events SET description = ? WHERE title = ? AND date = ?
        ''', (description, event_title, event_date))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Description updated successfully.")

    def save_feedback(self, event_title, event_date, feedback):
        # Placeholder function to save feedback in the database
        # Replace this with actual database update logic
        print(f"Event Title: {event_title}")
        print(f"Event Date: {event_date}")
        print(f"Feedback: {feedback}")
        messagebox.showinfo("Success", "Feedback saved successfully.")

    def save_note_content(self, note_title, note_date, content):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE notes SET content = ? WHERE title = ? AND date = ?
        ''', (content, note_title, note_date))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Content updated successfully.")

    def on_login_success(self, username):
        self.logged_in_username = username
        self.login_page.pack_forget()
        self.show_main_interface(username)
        
    
    def fetch_upcoming_events():
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT title, date FROM events WHERE date >= date('now') ORDER BY date ASC
        ''')
        events = cursor.fetchall()
        conn.close()
        return events

    def display_upcoming_events(self):
        upcoming_events = fetch_upcoming_events()
        for event in upcoming_events:
            event_label = ctk.CTkLabel(self.main_interface, text=f"{event[1]}: {event[0]}", font=("Arial", 12))  # Corrected line
            event_label.pack(pady=5)

    def create_calendar(self):
        calendar_frame = ctk.CTkFrame(self.main_interface, fg_color="#fad02c", corner_radius=15, border_width=5, border_color="#f8f7f2", width=600, height=400)
        calendar_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.calendar_widget = Calendar(calendar_frame, selectmode="day",
                                    font="Arial 12 bold italic",
                                    showweeknumbers=False, 
                                    showothermonthdays=False, 
                                    background='#fad02c', 
                                    foreground='black', 
                                    bordercolor='#fad02c', 
                                    borderwidth=5,
                                    headersbackground='#fad02c',
                                    selectbackground='lightblue',
                                    normalbackground='#f8f7f2',
                                    weekendbackground='lightgray',
                                    monthbackground="#fad02c",
                                    weekendforeground='black')
        self.calendar_widget.pack(expand=True, fill="both", padx=10, pady=10)

        self.mark_event_dates()

    def mark_event_dates(self):
        # Clear existing calendar markings first
        for event_id in self.calendar_widget.get_calevents():
            self.calendar_widget.calevent_remove(event_id)

        # Get current events and notes from database
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Mark events (visible to all)
        cursor.execute('SELECT DISTINCT date FROM events ORDER BY date')
        event_dates = cursor.fetchall()
        
        # Mark notes (only for logged-in user)
        cursor.execute('SELECT DISTINCT date FROM notes WHERE username = ? ORDER BY date', 
                    (self.logged_in_username,))
        note_dates = cursor.fetchall()
        
        conn.close()

        # Mark dates that have events
        for date_tuple in event_dates:
            date_str = date_tuple[0]
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                self.calendar_widget.calevent_create(date_obj, "Event", "event")
            except ValueError:
                continue
        
        # Mark dates that have notes
        for date_tuple in note_dates:
            date_str = date_tuple[0]
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                self.calendar_widget.calevent_create(date_obj, "Note", "note")
            except ValueError:
                continue
        
        # Configure distinct colors for events and notes
        self.calendar_widget.tag_config("event", background="#DF9755")  # Orange for events
        self.calendar_widget.tag_config("note", background="#90EE90")   # Light green for notes


    def is_date_string_valid(self, date_string, date_format='%Y-%m-%d'):
        """Check if the date_string matches the date_format."""
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False


    def update_calendar(self):
        # Clear existing calendar events
        for tag in self.calendar_widget.get_calevents():
            self.calendar_widget.calevent_remove(tag)
        
        # Reload events
        self.load_events()

    def show_event_popup(self, event):
        selected_date = self.calendar_widget.get_date()
        events_on_date = fetch_events_by_date(selected_date)
        notes_on_date = fetch_notes_by_date(selected_date)

        if not events_on_date and not notes_on_date:
            messagebox.showinfo("No Events or Notes", "There are no events or notes on this date.")
            return

        popup = Toplevel(self)
        popup.title("Details")
        popup.geometry("400x600")

        if events_on_date:
            for event_data in events_on_date:
                event_title = event_data[0]
                event_details = fetch_event_details(event_title, selected_date)

                if event_details:
                    event_description, event_image_data = event_details
                    event_image = Image.open(io.BytesIO(event_image_data)) if event_image_data else None
                else:
                    event_description = "No description available."
                    event_image = None

                title_label = ctk.CTkLabel(popup, text=f"Event: {event_title}", font=("Arial", 16))
                title_label.pack(pady=10)

                date_label = ctk.CTkLabel(popup, text=f"Date: {selected_date}", font=("Arial", 14))
                date_label.pack(pady=5)

                description_label = ctk.CTkLabel(popup, text="Description:", font=("Arial", 14))
                description_label.pack(pady=5)
                description_text = ctk.CTkTextbox(popup, height=5, width=40)
                description_text.insert("1.0", event_description)
                description_text.pack(pady=5)

                if event_image:
                    img_tk = ImageTk.PhotoImage(event_image)
                    img_label = ctk.CTkLabel(popup, image=img_tk)
                    img_label.image = img_tk  # Keep reference to the image
                    img_label.pack(pady=10)

                save_button = ctk.CTkButton(popup, text="Save Description", command=lambda: self.save_description(event_title, selected_date, description_text.get("1.0", "end-1c")))
                save_button.pack(pady=10)

                feedback_label = ctk.CTkLabel(popup, text="Feedback:", font=("Arial", 14))
                feedback_label.pack(pady=5)
                feedback_text = ctk.CTkTextbox(popup, height=5, width=40)
                feedback_text.pack(pady=5)

                save_feedback_button = ctk.CTkButton(popup, text="Save Feedback", command=lambda: self.save_feedback(event_title, selected_date, feedback_text.get("1.0", "end-1c")))
                save_feedback_button.pack(pady=10)

        if notes_on_date:
            for note_data in notes_on_date:
                note_title = note_data[0]
                note_details = fetch_note_details(note_title, selected_date)

                if note_details:
                    note_content = note_details[0]
                else:
                    note_content = "No content available."

                note_title_label = ctk.CTkLabel(popup, text=f"Note: {note_title}", font=("Arial", 16))
                note_title_label.pack(pady=10)

                note_date_label = ctk.CTkLabel(popup, text=f"Date: {selected_date}", font=("Arial", 14))
                note_date_label.pack(pady=5)

                note_content_label = ctk.CTkLabel(popup, text="Content:", font=("Arial", 14))
                note_content_label.pack(pady=5)
                note_content_text = ctk.CTkTextbox(popup, height=5, width=40)
                note_content_text.insert("1.0", note_content)
                note_content_text.pack(pady=5)

                save_note_button = ctk.CTkButton(popup, text="Save Content", command=lambda: self.save_note_content(note_title, selected_date, note_content_text.get("1.0", "end-1c")))
                save_note_button.pack(pady=10)

        popup.mainloop()
    def create_footer(self):
        footer_frame = ctk.CTkFrame(self.main_interface, height=60, fg_color="#A8192E")
        footer_frame.pack(fill="x", side="bottom")
        ctk.CTkLabel(
            footer_frame,
            text=f"Today's Date: {self.current_date.strftime('%B %d, %Y')}",
            font=("Arial", 12),
            text_color="white"
        ).pack(pady=10)

    def sign_out(self):
        confirm = messagebox.askyesno(
            "Sign Out",
            "Are you sure you want to sign out?",
            icon='question'
        )
        
        if confirm:
            # Destroy all toplevel windows
            for widget in self.winfo_children():
                if isinstance(widget, tk.Toplevel):
                    widget.destroy()
                    
            # Clear main interface
            if hasattr(self, 'main_interface'):
                self.main_interface.pack_forget()
                
            self.show_login_page()

    def loop_login(self, delay=5):
        def loop():
            while True:
                time.sleep(delay)
                self.sign_out()
        threading.Thread(target=loop, daemon=True).start()

if __name__ == "__main__": 
    app = Application()
    app.mainloop()