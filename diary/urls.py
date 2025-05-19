from django.contrib import admin
from django.urls import path
from diary.views import home,getAllEntries,AddEntry,getIndividualEntry
urlpatterns = [
    path('',home),
    path('view-entries',getAllEntries),
    path('add-new-entry',AddEntry),
    path('<int:id>/',getIndividualEntry),
    path('<str:id>/',getIndividualEntry),
]