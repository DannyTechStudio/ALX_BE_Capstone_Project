import re
import pycountry
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

# Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_at']
    
    # Validate password strength
    def validate_password(self, pwd):
        if len(pwd) < 8:
            raise serializers.ValidationError('Password must be at 8 characters long.')
        if not re.search(r'[A-Z]', pwd):
            raise serializers.ValidationError('Password must contain at least 1 uppercase letter.')
        if not re.search(r'[a-z]', pwd):
            raise serializers.ValidationError('Password must contain at least 1 lowercase letter.')
        if not re.search(r'\d', pwd):
            raise serializers.ValidationError('Password must contain at least 1 number.')
        if not re.search(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', pwd):
            raise serializers.ValidationError('Password must contain at least 1 symbol.')
        return pwd
            
    # Create a new user
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        Token.objects.create(user=user)
        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        User = get_user_model()
        
        # Getting the user by their email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials!')
        
        # Autheticate user
        user = authenticate(username=user.email, password=password)
        
        if not user:
            raise serializers.ValidationError('Invalid credentials!')

        if not user.is_active:
            raise serializers.ValidationError('This account is inactive.')

        return user
            

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'currency']
        extra_kwargs = {
            'username': {'required': False},
            'currency': {'required': False},
        }
        
        def validate_currency(self, value):
            value = value.upper()
            if not pycountry.currencies.get(alpha_3=value):
                raise serializers.ValidationError("Invalid ISO currency code.")
            return value