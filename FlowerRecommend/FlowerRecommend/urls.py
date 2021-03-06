"""FlowerRecommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from map import views as map_view
from home import views as home_view
from order import views as order_view
from recommend import views as recommend_view
from register import views as register_view
from review import views as review_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map_view.main, name="main"),
    path('recom-flower/recom-store/', map_view.map, name="recom-store"),
    path('notice/', home_view.home, name="notice"),
    path('order/', order_view.order, name="order"),
    path('recom-flower/', recommend_view.recom, name="recom"),
    path('login/', register_view.login_view, name="login"),
    path('join/', register_view.join_view, name="join"),
    path('review/', review_view.review, name="review"),
    path('logout/', register_view.logout_view, name="logout"),
]
