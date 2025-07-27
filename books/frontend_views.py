from django.shortcuts import render, redirect
import requests

def login_view(request):
    if request.method == 'POST':
        data = {
            'username': request.POST['username'],
            'password': request.POST['password']
        }
        response = requests.post('http://127.0.0.1:8000/api/token/', data=data)
        if response.status_code == 200:
            request.session['access'] = response.json()['access']
            return redirect('books-page')
    return render(request, 'login.html')

def books_view(request):
    token = request.session.get('access')
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('http://127.0.0.1:8000/api/books/', headers=headers)
    books = response.json()
    return render(request, 'books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        token = request.session.get('access')
        headers = {'Authorization': f'Bearer {token}'}
        data = {
            'title': request.POST['title'],
            'author': request.POST['author'],
            'price': request.POST['price'],
        }
        requests.post('http://127.0.0.1:8000/api/books/', data=data, headers=headers)
    return redirect('books-page')


def delete_book_view(request, pk):
    if request.method == 'POST':
        token = request.session.get('access')
        headers = {'Authorization': f'Bearer {token}'}
        url= f'http://127.0.0.1:8000/api/books/{pk}/delete/'
        response = requests.delete(url,  headers=headers)
        return redirect('books-page')
    else:
        return redirect('books-page')

def update_book_view(request, pk):
    token = request.session.get('access')
    headers = {'Authorization': f'Bearer {token}'}
    book_url = f'http://localhost:8000/api/books/{pk}/update/'

    # GET: Load form with book data
    if request.method == 'GET':
        response = requests.get(book_url, headers=headers)
        if response.status_code == 200:
            book = response.json()
            return render(request, 'update.html', {'book': book})
        else:
            return redirect('books-page')

    # POST: Submit updated form
    if request.method == 'POST':
        data = {
            'title': request.POST['title'],
            'author': request.POST['author'],
            'price': request.POST['price'],

        }
        response = requests.put(book_url, headers=headers, data=data)
        if response.status_code in [200, 204]:
            return redirect('books-page')
        else:
            return render(request, 'update.html',
                          {'book': data, 'error': 'Failed to update book'})