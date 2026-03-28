from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add_patent,name='add_patient'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete')
    

]