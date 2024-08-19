from django.shortcuts import render
from django.http import JsonResponse
from client.models import Complaint


# Create your views here.
def index(request):
    return render(request, 'employee/index.html')


def get_complaint(request):
    # Optionally, you can filter the complaints based on a timestamp or other criteria
    complaints = Complaint.objects.all().values('complaint_id', 'client_pnr', 'client_name', 'complaint_time', 'department')
    return JsonResponse(list(complaints), safe=False)