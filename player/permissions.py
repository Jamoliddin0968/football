from rest_framework import permissions

class myPermission(permissions.IsAuthenticatedOrReadOnly):
    pass