from django.contrib import admin
from .models import BrideSide, GroomSide


class GroomSideAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'attending',
        'total_attending',
        'coach_attending',
        'song_request',
    )
    ordering = ('id',)


class BrideSideAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'attending',
        'total_attending',
        'song_request',
    )
    ordering = ('id',)

admin.site.register(BrideSide, BrideSideAdmin)
admin.site.register(GroomSide, GroomSideAdmin)
