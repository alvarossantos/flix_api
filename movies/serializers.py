from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


# Puxando um classe de serializer do rest_framework
class MovieModelSerializer(serializers.ModelSerializer):

    # Ligando ao banco de dados de Movie, chamando todos os campos = __all__
    class Meta:
        model = Movie
        fields = '__all__'

    # Validando se o ano de Movie e maior que 1980
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1980.")
        return value

    # Validando se o resumo de Movie e menor que 200 caracteres
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("O resumo não pode ter mais de 200 caracteres.")
        return value


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    # Logica para o calculo da media de avaliacoes
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
