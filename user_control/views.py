from rest_framework.viewsets import ModelViewSet
from .serializers import CreateUserSerializer, CustomUser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CreateUserView(ModelViewSet):
    http_method_names = ["post"]
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer()

    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        CustomUser.objects.create(**valid_request.validated_data)

        return Response(
            {"success": "User created successfully"}, status=status.HTTP_201_CREATED
        )


# class for login handling
class LoginView(ModelViewSet):
    http_method_names = ["post"]
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer()

    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        new_user = valid_request.validated_data["is_new_user"]

        if new_user:
            user = CustomUser.objects.filter(
                email=valid_request.validated_data["email"]
            )
            
            if user:
                user = user[0]
                if not user.password:
                    return Response({"userid": user.id})
                else:
                    raise Exception("User has password already")
