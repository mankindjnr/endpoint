from django.shortcuts import render
from django.http import JsonResponse
import datetime
import requests
import json

def index(request):
    # utc time
    now_ = datetime.datetime.utcnow()
    utc_time = now_.isoformat() + "Z"

    #current day
    current_date = datetime.date.today()
    day_of_week = current_date.weekday()
    day_name = current_date.strftime("%A")

    # status code
    url = "https://github.com/mankindjnr"
    response = requests.get(url)
    status_code = response.status_code

    #parameters
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # github urls
    file_url = "https://github.com/mankindjnr/hngx/blob/main/endpoint/stageone/views.py"
    full_source_code = "https://github.com/mankindjnr/hngx"

    one_stage = {
        "slack_name":slack_name,
        "current_day":day_name,
        "track":track,
        "github_file_url":file_url,
        "github_repo_url":full_source_code,
        "status_code": status_code
    }

    return JsonResponse(one_stage)