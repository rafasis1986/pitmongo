import factory
from ..models import User


class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'name-{0}'.format(n))
    surname = factory.Sequence(lambda n: 'surname-{0}'.format(n))
    slug = factory.Sequence(lambda n: 'slug-{0}'.format(n))

    class Meta:
        model = User
        django_get_or_create = ('name', )
