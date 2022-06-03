from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("contact_page/",views.Contact_page, name = 'Contact'),
    path("contact_page/Querrysubmit/", views.Querrysubmit, name = 'submit'),
    
    path("order/",views.order, name = 'order'),
    path("repairing/",views.repairing, name = 'repairing'),
    path("mortgage/",views.mortgage, name = 'mortgage'),

    path('logout/',views.logoutUser, name="logout"),
    path('login/',views.login, name="login"),
    path('createnewaccount/',views.CreateNewAccount, name="CreateNewAccount"),

    path('login/logincheck/',views.logincheck, name="login"),

    path('tracker/',views.tracker, name="tracker"),
    path("productview/",views.productview, name = "productview"),
    path("checkout/",views.checkout, name = "checkout"),

]
