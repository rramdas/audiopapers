from django.urls import path
from . import views
from .views import PaperListView

app_name = 'pdfparser'

urlpatterns = [
    # papers views
    # path('', views.paper_list, name='paper_list'),
    path('', PaperListView.as_view(), name='paper_list'),
    path('create/', views.create_paper, name='create_paper'),

    path('paper/<uuid:paper_id>/', views.paper_detail, name='paper_detail'),
    path('download/<uuid:paper_id>/', views.download, name='download')
]