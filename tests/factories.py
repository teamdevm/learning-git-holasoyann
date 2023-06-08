# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

<<<<<<< HEAD
from test_app_cc.database import db
from test_app_cc.user.models import User
=======
from testcc.database import db
from testcc.user.models import User
>>>>>>> origin/feature


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """User factory."""

    username = Sequence(lambda n: f"user{n}")
    email = Sequence(lambda n: f"user{n}@example.com")
    active = True

    class Meta:
        """Factory configuration."""

        model = User
