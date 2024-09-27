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

        query_serie = df.loc[df["hbl"] == hbl]
        query_df = query_serie.to_dict(orient='list')

        serializers = TransferSerializers(query_df)

        return Response(serializers.data)              # Return the result in JSON via Django REST Framework

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
        additional_cols = ['warehouse']

        data = pd.read_csv(file_obj)
        
        df = pd.DataFrame(data)

        # Convert the DataFrame to Django Model instances and save them
        for index, row in df.iterrows():
            Transfer.objects.create(
                hbl=row['hbl'],
                name=row['name'],
                city=row['city'],
                state=row['state'],
                warehouse=row['warehouse']
        )
        return Response(status=204)
    
class CheckWarehouse(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = Transfer.objects.all()
        df = read_frame(data)
        false_df = pd.DataFrame(columns=('hbl', 'name', 'city', 'state', 'warehouse'))

        query = df.loc[df["warehouse"] == "False"] 
        html_df = pd.concat([false_df, query])

        # Convert the DataFrame to an HTML table
        html_table = html_df.to_html(columns=('hbl', 'name', 'city', 'state', 'warehouse'), index=False)

        return render(request, 'display_table.html', {'html_table': html_table})