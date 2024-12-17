from auth import get_access_token
from search_patient import search_patient
from upload_file import upload_file

def main():
    try:
        # get access token
        token = get_access_token()
        print("Access Token obtained.")

        # search for patient
        patient_name = "John Doe"
        patient_dob = "1980-01-01"
        patient_id = search_patient(token, patient_name, patient_dob)
        print(f"Found Patient ID: {patient_id}")

        # upload file
        file_path = "patient_notes.pdf"
        upload_file(token, patient_id, file_path)
        print("File uploaded successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
