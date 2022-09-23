from django.contrib import admin
from django.urls import include, path,re_path

from reviews import views



urlpatterns = [

    # ex: /
    path('', views.review_list, name='review_list'),
# ex: /review/5/
    path('books/', views.book_list, name='book_list'),

    re_path(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),

    # ex: /book/


    # ex: /book/5/
    re_path(r'^book/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
    re_path(r'^book/(?P<book_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),

    # ex: /review/user - get reviews for the logged user
    re_path(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    re_path(r'^review/user/$', views.user_review_list, name='user_review_list'),

]
