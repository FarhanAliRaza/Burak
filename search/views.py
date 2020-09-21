from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product, Category

class SearchProductView(ListView):
    template_name = "search/searchresult.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        if query is not None:
            print(Product.objects.search(query))
            return Product.objects.search(query)
        return Product.objects.featured()
def search(request):
    cat_list=Category.objects.all()
    context={
        "cat_list":cat_list,
    }
    template_name = "search/search.html"
    return render(request, template_name, context)