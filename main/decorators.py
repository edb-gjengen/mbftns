from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

def groups_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        # Gi brukeren beskjed (muligens)
        message = "Jeg kan ikke gi deg tilgang fordi \
            du er ikke i noen av disse gruppene: {0}.".format(
                ", ".join(settings.GROUPS_ALLOWED))
        u.message_set.create(message=message)
        return False
    return user_passes_test(in_groups)
