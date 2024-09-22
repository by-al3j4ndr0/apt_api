from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TransferSerializers
from .models import Transfer
from django_pandas.io import read_frame
import pandas as pd

class QueryView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        hbl = request.query_params["hbl"]

        data = Transfer.objects.all()        # Perform database query
        df = read_frame(data)            # Transform queryset into pandas dataframe0

        query = df[df["hbl"] == hbl]

        return Response(query)              # Return the result in JSON via Django REST Framework

class ConfirmWarehouse(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        hbl = request.query_params["hbl"]

        update = Transfer.objects.filter(hbl=hbl).update(warehouse=True)

        response_message = {
            'status' : 'Dome'
        }
        
        return Response(response_message)              # Return the result in JSON via Django REST Framework

class FileUploadView(APIView):

    def put(self, request, format=None):
        file_obj = request.data['file']

        data = pd.read_csv(file_obj)
        
        transfer_df = pd.DataFrame(data)

        # Convert the DataFrame to Django Model instances and save them
        for index, row in transfer_df.iterrows():
            Transfer.objects.create(
                hbl=row['hbl'],
                name=row['name'],
                city=row['city'],
                state=row['state'],
        )
        return Response(status=204)