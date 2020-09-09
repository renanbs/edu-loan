from pycpfcnpj import cpfcnpj
from marshmallow import fields, Schema, validate


class SerializerException(Exception):
    pass


class BaseSchema(Schema):
    token = fields.Str(required=True)


class AuthSerializer(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


def validate_cpf(cpf):
    if not cpfcnpj.validate(cpf):
        raise SerializerException('Invalid CPF')


class CpfSerializer(BaseSchema):
    data = fields.Str(validate=validate_cpf, required=True)


def validate_name(fullname):
    splitted = fullname.split(' ', maxsplit=1)
    if len(splitted) != 2:
        raise SerializerException('You must provide your full name')


class NameSerializer(BaseSchema):
    data = fields.Str(validate=validate_name, required=True)


class BirthDaySerializer(BaseSchema):
    data = fields.Date(required=True)


class PhoneSerializer(BaseSchema):
    data = fields.Str(validate=validate.Length(min=10, max=11), required=True)


class AddressSerializer(BaseSchema):
    data = fields.Str(required=True)


class AmountSerializer(BaseSchema):
    data = fields.Number(required=True)


class EventFlowSerializer(Schema):
    event_flow = fields.List(fields.Str(required=True))
