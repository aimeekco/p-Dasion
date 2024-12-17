import requests

def get_access_token():
    """
    Function to obtain the access token using client credentials.
    """
    token_url = "https://your-openemr-server/apis/default/token"
    client_id = "your_client_id"
    client_secret = "your_client_secret"

    response = requests.post(token_url, data={
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    })
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Failed to get token: {response.text}")

if __name__ == "__main__":
    token = get_access_token()
    print("Access Token:", token)
