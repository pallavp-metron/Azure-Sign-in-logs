# Azure Sign-In Logs CLI

## Overview
This project provides a Python-based CLI tool to fetch Azure Sign-In Logs for a specified date range using the Microsoft Graph API. The logs are retrieved and processed based on user input, such as credentials and date offset.

## Setup
1. Install dependencies:
pip install -r requirements.txt

2. Create a creds.json file with Azure credentials:
{
    "tenant_id": "your-tenant-id",
    "client_id": "your-client-id",
    "client_secret": "your-client-secret"
}

# Example usage of the CLI.
python azure_logs_cli.py --azure_creds creds.json --date_offset <NUMBER_OF_DAYS>