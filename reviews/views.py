from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review, Book
from django.contrib.auth.models import User
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
import datetime




def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def book_list(request):
    book_list = Book.objects.order_by('-name')
    context = {'book_list':book_list}
    return render(request, 'reviews/book_list.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm()
    return render(request, 'reviews/book_detail.html', {'book': book, 'form': form})

# @login_required_message(message = "You should be logged in, in order to add comment")
@login_required(login_url='/register/login')
def add_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        # user_name = form.cleaned_data['username']
        # user_name = request.user.username
        review = Review()
        review.book = book
        review.user_name = User.objects.get(username=request.user.username)
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()

        return HttpResponseRedirect(reverse('reviews:book_detail', args=(book.id,)))

    return render(request, 'reviews/book_detail.html', {'book': book, 'form': form})

def user_review_list(request, username=None):
    username = User.objects.get(username=request.user.username)
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'reviews/user_review_list.html', context)
