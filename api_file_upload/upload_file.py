import requests
import base64

def upload_file(token, patient_id, file_path):
    """
    Function to upload a file to the patient's records.
    """
    upload_url = "https://your-openemr-server/apis/default/fhir/DocumentReference"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # read and encode the file
    with open(file_path, "rb") as file:
        encoded_file = base64.b64encode(file.read()).decode("utf-8")

    # JSON payload
    payload = {
        "resourceType": "DocumentReference",
        "status": "current",
        "type": {"text": "Clinical Notes"},
        "subject": {"reference": f"Patient/{patient_id}"},
        "content": [{"attachment": {"contentType": "application/pdf", "data": encoded_file}}]
    }

    response = requests.post(upload_url, headers=headers, json=payload)
    if response.status_code in [200, 201]:
        print("File uploaded successfully.")
    else:
        raise Exception(f"Error uploading file: {response.text}")

if __name__ == "__main__":
    # Test the function
    from get_auth_token import get_access_token
    from patient_search import patient_search

    token = get_access_token()
    patient_name = "John Doe"
    patient_dob = "1980-01-01"
    file_path = "patient_notes.pdf"

    try:
        patient_id = patient_search(token, patient_name, patient_dob)
        upload_file(token, patient_id, file_path)
    except Exception as e:
        print(e)
