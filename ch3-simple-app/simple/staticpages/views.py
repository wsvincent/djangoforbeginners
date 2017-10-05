from django.views.generic import TemplateView


class Home_page_view(TemplateView):
	template_name = 'staticpages/index.html'


class About_page_view(TemplateView):
	  template_name = 'staticpages/about.html'
