# api/zoho_integration.py
import requests
from decouple import config

class ZohoIntegration:
    def __init__(self):
        self.api_key = config('ZOHO_API_KEY')
        self.refresh_token = config('ZOHO_REFRESH_TOKEN')
        self.client_id = config('ZOHO_CLIENT_ID')
        self.client_secret = config('ZOHO_CLIENT_SECRET')
        self.access_token = None
    
    def get_access_token(self):
        """Obtener access token usando refresh token"""
        url = "https://accounts.zoho.com/oauth/v2/token"
        data = {
            'refresh_token': self.refresh_token,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'refresh_token'
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            return self.access_token
        return None
    
    def create_lead(self, contact_data):
        """Crear lead en Zoho CRM"""
        if not self.access_token:
            self.get_access_token()
        
        url = "https://www.zohoapis.com/crm/v2/Leads"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.access_token}',
            'Content-Type': 'application/json'
        }
        
        zoho_data = {
            "data": [{
                "Company": contact_data['company'],
                "Last_Name": contact_data['full_name'].split()[-1],
                "First_Name": contact_data['full_name'].split()[0] if len(contact_data['full_name'].split()) > 1 else '',
                "Email": contact_data['email'],
                "Phone": contact_data.get('phone', ''),
                "Description": contact_data['message'],
                "Lead_Source": "Website"
            }]
        }
        
        response = requests.post(url, json=zoho_data, headers=headers)
        if response.status_code == 201:
            return response.json()['data'][0]['details']['id']
        return None
    
    def create_calendar_event(self, event_data):
        """Crear evento en Zoho Calendar"""
        # Similar implementation
        pass