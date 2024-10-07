from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from setup import settings
from filmes.views import ListaFilmesListView, ListarFilmesCreateView, ListarFilmesDeleteView, ListarFilmesDetailView, ListarFilmesUpdateView, FilmeCreateView, FilmeDeleteView, FilmeDetailView, FilmeUpdateView, FilmeListView

urlpatterns = [
    path('', ListaFilmesListView.as_view(), name='lista_filmes_list'),
    path('create/', ListarFilmesCreateView.as_view(), name='lista_filmes_create'),
    path('<int:pk>/', ListarFilmesDetailView.as_view(), name='lista_filmes_detail'),
    path('<int:pk>/edit/', ListarFilmesUpdateView.as_view(), name='lista_filmes_update'),
    path('<int:pk>/delete/', ListarFilmesDeleteView.as_view(), name='lista_filmes_delete'),

    path('filmes/', FilmeListView.as_view(), name='filme_list'),
    path('filmes/create/', FilmeCreateView.as_view(), name='filme_create'),
    path('filmes/<int:pk>/', FilmeDetailView.as_view(), name='filme_detail'),
    path('filmes/<int:pk>/edit/', FilmeUpdateView.as_view(), name='filme_update'),
    path('filmes/<int:pk>/delete/', FilmeDeleteView.as_view(), name='filme_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
