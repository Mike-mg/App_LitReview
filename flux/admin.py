from django.contrib import admin
from flux.models import Ticket, UserFollows, Review


@admin.register(Ticket)
class TiketAdmin(admin.ModelAdmin):
    pass

@admin.register(UserFollows)
class UserfollowsAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass