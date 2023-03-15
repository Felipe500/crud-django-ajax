from .models import Client
from django.views.generic.list import ListView


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
