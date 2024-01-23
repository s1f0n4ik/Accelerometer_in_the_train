from django.shortcuts import render
from projects.models import Project
import pandas as pd
from plotly.offline import plot
import plotly.express as px

def index(request):
    qs = Project.objects.all()
    projects_data = [
        {
            "Project": x.name,
            "Start": x.start,
            "Finish": x.end_date,
            "Responsible": x.responcible
        } for x in qs
    ]

