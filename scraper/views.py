from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .utils import dynamic_scraper_function


class DynamicScraperView(View):
    template_name = 'scrape.html'

    def get(self, request):
        """
        Handle GET requests by rendering the scraper form template.
        """
        return render(request, self.template_name)

    def post(self, request):
        """
        Handle POST requests to process the scraping logic.
        """
        target_url = request.POST.get('url')
        if not target_url:
            return JsonResponse({'status': 'error', 'message': 'URL is required'})

        # Use the reusable scraper function
        result = dynamic_scraper_function(target_url)
        return JsonResponse(result)
