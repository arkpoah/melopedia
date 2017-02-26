#-*- coding: utf-8 -*-
from app import db
from lastfm import artist_infos
from sqlalchemy import event
from slugify import slugify


TagDetail = db.Table('TagDetail',
    db.Column('artistId', db.Integer, db.ForeignKey('Artist.id')),
    db.Column('tagId', db.Integer, db.ForeignKey('Tag.id'))
)

class Tag(db.Model):
    __tablename__ =  'Tag'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(50), index=True, unique=True)
    name = db.Column(db.String(50), index=True, unique=True)

    def __repr__(self):
        return '<Tag %r>' % self.name

    def nb_artists(self):
        return self.artists.count()

class Album(db.Model):
    __tablename__ = 'Album'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    year = db.Column(db.Integer, index=True)
    rate = db.Column(db.Float, index=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))

    def __repr__(self):
        return '<Album %r>' % self.name

class Artist(db.Model):
    __tablename__ =  'Artist'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(150), index=True, unique=True)
    name = db.Column(db.String(150), index=True, unique=True)
    year = db.Column(db.Integer, index=True)
    description = db.Column(db.Text)
    own_description = db.Column(db.Text)
    rate = db.Column(db.Float, index=True)
    img_url = db.Column(db.String(150))
    url = db.Column(db.String(150))
    tags = db.relationship('Tag', secondary=TagDetail, backref=db.backref('artists', lazy='dynamic')) #backref='artists')
    albums = db.relationship('Album', backref='artist', lazy='dynamic')

    def __repr__(self):
        return '<Artist %r>' % self.name

    def get_larger_img(self):
        if self.img_url is not None:
            return self.img_url.replace('64s','128s')

def artist_before_insert_listener(mapper, connection, target):
    target.slug = slugify(target.name)
    infos = artist_infos(target.name)
    target.url = infos["url"]
    target.img_url = infos["img_url"]
    target.description = infos["description"]

def tag_before_insert_listener(mapper, connection, target):
    target.slug = slugify(target.name)

event.listen(Artist, 'before_insert', artist_before_insert_listener)
event.listen(Tag, 'before_insert', tag_before_insert_listener)
