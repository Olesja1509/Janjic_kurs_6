from django.contrib import admin
from django.forms import ModelMultipleChoiceField

from service.models import Client, Mailing, Logs


@admin.register(Client)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user', )
    list_filter = ('user',)


@admin.register(Mailing)
class Mailing(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'finish_time', 'period', 'is_active', 'status', 'user', )
    list_filter = ('period', 'status', 'user', )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "clients":
            kwargs["queryset"] = Client.objects.all()
            kwargs["widget"] = admin.widgets.FilteredSelectMultiple(
                db_field.verbose_name,
                db_field.name in self.filter_vertical
            )
            return ModelMultipleChoiceField(**kwargs)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Logs)
class Mailing(admin.ModelAdmin):
    list_display = ('email', 'title', 'time', 'status',)
    list_filter = ('title', 'email', )
