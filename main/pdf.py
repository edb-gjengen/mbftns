#coding: utf-8

# Ref:
#  - http://stackoverflow.com/questions/1377446/html-to-pdf-for-a-django-site
#  - http://stackoverflow.com/questions/2179958/django-pisa-adding-images-to-pdf-output ?
#  - http://web.archive.org/web/20090413054650/http://www.xhtml2pdf.com/doc/pisa-en.html
import os

from cgi import escape
from django.template.loader import render_to_string
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse
import cStringIO as StringIO
import ho.pisa as pisa

def render_to_pdf(template_src, context_dict, context_instance):
    html  = render_to_string(template_src, context_dict, context_instance=context_instance)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(
            StringIO.StringIO(html.encode("UTF-8")),
            dest=result,
            link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def fetch_resources(uri, rel):
    # Replace the url with the physical path.
    path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    return path
