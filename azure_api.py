import requests

def fetch_sign_in_logs(creds, start_date, end_date, top=None):
    token = get_access_token(creds)
    headers = {"Authorization": f"Bearer {token}"}

    start_date_str = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_date_str = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    url = "https://graph.microsoft.com/v1.0/auditLogs/signIns"
    params = {
        "$filter": f"createdDateTime ge {start_date_str} and createdDateTime le {end_date_str}"
    }
    if top:
        params["$top"] = top

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")
    return response.json()

def get_access_token(creds):
    token_url = f"https://login.microsoftonline.com/{creds['tenant_id']}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": creds["client_id"],
        "client_secret": creds["client_secret"],
        "scope": "https://graph.microsoft.com/.default"
    }

    response = requests.post(token_url, data=data)

    if response.status_code != 200:
        raise Exception(f"Token Error: {response.status_code} - {response.text}")
    return response.json()["access_token"]

