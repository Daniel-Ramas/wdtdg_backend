from rest_framework import status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from wdtdg_backend.users.models import User

from .serializers import UserSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000/accounts/google/login/callback/"
    client_class = OAuth2Client


@api_view(["POST"])
@permission_classes([AllowAny])
def google_auth_callback(request):
    """
    Handle the OAuth2 callback from Google
    """
    try:
        # Get the authorization code from the request
        code = request.data.get("code")
        if not code:
            return Response(
                {"error": "Authorization code is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create a social login view instance
        view = GoogleLoginView.as_view()

        # Process the callback
        response = view(request._request)

        if response.status_code == 200:
            # Get the user from the response
            user = response.data.get("user")

            # Create or get token
            token, _ = Token.objects.get_or_create(user=user)

            return Response(
                {"token": token.key, "user": {"email": user.email, "name": user.name}}
            )

        return Response(
            {"error": "Authentication failed"}, status=status.HTTP_400_BAD_REQUEST
        )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
