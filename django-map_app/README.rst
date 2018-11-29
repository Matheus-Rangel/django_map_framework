=====
Map_app
=====

Map_app é uma aplicação django para armazenamento e mapeamento dos
gastos de uma prefeitura.

Quick start
-----------

1. Dependencias: 
    django-rest-framework: https://www.django-rest-framework.org/
    django-filter: pip install django-filter
    django-widget-tweaks: https://pypi.org/project/django-widget-tweaks/
    
2. Adicione "map_app" na sua configuração INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        'map_app',
    ]

3. É necessario o django admin para cadastrar ou modificar as despesas.

4. Inclua as URLconf do map_app no seu projeto urls.py com o prefixo que desejar::

    path('', include('map_app.urls')),
    ou
    path('prefixo/', include('map_app.urls'))

5. Execute `python manage.py migrate` para migrar os modelos do map_app para o banco de dados.

6. implemente o atualiza_app, reclama_app, info_app. De acordo com a prefeitura.
    
    atualiza_app será responsavel por atualizar os dados da prefeitura no banco de dados
    automaticamente se possivel.

    reclama_app será responsavel por gerar ou redirecionar o usuario para uma pagina de reclamação
    da prefeitura

    info_app será responsavel por exibir as informações gerais do gasto prefeitura, como: 
        - O gasto total.
        - O gasto por instituicão.
        - O gasto por orgão.
        - O gasto por elemento.
        ...

7. visite http://127.0.0.1:8000/prefixo/ para visualizar o mapa.
   visite http://127.0.0.1:8000/prefixo/api para visualizar as opcoes da api.
   