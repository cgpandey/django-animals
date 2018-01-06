from django.contrib.auth.models import User
from tastypie.serializers import Serializer
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import DjangoAuthorization, ReadOnlyAuthorization, Authorization

from .models import Animals

import urlparse
#this class is used to serialize the data
class urlencodeSerializer(Serializer):
    formats = ['json', 'jsonp', 'xml', 'yaml', 'html', 'plist', 'urlencode']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'xml': 'application/xml',
        'yaml': 'text/yaml',
        'html': 'text/html',
        'plist': 'application/x-plist',
        'urlencode': 'application/x-www-form-urlencoded',
        #'multipart': 'multipart/form-data',
        }
    def from_urlencode(self, data,options=None):
        """ handles basic formencoded url posts """
        qs = dict((k, v if len(v)>1 else v[0] )
            for k, v in urlparse.parse_qs(data).iteritems())
        return qs

    def to_urlencode(self,content): 
        pass

    def format_date(self, data):
        return data.strftime("%d-%m-%Y")

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get']
        resource_name = 'user'
        excludes = ['password']
        always_return_data = True
        filtering = {
            'username': 'exact'
        }

class AnimalResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner', full=True)
    class Meta:
        queryset = Animals.objects.all()
        resource_name = 'animal'
        allowed_methods = ['get', 'post', 'put','patch','delete']
        limit = 0
        always_return_data = True
        #authentication = AdminApiKeyAuthentication()
        authorization = Authorization()
        serializer = urlencodeSerializer()
        filtering = {
        	'contact_id' : ALL,
        	'contact_name' : ALL,
        	'contact_email' : ALL,
        	'contact_mobile' : ALL
		}
