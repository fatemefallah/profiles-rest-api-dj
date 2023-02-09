from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class Hello(APIView):
    """first api view"""

    def get(self, requset, format=None):
        """Rerutns a list"""
        apiview = ["test1", "test2", "test3"]

        return Response({"message": "hello", "apiview": apiview})
