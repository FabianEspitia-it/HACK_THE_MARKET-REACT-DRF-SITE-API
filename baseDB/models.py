# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.hashers import make_password


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'brand'

    def __str__(self) -> str:
        return self.brand_name


class CartProduct(models.Model):
    id_cart = models.ForeignKey('ShoppingCart', models.DO_NOTHING, db_column='ID_cart', blank=True, null=True)  # Field name made lowercase.
    id_product = models.ForeignKey('Product', models.DO_NOTHING, db_column='ID_product', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart_product'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'category'

    def __str__(self) -> str:
        return self.category_name


class CpuKind(models.Model):
    cpu_kind_id = models.AutoField(primary_key=True)
    cpu_kind_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cpu_kind'

    def __str__(self) -> str:
        return self.cpu_kind_name


class DeliveryMethod(models.Model):
    delivery_method_id = models.AutoField(primary_key=True)
    delivery_method_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'delivery_method'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Kind(models.Model):
    kind_id = models.AutoField(primary_key=True)
    kind_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'kind'

    def __str__(self) -> str:
        return self.kind_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(blank=True, null=True)
    order_cart = models.ForeignKey('ShoppingCart', models.DO_NOTHING, db_column='order_cart')
    order_user = models.ForeignKey('User', models.DO_NOTHING, db_column='order_user')

    class Meta:
        managed = False
        db_table = 'order'


class OrderProduct(models.Model):
    id_order = models.ForeignKey(Order, models.DO_NOTHING, db_column='ID_order', blank=True, null=True)  # Field name made lowercase.
    id_product = models.ForeignKey('Product', models.DO_NOTHING, db_column='ID_product', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_product'


class OtherCharacteristics(models.Model):
    other_characteristics_id = models.AutoField(primary_key=True)
    other_characteristics_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'other_characteristics'

    def __str__(self) -> str:
        return self.other_characteristics_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(blank=True, null=True)
    product_image = models.TextField(blank=True, null=True)
    product_price = models.FloatField(blank=True, null=True)
    product_stock = models.PositiveIntegerField(blank=True, null=True)
    product_ram_memory = models.IntegerField(blank=True, null=True)
    product_storage = models.IntegerField(blank=True, null=True)
    product_screen_size = models.IntegerField(blank=True, null=True)
    product_other_characteristics = models.ForeignKey(OtherCharacteristics, models.DO_NOTHING, db_column='product_other_characteristics', blank=True, null=True)
    product_kind = models.ForeignKey(Kind, models.DO_NOTHING, db_column='product_kind', blank=True, null=True)
    product_cpu_kind = models.ForeignKey(CpuKind, models.DO_NOTHING, db_column='product_cpu_kind', blank=True, null=True)
    product_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='product_category', blank=True, null=True)
    product_brand = models.ForeignKey(Brand, models.DO_NOTHING, db_column='product_brand', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'

    def __str__(self) -> str:
        return f"Name: {self.product_name} - Price: {self.product_price} - Stock: {self.product_stock} - Brand: {self.product_brand} - Category: {self.product_category}"


class ShoppingCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cart_delivery_cost = models.FloatField(blank=True, null=True)
    cart_delivery_discount = models.FloatField(blank=True, null=True)
    cart_total_cost = models.FloatField(blank=True, null=True)
    cart_delivery_method = models.ForeignKey(DeliveryMethod, models.DO_NOTHING, db_column='cart_delivery_method', blank=True, null=True)
    cart_user = models.ForeignKey('User', models.DO_NOTHING, db_column='cart_user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_cart'

    def __str__(self) -> str:
        return f"User: {self.cart_user} Delivery Method: {self.cart_delivery_method} -  Delivery Cost: {self.cart_delivery_cost} - Delivery Discount: {self.cart_delivery_discount} - Total Cost: {self.cart_total_cost} "


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(unique=True, max_length=100)
    user_password = models.CharField(max_length=200)
    user_address = models.CharField(max_length=100)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def set_password(self, raw_password):
        self.user_password = make_password(raw_password)

    class Meta:
        managed = False
        db_table = 'user'
    
    def __str__(self) -> str:
        return f"Name: {self.user_name} - Email: {self.user_email} - Address: {self.user_address}"
    
    
