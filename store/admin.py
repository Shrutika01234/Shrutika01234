from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin


# Register your models here.

from .models import *
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','status']
    filter = ['status']

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','status','image_tag']
    filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','price','quantity','amount']
    list_filter = ['user']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','image_tag']


class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product','price','quantity','amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone','city','total','status']
    list_filter = ['status']
    readonly_fields = ('user','address','city','country','phone','first_name','ip', 'last_name','phone','city','total')
    can_delete = False
    inlines = [OrderProductline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','price','quantity','amount']
    list_filter = ['user']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','comment','ip','user','product','rate','id')


admin.site.register(UserProfile,UserProfileAdmin)



admin.site.register(Category,CategoryAdmin2)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
admin.site.register(ContactMessage)
admin.site.register(Blog)
admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Variants)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
admin.site.register(Comment,CommentAdmin)



