from django.contrib import admin
from django.urls import path, include
from feeds import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("feeds/", include("feeds.urls"))
    # path('feeds/', views.show_feed),
    # path('feeds/all', views.all_feed),
    # path('feeds/<int:feed_id>/<str:feed_content>', views.one_feed)
]
