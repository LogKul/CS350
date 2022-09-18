from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tasks.models import *
from tasks.serializers import *
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def author(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            author = authors.filter(name_icontains=name)
        authors_serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(authors_serializer.data, safe=False)

    elif request.method == 'POST':
        author_data = JSONParser().parse(request)
        author_serializer = AuthorSerializer(data=author_data)
        if author_serializer.is_valid():
            author_serializer.save()
            return JsonResponse(author_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Author.objects.all().delete()
        return JsonResponse({'message': '{} Authors were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def book(request):
    if request.method == 'GET':
        books = Book.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            book = books.filter(name_icontains=name)
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)

    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Book.objects.all().delete()
        return JsonResponse({'message': '{} Books were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def author_books(request):

    # Example: [http://localhost:8000/authorbooks?author_id=3], no body
    if request.method == 'GET':
        books = Book.objects.all()

        author_id = request.GET.get('author_id', None)
        if author_id is not None:
            books = books.filter(author=author_id)

            books_serializer = BookSerializer(books, many=True)
            return JsonResponse(books_serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'Missing author_id field.'}, status=status.HTTP_204_NO_CONTENT)
        # 'safe=False' for objects serialization

    elif request.method == 'DELETE':
        books = Book.objects.all()

        author_id = request.GET.get('author_id', None)
        if author_id is not None:
            books = books.filter(author=author_id)
            count = books.delete()
            return JsonResponse({'message': '{} Books were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': 'Missing author_id field.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def single_author(request, pk):

    # Example: [http://localhost:8000/authorbooks/3], no body
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return JsonResponse({'message': 'The author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        authors_serializer = AuthorSerializer(author)
        return JsonResponse(authors_serializer.data)

    elif request.method == 'DELETE':
        author.delete()
        return JsonResponse({'message': 'Author was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


'''
@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials

    # Alternate GET that searches for conditional entries rather than all entries
    """ if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization """

    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try:
        tutorial = Tutorial.objects.get(pk=pk)

        if request.method == 'GET':
            tutorial_serializer = TutorialSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)
        elif request.method == 'PUT':
            tutorial_data = JSONParser().parse(request)
            tutorial_serializer = TutorialSerializer(
                tutorial, data=tutorial_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            tutorial.delete()
            return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET / PUT / DELETE tutorial


@api_view(['GET'])
def tutorial_list_published(request):
    # GET all published tutorials
    tutorials = Tutorial.objects.filter(published=True)

    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
'''
