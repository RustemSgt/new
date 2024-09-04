# from django.db import models
# from django.contrib.auth.models import User

# class Game(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     def __str__(self):
#         return self.user.username

# class Bet(models.Model):
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     result = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username} bet {self.amount} on {self.game.name}"
# from django.db import models
# from django.contrib.auth.models import User

# class Game(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     def __str__(self):
#         return self.user.username

# class Bet(models.Model):
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     result = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username} bet {self.amount} on {self.game.name}"

# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     def __str__(self):
#         return self.user.username

# class Transaction(models.Model):
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_type = models.CharField(max_length=50)  # E.g., "Deposit", "Withdrawal"
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username} - {self.transaction_type} - {self.amount}"

# class Game(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class Bet(models.Model):
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     result = models.CharField(max_length=100, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username} bet {self.amount} on {self.game.name}"

# class Roulette(Game):
#     bet_number = models.IntegerField()
#     payout = models.DecimalField(max_digits=10, decimal_places=2)

# class CoinToss(Game):
#     result = models.CharField(max_length=10)  # "Heads" or "Tails"

# class Blackjack(Game):
#     player_hand = models.CharField(max_length=255)
#     dealer_hand = models.CharField(max_length=255)
#     result = models.CharField(max_length=50)  # "Win", "Lose", "Push"

# class DiceRoll(Game):
#     dice_roll = models.IntegerField()
#     payout = models.DecimalField(max_digits=10, decimal_places=2)


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)  # E.g., "Deposit", "Withdrawal"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.transaction_type} - {self.amount}"

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Bet(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    result = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username} bet {self.amount} on {self.game.name}"

class Roulette(Game):
    bet_number = models.IntegerField()
    payout = models.DecimalField(max_digits=10, decimal_places=2)

class CoinToss(Game):
    result = models.CharField(max_length=10)  # "Heads" or "Tails"

class Blackjack(Game):
    player_hand = models.CharField(max_length=255)
    dealer_hand = models.CharField(max_length=255)
    result = models.CharField(max_length=50)  # "Win", "Lose", "Push"

class DiceRoll(Game):
    dice_roll = models.IntegerField()
    payout = models.DecimalField(max_digits=10, decimal_places=2)
