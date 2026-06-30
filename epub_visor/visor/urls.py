from django.urls import path
from . import views

urlpatterns = [
    path('', views.library, name='library'),
    path('upload/', views.upload_book, name='upload_book'),
    path('scan-opencode/', views.scan_opencode, name='scan_opencode'),
    path('book/<slug:slug>/', views.book_detail, name='book_detail'),
    path('book/<slug:slug>/read/', views.reader, name='reader'),
    path('book/<slug:slug>/download/', views.download_epub, name='download_epub'),
    path('book/<slug:slug>/download-pdf/', views.download_pdf, name='download_pdf'),
    path('book/<slug:slug>/diagnostics/', views.run_diagnostics, name='run_diagnostics'),
    path('book/<slug:slug>/delete/', views.delete_book, name='delete_book'),
    path('book/<slug:slug>/buy/', views.buy_now, name='buy_now'),
    path('cart/', views.cart_detail, name='cart'),
    path('cart/add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
    path('checkout/cancel/', views.checkout_cancel, name='checkout_cancel'),
    path('orders/', views.order_list, name='orders'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('stripe/webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
