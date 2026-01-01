from .media import Book, Movie

class MediaFactory:
    @staticmethod
    def create_media(media_type, **kwargs):
        if media_type == "book":
            return Book(kwargs['title'], kwargs['year'], kwargs['author'])
        elif media_type == "movie":
            return Movie(kwargs['title'], kwargs['year'], kwargs['director'])
        return None