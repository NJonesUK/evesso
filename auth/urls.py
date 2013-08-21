from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'users.views.register', name='home'),
    # url(r'^auth/', include('auth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #user management URLs
    url(r'^accounts/login/$', 'users.views.custom_login'),
    url(r'^accounts/logout/$', 'users.views.custom_logout'),
    url(r'^accounts/register/$', 'users.views.register'),
    url(r'^accounts/profile/$', 'users.views.profile'),
    url(r'^accounts/changepassword/$', 'django.contrib.auth.views.password_change'),
    url(r'^accounts/changepassworddone/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'registration/password_change_done.html'}),
)

urlpatterns += staticfiles_urlpatterns()
