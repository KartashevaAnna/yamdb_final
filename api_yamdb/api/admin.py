from django.contrib import admin

from reviews.models import Category, Genre, Title, Review, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_filter = ("name", "slug")
    empty_value_display = "-empty-"


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_filter = ("name", "slug")
    empty_value_display = "-empty-"


class TitleAdmin(admin.ModelAdmin):
    def genre(self, obj):
        return [genre.name for genre in obj.genre.all()]

    def category(self, obj):
        return [category.name for category in obj.category.all()]

    list_display = (
        "name",
        "year",
        "description",
        "genre",
        "category",
    )
    list_filter = ("name", "year", "description")
    empty_value_display = "-empty-"


class ReviewAdmin(admin.ModelAdmin):
    def title(self, obj):
        return [title.name for title in obj.title.all()]

    def author(self, obj):
        return [author.name for author in obj.author.all()]

    list_display = [
        "title",
        "text",
        "author",
        "score",
        "pub_date",
    ]
    list_filter = [
        field.name
        for field in Review._meta.get_fields()
        if not field.many_to_many
    ]
    empty_value_display = "-empty-"


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        field.name
        for field in Comment._meta.get_fields()
        if not field.many_to_many
    ]
    list_filter = [
        field.name
        for field in Comment._meta.get_fields()
        if not field.many_to_many
    ]
    empty_value_display = "-empty-"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
