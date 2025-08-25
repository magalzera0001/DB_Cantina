{"natural_language_write_file_response": {"result": "The file was updated", "status": "succeeded"}}
from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('turma',)