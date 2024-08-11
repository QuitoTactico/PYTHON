import re
from datetime import datetime

class ValidationError(Exception):
    pass

class Field:
    def __init__(self, blank=False, default=None):
        self.blank = blank
        self.default = default
        self.name = None

    def validate(self, value):
        if value is None:
            if not self.blank:
                raise ValidationError(f"{self.name} cannot be blank")
        else:
            self.validate_value(value)

    def validate_value(self, value):
        raise NotImplementedError

class CharField(Field):
    def __init__(self, min_length=0, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def validate_value(self, value):
        if not isinstance(value, str):
            raise ValidationError(f"{self.name} must be a string")
        if len(value) < self.min_length:
            raise ValidationError(f"{self.name} must be at least {self.min_length} characters long")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(f"{self.name} must be at most {self.max_length} characters long")

class IntegerField(Field):
    def __init__(self, min_value=None, max_value=None, **kwargs):
        super().__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value

    def validate_value(self, value):
        if not isinstance(value, int):
            raise ValidationError(f"{self.name} must be an integer")
        if self.min_value is not None and value < self.min_value:
            raise ValidationError(f"{self.name} must be at least {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValidationError(f"{self.name} must be at most {self.max_value}")

class BooleanField(Field):
    def validate_value(self, value):
        if not isinstance(value, bool):
            raise ValidationError(f"{self.name} must be a boolean")

class DateTimeField(Field):
    def __init__(self, auto_now=False, **kwargs):
        super().__init__(**kwargs)
        self.auto_now = auto_now

    def validate_value(self, value):
        if not isinstance(value, datetime):
            raise ValidationError(f"{self.name} must be a datetime")

class EmailField(CharField):
    def validate_value(self, value):
        super().validate_value(value)
        if not re.match(r'^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+$', value):
            raise ValidationError(f"{self.name} must be a valid email address")

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {key: value for key, value in attrs.items() if isinstance(value, Field)}
        for key, value in fields.items():
            value.name = key
        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for name, field in self._fields.items():
            value = kwargs.get(name, field.default)
            if value is None and isinstance(field, DateTimeField) and field.auto_now:
                value = datetime.now()
            setattr(self, name, value)

    def validate(self):
        for name, field in self._fields.items():
            value = getattr(self, name)
            field.validate(value)


# --------------------------------------- TEST -----------------------------------------

class User(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)

hasattr(User, 'first_name')

user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
user1.validate()

print(user1.date_joined)  # imprime la fecha y hora cuando se creó la instancia
print(user1.is_verified)  # imprime False (valor por defecto)

user1.age = 256
try:
    user1.validate()  # lanza ValidationError - la edad está fuera del rango
except ValidationError as e:
    print(e)

user2 = User()
try:
    user2.validate()  # lanza ValidationError - los primeros tres campos son obligatorios
except ValidationError as e:
    print(e)