from django.urls import path
from .views import (
    admin_access,
    admin_logout,
    book_create,
    book_delete,
    book_update,
    comprar_libro,
    detalle_libro,
    home,
    store_dashboard,
)

urlpatterns = [
    path('', home, name='home'),
    path('admin-entrar/', admin_access, name='admin_access'),
    path('admin-salir/', admin_logout, name='admin_logout'),
    path('dashboard/', store_dashboard, name='store_dashboard'),
    path('dashboard/crear/', book_create, name='book_create'),
    path('dashboard/<int:pk>/editar/', book_update, name='book_update'),
    path('dashboard/<int:pk>/eliminar/', book_delete, name='book_delete'),
    path('libro/<int:pk>/', detalle_libro, name='libro_detalle'),
    path('libro/<int:pk>/comprar/', comprar_libro, name='libro_comprar'),
]
