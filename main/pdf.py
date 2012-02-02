#coding: utf-8

# Ref:
#  - http://stackoverflow.com/questions/1377446/html-to-pdf-for-a-django-site
#  - http://stackoverflow.com/questions/2179958/django-pisa-adding-images-to-pdf-output ?

import uuid
import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def unique_filename():
    return uuid.uuid4()
