from django.contrib import admin
from django.apps import apps

Chunk = apps.get_model('chunks', 'chunk')


class ChunkAdmin(admin.ModelAdmin):
    list_display = ('key', 'description',)
    search_fields = ('key', 'content')


admin.site.register(Chunk, ChunkAdmin)
