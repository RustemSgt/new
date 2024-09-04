# from rest_framework import serializers
# from .models import Game, UserProfile, Bet

# class GameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields = '__all__'

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'

# class BetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bet
#         fields = '__all__'

# from rest_framework import serializers
# from .models import Game, UserProfile, Bet, Transaction, Roulette, CoinToss, Blackjack, DiceRoll

# class GameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields = '__all__'

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'

# class BetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bet
#         fields = '__all__'

# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = '__all__'

# class RouletteSerializer(GameSerializer):
#     class Meta:
#         model = Roulette
#         fields = '__all__'

# class CoinTossSerializer(GameSerializer):
#     class Meta:
#         model = CoinToss
#         fields = '__all__'

# class BlackjackSerializer(GameSerializer):
#     class Meta:
#         model = Blackjack
#         fields = '__all__'

# class DiceRollSerializer(GameSerializer):
#     class Meta:
#         model = DiceRoll
#         fields = '__all__'


from rest_framework import serializers
from .models import Game, UserProfile, Bet, Transaction, Roulette, CoinToss, Blackjack, DiceRoll

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class RouletteSerializer(GameSerializer):
    class Meta:
        model = Roulette
        fields = '__all__'

class CoinTossSerializer(GameSerializer):
    class Meta:
        model = CoinToss
        fields = '__all__'

class BlackjackSerializer(GameSerializer):
    class Meta:
        model = Blackjack
        fields = '__all__'

class DiceRollSerializer(GameSerializer):
    class Meta:
        model = DiceRoll
        fields = '__all__'
