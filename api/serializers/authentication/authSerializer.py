from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(TokenSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token