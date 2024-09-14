from SAPP.models import Seeds

def list_seeds():
    seeds = Seeds.objects.all()
    return seeds