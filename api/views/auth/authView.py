from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from api.serializers.authentication.authSerializer import TokenSerializer

class TokenView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = TokenSerializer