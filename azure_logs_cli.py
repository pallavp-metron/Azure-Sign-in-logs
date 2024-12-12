import click
import json
from datetime import datetime, timedelta, timezone
from azure_api import fetch_sign_in_logs

@click.command()
@click.option('--azure_creds', required=True, type=click.Path(exists=True))
@click.option('--date_offset', required=True, type=int)
@click.option('--top', default=None, type=int)
def main(azure_creds, date_offset, top):
    try:
        with open(azure_creds, 'r') as f:
            creds = json.load(f)

        end_date = datetime.now(timezone.utc)
        start_date = end_date - timedelta(days=date_offset)

        logs = fetch_sign_in_logs(creds, start_date, end_date, top)

        click.echo(json.dumps(logs, indent=4))
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

if __name__ == "__main__":
    main()
