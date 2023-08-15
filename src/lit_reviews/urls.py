"""
URL configuration for lit_reviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# from django.conf import settings

from .settings import MEDIA_URL, MEDIA_ROOT, DEBUG
from .views import (
    index,
    signup,
    homepage,
    subscriptions,
    follow_new_user,
    unfollow_user,
    posts,
    logout_view,
)

urlpatterns = [
    path("", index, name="index"),
    path("signup", signup, name="signup"),
    path("home/", homepage, name="homepage"),
    path("subscriptions/", subscriptions, name="subscriptions"),
    path("new-subcription/", follow_new_user, name="new-subscription"),
    path("unfollow/<str:subs_username>", unfollow_user, name="unfollow"),
    path("posts/", posts, name="posts"),
    path("tickets/", include("tickets_app.urls")),
    path("reviews/", include("reviews_app.urls")),
    path("logout/", logout_view, name="logout"),
    path("admin/", admin.site.urls),
]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
