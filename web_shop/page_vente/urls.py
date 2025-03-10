from django.urls import path
from . import views
from page_vente.views import add_to_cart, cart_detail, vider_panier, remove_from_cart, get_product_images

app_name = 'boutique'

urlpatterns = [
    path('', views.index, name="index"),
    path('tous-les-produits/macrames/', views.macrames, name="macrames"),
    path('tous-les-produits/maroquinerie/', views.maroquinerie, name="maroquinerie"),
    path('creation-sur-mesure/', views.creation_sur_mesure, name="creation-sur-mesure"),
    path('tous-les-produits/hybride/', views.hybride, name="hybride"),
    path('tous-les-produits/', views.tous_les_produits, name="tous-les-produits"),
    path('panier/', views.panier, name="panier"),
    path('a_propos/', views.a_propos, name="a_propos"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('vider_panier/', vider_panier, name='vider_panier'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('get_product_images/<int:article_id>/', get_product_images, name='get_product_images'),
    path('checkout/', views.checkout, name='checkout'),
]