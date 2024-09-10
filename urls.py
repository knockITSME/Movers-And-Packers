from django.urls import path
from . import views
urlpatterns = [
path("",views.index,name="PMHome"),
path("aboutus/",views.aboutusView,name="aboutus"),
path("contact/",views.contactView,name="contact"),
path("regform/",views.regformView,name="regform"),
path("services2/",views.servicesView1,name="services1"),
path("services1/",views.servicesView2,name="services2"),
path("loginurl/",views.loginView1,name="loginurl"),
path("signupurl/",views.signupView1,name="signupurl"),
path("getaquote/",views.getaquoteView,name="getaquote"),
path("signupForm/",views.signupForm,name="signupForm"),
path("getquoteForm/",views.getquoteForm,name="getquoteForm"),
path("viewdetails/",views.viewdetails,name="viewdetails"),
path("destroy/",views.destroy,name="destroy"),
path("handlelogin/",views.handlelogin,name="handlelogin"),
path("handlelogout/",views.handlelogout,name="handlelogout"),
]