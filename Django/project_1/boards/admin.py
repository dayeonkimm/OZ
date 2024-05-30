from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
	list_display = ('title', 'writer', 'date', 'likes', 'updated_at', 'created_at')
	list_filter = ('date', 'writer')
	search_fields = ['title', 'content']
	ordering = ('-date',)
	readonly_fields = ('writer',)
	fieldsets = (
        (None, {'fields': ('title', 'content')}),
        ('추가옵션', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
    )
	list_per_page = 1
 
	actions = ('increment_likes',)
		
	def increment_likes(self, request, queryset):
		for board in queryset:
			board.likes += 1
			board.save()
    
	increment_likes.short_description = "선택한 게시글의 좋아요 수 증가"
 
