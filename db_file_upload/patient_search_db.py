from db_connection import connect_to_db

def patient_search_db(name, dob):
    """
    Search for a patient using name and date of birth in patient_data.
    """
    query = """
        SELECT pid FROM patient_data
        WHERE CONCAT(fname, ' ', lname) = %s AND DOB = %s
    """
    conn = connect_to_db()
    try:
        cursor = conn.cursor()
        cursor.execute(query, (name, dob))
        result = cursor.fetchone()
        if result:
            return result[0]  # return patient ID
        else:
            raise Exception("Patient not found.")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    pid = patient_search_db("John Doe", "1980-01-01")
    print(f"Patient ID: {pid}")
