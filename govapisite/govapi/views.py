from django.shortcuts import render
from tablib import Dataset
from .serializers import GovernorSerializer
from .models import Governor
from rest_framework import viewsets

# Create your views here.

class GovernorViewSet(viewsets.ModelViewSet):
    queryset = Governor.objects.all().order_by('state')
    serializer_class = GovernorSerializer


def simple_upload(request):
    if request.method == 'POST':
        governor_resource = GovernorResource()
        dataset = Dataset()
        new_governors = request.FILES['myfile']

        imported_data = dataset.load(new_governors.read())
        result = governor_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            governor_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')
