from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
import json
import requests

@api_view(['POST'])
@permission_classes([AllowAny])
def captcha(request):

    key = "6LdOFPMUAAAAAB2TY0ToGgrSi1j5A73SsRZcnvuO"

    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    token = body_data.get("captcha")
    
    data = {
        'secret':key,
        'response':token
    }
    url = "https://www.google.com/recaptcha/api/siteverify"
    
    req = requests.post(url, data=data)

    
    return Response(req.json(), status=status.HTTP_200_OK)