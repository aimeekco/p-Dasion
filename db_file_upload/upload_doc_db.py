from db_connection import connect_to_db
import os
import datetime

def upload_doc_db(patient_id, file_path):
    """
    Upload file metadata into the OpenEMR documents table.
    """
    # extract file information
    file_name = os.path.basename(file_path)
    file_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_size = os.path.getsize(file_path)

    # path where files are stored in OpenEMR (adjust as needed)
    document_dir = "/var/www/html/openemr/sites/default/documents"
    file_dest = os.path.join(document_dir, str(patient_id), file_name)

    # insert metadata into the 'documents' table
    insert_query = """
        INSERT INTO documents (foreign_id, url, date, size, mimetype, docname)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    conn = connect_to_db()
    try:
        # copy the file to the destination folder
        os.makedirs(os.path.dirname(file_dest), exist_ok=True)
        os.system(f"cp {file_path} {file_dest}")

        # insert metadata
        cursor = conn.cursor()
        cursor.execute(insert_query, (
            patient_id, file_dest, file_date, file_size, "application/pdf", file_name
        ))
        conn.commit()
        print("File uploaded and metadata saved.")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    upload_document_db(1, "patient_notes.pdf")
