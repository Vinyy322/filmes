from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.shortcuts import render
from filmes.forms import FilmeForm, ListFilmesForm
from filmes.models import Filme, ListFilmes

class ListaFilmesListView(ListView):
    model = ListFilmes
    context_object_name = 'listfilm'
    template_name = 'listfilme/listfilm_list.html'
    paginate_by = 8
    queryset = ListFilmes.objects.order_by('-id')

class ListarFilmesDetailView(DetailView):
    model = ListFilmes
    context_object_name = 'listfilm'
    template_name = 'listfilme/listfilm_detail.html'

class ListarFilmesCreateView(CreateView):
    model = ListFilmes
    form_class = ListFilmesForm
    template_name = 'listfilme/listfilm_form.html'
    success_url = reverse_lazy('lista_filmes_list')

class ListarFilmesUpdateView(UpdateView):
    model = ListFilmes
    fields = ['nome', 'filmes']
    template_name = 'listfilme/listfilm_form.html'
    success_url = reverse_lazy('lista_filmes_list')

class ListarFilmesDeleteView(DeleteView):
    model = ListFilmes
    template_name = 'listfilme/listfilm_confirm_delete.html'
    success_url = reverse_lazy('lista_filmes_list')



#filme
class FilmeListView(ListView):
    model = Filme
    context_object_name = 'filme'
    template_name = 'filme/filme_list.html'

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filme/filme_detail.html'

class FilmeCreateView(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filme/filme_form.html'
    
class FilmeUpdateView(UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filme/filme_form.html'
    success_url = reverse_lazy('filme_list')

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filme/filme_confirm_delete.html'
    success_url = reverse_lazy('filme_list')
