from django.contrib import admin
from .models import BrideSide, GroomSide


class GroomSideAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'attending_gurdwara_groom',
        'total_attending_gurdwara_groom',
        'coach_attending_gurdwara_groom',
        'attending_reception_groom',
        'total_attending_reception_groom',
        'coach_attending_reception_groom',
        'song_request_groom',
    )
    ordering = ('id',)


class BrideSideAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'attending_gurdwara_bride',
        'total_attending_gurdwara_bride',
        'attending_reception_bride',
        'total_attending_reception_bride',
        'song_request_bride',
    )
    ordering = ('id',)

admin.site.register(BrideSide, BrideSideAdmin)
admin.site.register(GroomSide, GroomSideAdmin)
