from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Post

admin.site.unregister(Group)

# Mix Profile info into User info
class ProfileInline(admin.StackedInline):
	model = Profile

class UserAdmin(admin.ModelAdmin):
	model = User
	fields = ["username", "first_name", "last_name", "email", "is_staff"]
	inlines = [ProfileInline]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)

admin.site.register(Post)