from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name='blog'),
 
    path("<int:pk>/", views.PostDetailView.as_view(), name='post'),

    path("<int:pk>/comment/", views.add_comment, name='add_comment'),

    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    path('search/', views.search, name='search' ),

    path('create', views.create, name='create'),

    path('manage/', views.manage_posts, name='manage'),

    path('search2/', views.search_manage, name='search2' ),

    path("post/<int:pk>/", views.delete_post, name='delete')
]

