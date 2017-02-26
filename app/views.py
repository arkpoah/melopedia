#-*- coding: utf-8 -*-
#from config import ITEM_PER_PAGE
from app import app, db
from flask import render_template, request
from flask_paginate import Pagination, get_page_args
from app.models import Artist, Tag, Album
from lastfm import artist_infos

@app.route('/')
@app.route('/index')
def index():
    tags = Tag.query.all()
    tags = sorted(tags, key=lambda x: x.nb_artists(),reverse=True)
    art_years = list(set([y.year for y in Artist.query.filter(Artist.year).all()]))
    alb_years = list(set([y.year for y in Album.query.filter(Album.year).all()]))
    return render_template("index.html", tags=tags, artist_years=art_years, album_years=alb_years)


### ARTISTS
@app.route('/artists')
def artists(page=1):
    search = True if request.args.get('q') else False
#    page = request.args.get('page', type=int, default=1)

    page, per_page, offset = get_page_args()
    artists = Artist.query.order_by(Artist.rate.desc()).offset(offset).limit(per_page).all()
    pagination = Pagination(bs_version=3,page=page, per_page=per_page, total=len(Artist.query.all()), search=search, record_name='artists')
    return render_template("artists.html", artists=artists, pagination=pagination, title='Artists')

@app.route('/artist/<artist>')
def artist(artist):
    artist = Artist.query.filter_by(slug=artist).first()
    tags = Tag.query.filter(Tag.artists.any(id=artist.id)).all()
    return render_template("artist.html", artist=artist, tags=tags, albums=artist.albums.all(), title=artist.name)


### ALBUMS
@app.route('/albums')
def albums(page=1):
    search = True if request.args.get('q') else False

    page, per_page, offset = get_page_args()
    albums = Album.query.order_by(Album.rate.desc()).offset(offset).limit(per_page).all()
    pagination = Pagination(bs_version=3,page=page, per_page=per_page, total=len(Album.query.all()), search=search, record_name='albums')
    return render_template("albums.html", albums=albums, pagination=pagination, title='Albums')

@app.route('/album/<alb_id>')
def album(alb_id):
    album = Album.query.get(alb_id)
    return render_template("album.html", album=album, title=album.name)


### TAGS
@app.route('/tag/<tagname>')
def tags(tagname, page=1):
    search = True if request.args.get('q') else False

    page, per_page, offset = get_page_args()
    tag = Tag.query.filter_by(slug=tagname).first()
    pagination = Pagination(bs_version=3,page=page, per_page=per_page, total=tag.artists.count(), search=search, record_name=tag.name + ' artists')
    return render_template("artists.html", artists=sampling(tag.artists.order_by(Artist.rate.desc()), offset, per_page), pagination=pagination, title=tagname.capitalize())

### SEARCH
@app.route('/artists/rate/<rate>')
def artists_by_rate(rate, page=1):
    search = True if request.args.get('q') else False

    page, per_page, offset = get_page_args()
    artists = Artist.query.filter_by(rate=float(rate)).all()
    pagination = Pagination(bs_version=3,page=page, per_page=per_page, total=len(artists), search=search, record_name='artists with rate ' + rate)
    return render_template("artists.html", artists=sampling(artists, offset, per_page), pagination=pagination, title='Artist rate ' + rate)

@app.route('/albums/rate/<rate>')
def albums_by_rate(rate, page=1):
    search = True if request.args.get('q') else False

    page, per_page, offset = get_page_args()
    albums = Album.query.filter_by(rate=float(rate)).all()
    pagination = Pagination(bs_version=3,page=page, per_page=per_page, total=len(albums), search=search, record_name='albums with rate ' + rate)
    return render_template("albums.html", albums=sampling(albums, offset, per_page), pagination=pagination, title='Album rate ' + rate)

@app.route('/artists/year/<year>')
def artists_by_year(year, page=1):
    search = True if request.args.get('q') else False

    page, per_page, offset = get_page_args()
    artists = Artist.query.filter_by(year=int(year)).all()
    pagination = Pagination(bs_version=3,page=page, per_page=per_page, total=len(artists), search=search, record_name='artists began in ' + year)
    return render_template("artists.html", artists=sampling(artists, offset, per_page), pagination=pagination, title=year + ' artists')

@app.route('/albums/year/<year>')
def albums_by_year(year, page=1):
    search = True if request.args.get('q') else False

    page, per_page, offset = get_page_args()
    albums = Album.query.filter_by(year=int(year)).all()
    pagination = Pagination(bs_version=3,page=page, per_page=per_page, total=len(albums), search=search, record_name='albums created in ' + year)
    return render_template("albums.html", albums=sampling(albums, offset, per_page), pagination=pagination, title=year + ' albums')




def sampling(selection, offset=0, limit=None):
    return selection[offset:(limit + offset if limit is not None else None)]


