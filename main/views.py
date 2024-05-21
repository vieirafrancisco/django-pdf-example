from datetime import timezone

from django.views.generic import TemplateView

from django_weasyprint import WeasyTemplateResponseMixin


class MyDetailView(TemplateView):
    template_name = 'my_detail.html'


class DownloadView(WeasyTemplateResponseMixin, MyDetailView):
    # suggested filename (is required for attachment/download!)
    pdf_filename = 'foo.pdf'
    # set PDF variant to 'pdf/ua-1' (see weasyprint.DEFAULT_OPTIONS)
    pdf_options = {'pdf_variant': 'pdf/ua-1'}


class DynamicNameView(WeasyTemplateResponseMixin, MyDetailView):
    # dynamically generate filename
    def get_pdf_filename(self):
        return 'foo-{at}.pdf'.format(
            at=timezone.now().strftime('%Y%m%d-%H%M'),
        )
