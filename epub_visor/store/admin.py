from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count

from .models import Libro, PayhipClick


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    change_list_template = 'admin/store/libro/change_list.html'
    list_display = (
        'titulo',
        'precio',
        'publicado',
        'payhip_url',
        'payhip_clicks_count',
        'last_payhip_click',
    )
    list_filter = ('publicado',)
    search_fields = ('titulo', 'descripcion')
    readonly_fields = ('payhip_clicks_count', 'last_payhip_click')
    fields = (
        'titulo',
        'descripcion',
        'portada_url',
        'precio',
        'payhip_url',
        'publicado',
        'payhip_clicks_count',
        'last_payhip_click',
    )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_site.admin_view(self.dashboard_view), name='store_libro_dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        top_books = (
            Libro.objects.filter(publicado=True)
            .annotate(clicks=Count('payhip_clicks'))
            .order_by('-clicks')[:10]
        )
        total_clicks = PayhipClick.objects.count()
        recent_clicks = (
            PayhipClick.objects.select_related('libro')
            .order_by('-timestamp')[:20]
        )
        context = {
            **self.admin_site.each_context(request),
            'title': 'Dashboard de Payhip',
            'top_books': top_books,
            'total_clicks': total_clicks,
            'recent_clicks': recent_clicks,
        }
        return TemplateResponse(request, 'admin/store/libro/dashboard.html', context)

    def payhip_clicks_count(self, obj):
        return obj.payhip_clicks.count()
    payhip_clicks_count.short_description = 'Clicks Payhip'

    def last_payhip_click(self, obj):
        last = obj.payhip_clicks.order_by('-timestamp').first()
        return last.timestamp if last else '-'
    last_payhip_click.short_description = 'Último click'


@admin.register(PayhipClick)
class PayhipClickAdmin(admin.ModelAdmin):
    list_display = ('libro', 'timestamp', 'ip_address', 'short_user_agent')
    list_filter = ('timestamp', 'libro')
    search_fields = ('libro__titulo', 'ip_address', 'user_agent')

    def short_user_agent(self, obj):
        return obj.user_agent[:80]
    short_user_agent.short_description = 'User agent'
