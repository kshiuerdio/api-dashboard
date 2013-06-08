from django.http import HttpResponse
from django.template import Context, loader
from twitter_utils import get_favorites, status_to_hash
import json

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render(Context({})))

def favorites_data(request):
  statuses = [ status_to_hash(fave) for fave in get_favorites() ]
  return HttpResponse(json.dumps(statuses), mimetype="application/json")
