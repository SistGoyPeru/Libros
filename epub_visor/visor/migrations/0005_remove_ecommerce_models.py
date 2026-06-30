from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0004_book_is_featured_book_price_cart_order_orderitem_and_more'),
    ]

    operations = [
        migrations.DeleteModel('OrderItem'),
        migrations.DeleteModel('CartItem'),
        migrations.DeleteModel('Order'),
        migrations.DeleteModel('Cart'),
    ]
