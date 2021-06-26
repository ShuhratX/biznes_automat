from django.contrib import admin
from worker.models import Worker


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'salary')


admin.site.register(Worker, WorkerAdmin)
