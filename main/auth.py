from django.conf import settings
from django.contrib import messages

def in_groups(request):
    if request.user.is_authenticated():
        #settings.GROUPS_ALLOWED
        if bool(request.user.groups.filter(name__in=settings.GROUPS_ALLOWED)) or request.user.is_superuser:
            return True
        # Gi brukeren beskjed (muligens)
        message = "Jeg kan ikke gi deg tilgang fordi \
            du er ikke i noen av disse gruppene: {0}.".format(
                ", ".join(settings.GROUPS_ALLOWED))
        messages.info(request, message=message)
    return False
