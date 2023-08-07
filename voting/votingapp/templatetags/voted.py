from django import template
from votingapp.models import Vote,Voteuser
register = template.Library()

@register.filter(name='votefilter')
def votefilter(questionid,currentuser):
    b=Vote.objects.filter(id__in=[questionid],user=currentuser).count()
    if b > 0:
    
        return True
    return False
    
