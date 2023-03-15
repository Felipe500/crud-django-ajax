# CRUD DJANGO + JQUERY (AJAX)
Então a sigla CRUD é um acrônimo, de quatro operações básicas, são elas:

C: Create – Criar um novo registro. 
R: Read – Ler um registro, ou uma lista de registros.
U: Update – Atualizar um registro.
D: Delete – Excluir um registro.

Atenção:
É requisitado que o banco de dados Postgres possua a extenção unaccent para poder realizar a busca
de palavras com acento e caracteres especiais, segue o link:
https://ohmycode.com.br/melhorando-as-pesquisas-de-texto-com-django-e-postgres/

caso não tenha conseguido instalar "extenção unaccent" no seu banco de dados, altere em:
app/client/view_ajax.py - ClientListAjax

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return self.model.filter(
                Q(name__icontains=query) | Q(surname__icontains=query)
            )
        return self.model
