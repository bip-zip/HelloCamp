from django.shortcuts import render
from django.views.generic import TemplateView


from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Camp


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['camps'] = Camp.objects.all()  # Retrieve all camp data
        return context
    
    
        query = request.GET.get('query')
        
        if query:
            # Call the search function or scrape function here
            # search_results = search_summer_camps(query)  # Replace with your actual function
            

            # Filter camps based on the query
            search_results = Camp.objects.filter(
                name__icontains=query  # You can modify this to search other fields as needed
            )
            return render(request, 'search.html', {
                'query': query,  # Pass the search term back to the template
                'camps': search_results,
            })
        else:
            return render(request, self.template_name, {
                'error': 'Please enter a keyword to search.',
            })
        
        
def search(request):
    query = request.GET.get('query')
    search_results = Camp.objects.filter(name__icontains=query)
    return render(request, 'search.html', {
            'query': query,
            'camps': search_results,
        })
  
   


