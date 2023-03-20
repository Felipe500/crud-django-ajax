from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView
from django.views import View
from .models import Client
from .forms import ClientReadOnlyForm, ClientForm


class ViewClient(View):
    def get(self, request, id):
        cliente = Client.objects.get_queryset().get(id=id)
        form = ClientReadOnlyForm(instance=cliente)
        return render(request, 'views_ajax/form_client.html', {'form': form})


class ViewCreateClient(View):
    def get(self, request):
        form = ClientForm()
        return render(request, 'views_ajax/form_client.html', {
            'form': form,
            'id_client': 0,
            'name_client': 'Cliente Novo'
        })


class ViewUpdateClient(View):
    def get(self, request, id):
        cliente = Client.objects.get_queryset().get(id=id)
        form = ClientForm(instance=cliente)
        return render(request, 'views_ajax/form_client.html', {
            'form': form,
            'id_client': cliente.id,
            'name_client': cliente.full_name
        })


class ViewDeleteClient(View):
    def get(self, request, id):
        cliente = Client.objects.get_queryset().get(id=id)
        form = ClientReadOnlyForm(instance=cliente)
        return render(request, 'views_ajax/client_delete.html', {
            'form': form,
            'id_client': cliente.id,
            'name_client': cliente.full_name,
        })


class CreateClient(View):
    def post(self,  *args, **kwargs):
        form = ClientForm(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'created': 'True'})
        return render(self.request, 'views_ajax/form_client.html', {
            'form': form,
            'id_client': 0,
            'name_client': 'novo cliente',
        })


class UpdateClient(View):
    def post(self,  *args, **kwargs):
        cliente = Client.objects.get_queryset().get(id=kwargs['id'])
        form = ClientForm(self.request.POST or None, self.request.FILES or None, instance=cliente)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'updated': 'True'})
        return render(self.request, 'views_ajax/form_client.html', {
            'form': form,
            'id_client': cliente.id,
            'name_client': cliente.full_name
        })


class DeleteClient(View):
    def post(self,  *args, **kwargs):
        Client.objects.get_queryset().get(id=kwargs['id']).delete()
        return JsonResponse({'deleted': True})


class ClientListAjax(ListView):
    paginate_by = 2
    model = Client.objects.actives()
    fields = '__all__'
    template_name = 'views_ajax/get_list_clients.html'
    form_filter = None

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            try:
                return self.model.filter(
                    Q(name__unaccent__icontains=query) | Q(surname__unaccent__icontains=query)
                )
            except:
                return self.model.filter(
                    Q(name__icontains=query) | Q(surname__icontains=query)
                )
        return self.model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['clientes'] = paginator.page(page)
        return context
