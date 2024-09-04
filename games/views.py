# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Game, UserProfile, Bet
# from django.contrib.auth.models import User
# from django.http import HttpResponse

# @login_required
# def home(request):
#     games = Game.objects.all()
#     return render(request, 'games/home.html', {'games': games})

# @login_required
# def place_bet(request, game_id):
#     if request.method == 'POST':
#         amount = float(request.POST.get('amount', 0))
#         user_profile = UserProfile.objects.get(user=request.user)
#         game = Game.objects.get(id=game_id)
#         if user_profile.balance >= amount:
#             user_profile.balance -= amount
#             user_profile.save()
#             Bet.objects.create(user_profile=user_profile, game=game, amount=amount)
#             return redirect('home')
#         else:
#             return HttpResponse("Insufficient balance")
#     return render(request, 'games/place_bet.html', {'game_id': game_id})

# @login_required
# def profile(request):
#     user_profile = UserProfile.objects.get(user=request.user)
#     return render(request, 'games/profile.html', {'profile': user_profile})


# from rest_framework import viewsets
# from .models import Game, UserProfile, Bet
# from .serializers import GameSerializer, UserProfileSerializer, BetSerializer

# class GameViewSet(viewsets.ModelViewSet):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer

# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

# class BetViewSet(viewsets.ModelViewSet):
#     queryset = Bet.objects.all()
#     serializer_class = BetSerializer

# from rest_framework.permissions import IsAuthenticated
# from rest_framework import viewsets
# from .models import Game, UserProfile, Bet
# from .serializers import GameSerializer, UserProfileSerializer, BetSerializer

# class GameViewSet(viewsets.ModelViewSet):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer
#     permission_classes = [IsAuthenticated]

# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     permission_classes = [IsAuthenticated]

# class BetViewSet(viewsets.ModelViewSet):
#     queryset = Bet.objects.all()
#     serializer_class = BetSerializer
#     permission_classes = [IsAuthenticated]

# from rest_framework import viewsets
# from .models import Game, UserProfile, Bet, Transaction, Roulette, CoinToss, Blackjack, DiceRoll
# from .serializers import GameSerializer, UserProfileSerializer, BetSerializer, TransactionSerializer, RouletteSerializer, CoinTossSerializer, BlackjackSerializer, DiceRollSerializer

# class GameViewSet(viewsets.ModelViewSet):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer
#     # permission_classes = [IsAuthenticated]

# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     # permission_classes = [IsAuthenticated]

# class BetViewSet(viewsets.ModelViewSet):
#     queryset = Bet.objects.all()
#     serializer_class = BetSerializer
#     # permission_classes = [IsAuthenticated]

# class TransactionViewSet(viewsets.ModelViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#     # permission_classes = [IsAuthenticated]

# class RouletteViewSet(viewsets.ModelViewSet):
#     queryset = Roulette.objects.all()
#     serializer_class = RouletteSerializer
#     # permission_classes = [IsAuthenticated]

# class CoinTossViewSet(viewsets.ModelViewSet):
#     queryset = CoinToss.objects.all()
#     serializer_class = CoinTossSerializer
#     # permission_classes = [IsAuthenticated]

# class BlackjackViewSet(viewsets.ModelViewSet):
#     queryset = Blackjack.objects.all()
#     serializer_class = BlackjackSerializer
#     # permission_classes = [IsAuthenticated]

# class DiceRollViewSet(viewsets.ModelViewSet):
#     queryset = DiceRoll.objects.all()
#     serializer_class = DiceRollSerializer
#     # permission_classes = [IsAuthenticated]

from rest_framework import viewsets
from .models import Game, UserProfile, Bet, Transaction, Roulette, CoinToss, Blackjack, DiceRoll
from .serializers import GameSerializer, UserProfileSerializer, BetSerializer, TransactionSerializer, RouletteSerializer, CoinTossSerializer, BlackjackSerializer, DiceRollSerializer
from rest_framework.permissions import IsAuthenticated

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

class RouletteViewSet(viewsets.ModelViewSet):
    queryset = Roulette.objects.all()
    serializer_class = RouletteSerializer
    permission_classes = [IsAuthenticated]

class CoinTossViewSet(viewsets.ModelViewSet):
    queryset = CoinToss.objects.all()
    serializer_class = CoinTossSerializer
    permission_classes = [IsAuthenticated]

class BlackjackViewSet(viewsets.ModelViewSet):
    queryset = Blackjack.objects.all()
    serializer_class = BlackjackSerializer
    permission_classes = [IsAuthenticated]

class DiceRollViewSet(viewsets.ModelViewSet):
    queryset = DiceRoll.objects.all()
    serializer_class = DiceRollSerializer
    permission_classes = [IsAuthenticated]
