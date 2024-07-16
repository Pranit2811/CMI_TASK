from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import welcome
from .views import MyChunkedUploadView, MyChunkedUploadCompleteView,ChunkedUploadDemo,QueryBuilderPanelView,UserListView,UserCreateView,UserDeleteView

urlpatterns = [
    path('welcome/', welcome, name='welcome'), 
    path('', ChunkedUploadDemo.as_view(), name='chunked_upload'),
    path('api/chunked_upload_complete/', MyChunkedUploadCompleteView.as_view(), name='api_chunked_upload_complete'),
    path('api/chunked_upload/', MyChunkedUploadView.as_view(), name='api_chunked_upload'),
    path('query-builder/', QueryBuilderPanelView.as_view(), name='query_builder_panel'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='add_user'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
]
