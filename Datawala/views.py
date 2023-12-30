import json
import pandas as pd

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from StoreData.serializers import PrimarySerializer
from StoreData.models import PrimaryData


def home_page(request):
    print("home page requested ")
    friends=["rishabh","paras","deepak"]
    return JsonResponse(friends, safe=False)

class FetchData(APIView):

    queryset = PrimaryData.objects.all()
    serializer_class = PrimarySerializer

    def get(self, request, pk=None):
        try:
            df = pd.DataFrame(PrimaryData.objects.values()).to_json(orient='records')
            #Pri_serializer = PrimarySerializer(df, many=True, context={'request': request})
            return JsonResponse(json.loads(df), safe = False)
        except Exception as e:
            print(e)
            return JsonResponse(e, safe=False)



    def post(self, request):
        try:
            form = json.loads(request.body)
            print(form)
            df1 = pd.read_excel('StoreData/excel.xlsx')
            print(df1)
            df1 = df1.fillna('NA')
            df2 = df1.to_dict('records')
            #df1 = df2.fillna('NA')
            modelInstances = list(map(lambda x: PrimaryData(**x), df2))
            PrimaryData.objects.bulk_create(modelInstances)
            data = PrimaryData.objects.all()
            print(data)
            resp = {"status": "pass"}
        except Exception as e:
            print("Error", e)
            resp = {"status": "fail"}
        return JsonResponse(resp, safe=False)
