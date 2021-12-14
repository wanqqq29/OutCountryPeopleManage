from django.urls import path, include
from outpeopleCheckin import views

urlpatterns=[
    path(r'',views.index,name="index"),
    path('success/',views.success,name="success"),
    path('n404/',views.notfound,name="notfound"),
    #提交教师信息
    path('Tinfo/add/',views.Tinfo_Createview.as_view(),name="Tinfo_add"),
    # path('Tinfo/query', views.Tinfo_query.as_view(), name="Tinfo_query"),
    # path('Tinfo/query/', views.Tinfo_query, name="Tinfo_query"),
    path('Tinfo/detail/<int:pk>/',views.DeatilView.as_view(),name="Tdetail"),
    path('Tinfo/edit/<int:pk>/', views.Tinfo_editview.as_view(), name="Tinfo_editview"),

    #学生信息
    path('Sinfo/add/',views.Sinfo_Createview.as_view(),name="Sinfo_add"),
    # path('Tinfo/query', views.Tinfo_query.as_view(), name="Tinfo_query"),
    # path('Tinfo/query/', views.Tinfo_query, name="Tinfo_query"),
    path('Sinfo/detail/<int:pk>/',views.SDeatilView.as_view(),name="Sdetail"),
    path('Sinfo/edit/<int:pk>/', views.Sinfo_editview.as_view(), name="Sinfo_editview"),


    #出国信息
    path('out/Tadd/',views.Cinfo_Createview.as_view(),name="TCinfo_add"),
    path('out/Sadd/', views.SCinfo_Createview.as_view(), name="SCinfo_add"),
    path('out/query/', views.Cinfo_query, name="Cinfo_query"),
    # path('Tinfo/query/', views.Tinfo_query, name="Tinfo_query"),
    # path('out/detail/<int:pk>/',views.SDeatilView.as_view(),name="Sdetail"),
    path('out/Tedit/<int:pk>/', views.Cinfo_editview.as_view(), name="Tout_editview"),
    path('out/Sedit/<int:pk>/', views.SCinfo_editview.as_view(), name="Sout_editview"),

]