from django.urls import path

from COS_API import views

urlpatterns = [

    path('College/search/<str:search>/', views.CollegeList.as_view()),
    path('College/', views.CollegeList.as_view()),
    path('College/<int:pk>/', views.CollegeUpdate.as_view()),



    path('Course/', views.CourseCtl.as_view()),
    path('Course/<int:pk>', views.CourseCtl.as_view()),
    path('Course/search/<str:search>/', views.CourseCtl.as_view()),




    path('Student/', views.StudentView.as_view()),
    path('Student/<int:pk>', views.StudentView.as_view()),



    path('Subject/', views.SubjectView.as_view()),
    path('Subject/<int:pk>', views.SubjectView.as_view())
   ]
