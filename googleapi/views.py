# This file is made by Satyam

from django.shortcuts import render

import pickle
import os.path
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from django.http import HttpResponse


SCOPES = ['https://www.googleapis.com/auth/drive']

def index(request):
    return HttpResponse('Hell satyam this is your first website using django')

def show(request):
    folder_ids= {}
    Images_link=[]
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    # children = build('drive','v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=12, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(item['name'],item['id'])
            folder_ids[item['id']]=item['id']   
            if(item['name']=='Google'):

                children =  service.files().list(
                    q="'"+item['id']+"' in parents",fields='nextPageToken, files(id,name)').execute()
                
                childFiles = children['files']
                for child in childFiles:
                    print(child)
                    Images_link.append('https://drive.google.com/uc?export=view&id={}'.format(child['id']))
                # return HttpResponse(Images_link)
    return render(request, 'myPage.html', {"links": Images_link}) # passing the total urls of images to render on html.


                

    # return HttpResponse('hey this is your show function\n OOh! you successfully made the api endpoints using django')