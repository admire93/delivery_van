# -*- coding: utf-8 -*-
from pytest import fixture
from flask import _request_ctx_stack, g
from sqlalchemy.orm import sessionmaker

from dv.web.app import app
from dv.db import get_session, Base, get_engine


@fixture
def f_session(request):
    with app.test_request_context() as _ctx:
        Session = sessionmaker(autocommit=False, autoflush=False)
        app.config['DATABASE_URL'] = 'sqlite:///test.db'
        engine = get_engine(app)
        Base.metadata.create_all(engine)
        _ctx.push()
        session = Session(bind=engine)
        setattr(g, 'sess', session)
        def finish():
            session.close()
            Base.metadata.drop_all(engine)
            engine.dispose()

        request.addfinalizer(finish)
        return session


def pytest_addoption(parser):
    parser.addoption('--crawl',
                     action='store_true',
                     help='run tests that actually crawl bugs web page')


@fixture
def f_page():
    with open('./tests/assets/test.html', 'r') as f:
        return f.read()

