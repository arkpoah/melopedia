#-*- coding: utf-8 -*-
#from config import ITEM_PER_PAGE
from app import app, db
from flask import render_template, request, jsonify
from app.models import Album, Artist, Tag
import json

@app.route('/_rate')
def rate():
    model = request.args.get('type', '', type=str)
    obj_id = request.args.get('id', 0, type=int)
    note = request.args.get('note', 0, type=float)

    if model == "album":
        album = Album.query.get(obj_id)
        album.rate = note
        db.session.add(album)
    if model == "artist":
        artist = Artist.query.get(obj_id)
        artist.rate = note
        db.session.add(artist)

    db.session.commit()
    return jsonify("ok")


@app.route('/_all.json')
def all():
    artists = Artist.query.all()
    albums = Album.query.all()
    tags = Tag.query.all()

    return json.dumps({'status':True,'error':None,'data':
                {
                    'artists': [{"img":a.img_url, "slug":a.slug, "display":a.name+" - "+str(a.year)} for a in artists],
                    'albums': [{"id":a.id, "display":a.name+" - "+str(a.year)} for a in albums],
                    'tags':[{"slug":t.slug, "display":t.name} for t in tags]
                }
               })

