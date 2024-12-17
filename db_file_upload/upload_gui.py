import tkinter as tk
from tkinter import filedialog, messagebox
from patient_search_db import search_patient_db
from upload_doc_db import upload_document_db

def upload_file():
    try:
        name = name_entry.get()
        dob = dob_entry.get()
        file_path = filedialog.askopenfilename(title="Select Patient File")
        
        if not file_path:
            messagebox.showerror("Error", "No file selected.")
            return

        # search for patient and upload
        patient_id = search_patient_db(name, dob)
        upload_document_db(patient_id, file_path)
        
        messagebox.showinfo("Success", "File uploaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
app = tk.Tk()
app.title("Patient Notes Uploader")

# patient name entry
tk.Label(app, text="Patient Name:").grid(row=0, column=0)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

# DOB Entry
tk.Label(app, text="Date of Birth (YYYY-MM-DD):").grid(row=1, column=0)
dob_entry = tk.Entry(app)
dob_entry.grid(row=1, column=1)

# upload button
upload_button = tk.Button(app, text="Upload File", command=upload_file)
upload_button.grid(row=2, column=0, columnspan=2)

app.mainloop()
