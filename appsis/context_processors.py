from appsis.models import Persona


def get_persons(request):

    persona = Persona.objects.all()

    return {
        'personas': persona
    }
