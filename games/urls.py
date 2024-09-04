# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('place_bet/<int:game_id>/', views.place_bet, name='place_bet'),
#     path('profile/', views.profile, name='profile'),
# ]
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import GameViewSet, UserProfileViewSet, BetViewSet

# router = DefaultRouter()
# router.register(r'games', GameViewSet)
# router.register(r'user_profiles', UserProfileViewSet)
# router.register(r'bets', BetViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import GameViewSet, UserProfileViewSet, BetViewSet, TransactionViewSet, RouletteViewSet, CoinTossViewSet, BlackjackViewSet, DiceRollViewSet

# router = DefaultRouter()
# router.register(r'games', GameViewSet)
# router.register(r'user_profiles', UserProfileViewSet)
# router.register(r'bets', BetViewSet)
# router.register(r'transactions', TransactionViewSet)
# router.register(r'roulette', RouletteViewSet)
# router.register(r'coin_toss', CoinTossViewSet)
# router.register(r'blackjack', BlackjackViewSet)
# router.register(r'dice_roll', DiceRollViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, UserProfileViewSet, BetViewSet, TransactionViewSet, RouletteViewSet, CoinTossViewSet, BlackjackViewSet, DiceRollViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'bets', BetViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'roulette', RouletteViewSet)
router.register(r'coin_toss', CoinTossViewSet)
router.register(r'blackjack', BlackjackViewSet)
router.register(r'dice_roll', DiceRollViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
