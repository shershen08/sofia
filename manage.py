#!/usr/bin/env python
# encoding: utf-8
# by masterzh


import json

from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Shell
from flask_script import Server
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
manager = Manager(app)
miarate = Migrate(app, db)


def make_context():
    return dict(app=app, db=db, Memory=Memory)

manager.add_command('runserver', Server(host='0.0.0.0', port=9009))
manager.add_command('shell', Shell(make_context=make_context))
manager.add_command('db', MigrateCommand)


class Memory(db.Model):
    __tablename__ = 'memory'
    id = db.Column(db.Integer, primary_key=True)
    memory = db.Column(db.Integer, default=0)
    time = db.Column(db.Integer, default=0)

    def __init__(self, memory, time):
        self.memory = memory
        self.time = time


cur_time = 0


@app.route('/')
def index():
    global cur_time
    cur_time = 0

    return render_template('index.html')


@app.route('/meminfo', methods=['GET'])
def data():
    d = []
    global cur_time

    for m in db.session.query(Memory).filter(Memory.time > (cur_time / 1000)).all():
        d.append([m.time * 1000, m.memory])

    if len(d):
        cur_time = d[-1][0]

    return json.dumps(d)


if __name__ == '__main__':
    manager.run()
