import traceback
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleEndPoint(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        try:
            data = {'message': 'OK'}
            return Response(data=data, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            return Response(data={"message": "Fail"}, status=status.HTTP_404_NOT_FOUND)
