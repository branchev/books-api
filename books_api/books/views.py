from .serializers import BookModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookModelSerializer


class BookCRUD(APIView):
    @staticmethod
    def get_book(kwargs):
        try:
            data = Book.objects.get(id=kwargs['pk'])
            flag = False
        except KeyError:
            data = Book.objects.all()
            flag = True
        return data, flag

    def get(self, request, **kwargs):
        book, flag = self.get_book(kwargs)
        serializer = BookModelSerializer(book, many=flag)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        book, _ = self.get_book(kwargs)
        # for editing - first passed arg is the obj, seccond is the new data
        serializer = BookModelSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        book, _ = self.get_book(kwargs)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
