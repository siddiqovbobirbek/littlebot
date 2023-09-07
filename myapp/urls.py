from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'botuser', BotUserViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'subcategory', SubCategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderitem', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('change/', ChangeLanguage.as_view()),
    path('phone/', ChangePhoneNumber.as_view()),
    path('shop/', OrderItems.as_view()),
    path('set_order/', SetOrderItem.as_view()),
    path('delete_basket/', DestroyBasket.as_view()),
    path('user/', BotUserInfo.as_view()),
    path('delete_item/', DeleteItem.as_view())

]