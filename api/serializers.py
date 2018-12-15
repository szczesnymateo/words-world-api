from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Language, Question, Answer, Achievement, Score, Challenge, GivenAnswer, Round, UserFollowing


class AchievementBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name', 'condition', 'font_awesome_icon')


class QuestionBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'context', 'external_source',
                  'language', 'question_type', 'get_gap_markdown',
                  'difficulty')


class AnswerBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'context', 'is_correct')


class UserBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    achievements = AchievementBaseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'achievements')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name')


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionBaseSerializer(many=False, read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'context', 'is_correct', 'question')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerBaseSerializer(many=True, read_only=True)
    language = LanguageSerializer(many=False, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'context', 'external_source',
                  'language', 'question_type', 'answers',
                  'get_gap_markdown', 'difficulty')


class RoundSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=False)

    class Meta:
        model = Round
        fields = ('id', 'round_number', 'question')


class ChallengeSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=False, read_only=True)
    rounds = RoundSerializer(many=True)

    class Meta:
        model = Challenge
        fields = ('id', 'language', 'rounds')


class GivenAnswerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    
    class Meta:
        model = GivenAnswer
        fields = ('id', 'user', 'round', 'is_correct')
        

class ScoreSerializer(serializers.ModelSerializer):
    given_answers = GivenAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Score
        fields = ('id', 'status', 'challenge', 'given_answers')


class UserChallenge(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'scores')


class UserFollowingSerializer(serializers.ModelSerializer):
    users = UserBaseSerializer(many=True)

    class Meta:
        model = UserFollowing
        fields = ('users',)



