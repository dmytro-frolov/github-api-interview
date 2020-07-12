from django.urls import path

from .views.github_app import Authenticate, OathCallback
from .views.profile import Info, Availability, Visibility, Remove


urlpatterns = [
    path('authenticate', Authenticate.as_view(), name='authenticate'),
    path('oath-callback', OathCallback.as_view(), name='oath-callback'),

    path('profile/info', Info.as_view(), name='profile_update-info'),
    path('profile/info/<str:username>', Info.as_view(), name='profile_list_username'),

    path('profile/availability', Availability.as_view(), name='profile_availability'),
    path('profile/visibility', Visibility.as_view(), name='profile_visibility'),
    path('profile/remove', Remove.as_view(), name='profile_remove'),
]
app_name = 'api'
