from search_patient_db import search_patient_db
from upload_document_db import upload_document_db

def main():
    try:
        # search for patient
        patient_name = "John Doe"
        patient_dob = "1980-01-01"
        patient_id = search_patient_db(patient_name, patient_dob)
        print(f"Patient ID found: {patient_id}")

        # upload document
        file_path = "patient_notes.pdf"
        upload_document_db(patient_id, file_path)

        print("Patient notes uploaded successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
