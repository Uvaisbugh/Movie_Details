from django.urls import path, include

from Movie_App import views
app_name = 'movieapp'
urlpatterns = [
    path('',views.index,name="index"),
    path('movie/<int:MID>',views.details,name="details"),
    path('add/',views.add,name='add'),
    path('update/<int:Id>',views.update,name='update'),
    path('delete/<int:Id>',views.delete,name='delete')
]
