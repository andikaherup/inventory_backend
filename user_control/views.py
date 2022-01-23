from rest_framework.viewsets import ModelViewSet
from .serializers import CreateUserSerializer, CustomUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from datetime import datetime

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
            # use filter because it returns an empty array if no user is found
            user = CustomUser.objects.filter(
                email=valid_request.validated_data["email"]
            )
            # when there is a user in the array
            if user:
                user = user[0]
                # if the user doesnt have password
                if not user.password:
                    return Response({"userid": user.id})
                else:
                    raise Exception("User has password already")
            else:
                raise Exception("User not found")

        # authenticate the user
        user = authenticate(
            username=valid_request.validated_data["email"],
            password=valid_request.validated_data("password", None),
        )

        if not user:
            return response(
                {"error": "Invalid email or password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        access = get_access_token({"user_id", user.id},1)
        user.last_login = datetime.now()
        user.save()

        return Response({"access": access})