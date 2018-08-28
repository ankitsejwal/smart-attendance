import os, json
import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_members(app):
    file_path = os.path.join(app.static_folder, 'js/members.json')
    file = open(file_path, "r")
    members = json.load(file)
    return members

def connection():
    # use creds to create a client to interact with the Google Drive API
    scope   = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds   = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client  = gspread.authorize(creds)
    return client.open('attendance-2018').sheet1


def mark_present(row, index):
    sheet = connection()
    sheet.insert_row(row, index)
