from .models import Client
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.views import View
from .forms import ClientReadOnlyForm, ClientForm


class CreateClient(View):
    form_class = ClientForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'views_ajax/form_client.html', {'form': form,
                                                               'id_client': 0,
                                                               'name_client': 'Cliente Novo'})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            form.save()
            return JsonResponse({'created': 'True'})
        return render(self.request, 'views_ajax/form_client.html', {
            'form': form,
            'id_client': 0,
            'name_client': 'novo cliente',
        })


class ChangeClient(View):
    form_class = ClientForm

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        cliente = Client.objects.get(pk=pk)
        form = self.form_class(instance=cliente)
        return render(request, 'views_ajax/form_client.html', {
            'form': form,
            'id_client': cliente.id,
            'name_client': cliente.full_name,
            'pk': pk})

    def post(self, request, *args, **kwargs):
        cliente = Client.objects.get(pk=kwargs.get('id'))
        form = self.form_class(request.POST or None, instance=cliente)
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
    form_class = ClientForm

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        cliente = Client.objects.get(pk=pk)
        form = ClientReadOnlyForm(instance=cliente)
        return render(request, 'views_ajax/client_delete.html', {
            'form': form,
            'id_client': cliente.id,
            'name_client': cliente.full_name,
        })

    def post(self, request, *args, **kwargs):
        Client.objects.get_queryset().get(id=kwargs['id']).delete()
        return JsonResponse({'deleted': True})


class ClientList(ListView):
    paginate_by = 2
    model = Client.objects.actives()
    fields = '__all__'
    template_name = 'client.html'
    form_filter = None

    def get_queryset(self):
        return self.model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['clientes'] = paginator.page(page)
        return context
