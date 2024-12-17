import requests

def patient_search(token, name, dob):
    """
    Function to search for a patient using name and date of birth.
    """
    search_url = "https://your-openemr-server/apis/default/fhir/Patient"
    headers = {'Authorization': f'Bearer {token}'}
    params = {'name': name, 'birthdate': dob}

    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code == 200:
        patients = response.json()
        if patients.get('total', 0) > 0:
            patient_id = patients['entry'][0]['resource']['id']
            return patient_id
        else:
            raise Exception("Patient not found.")
    else:
        raise Exception(f"Error in searching for patient: {response.text}")

if __name__ == "__main__":
    from get_auth_token import get_access_token

    token = get_access_token()
    patient_name = "John Doe"
    patient_dob = "1980-01-01"

    try:
        patient_id = patient_search(token, patient_name, patient_dob)
        print("Patient ID:", patient_id)
    except Exception as e:
        print(e)
