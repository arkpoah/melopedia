#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""parse_zik.py: ..."""

__author__  = "arkpoah"

import os
import argparse
import re
#flask app
from app import db, models

def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if not instance:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
    return instance

def get_album_year(album):
    try:
        year = int(re.search('.*(?P<year>[0-9]{4})(.*)?', album).group('year'))
        album = album.replace(str(year),'')
    except:
        year = 0
    return album, year

def add_tag(tag, artist):
    if ':' in tag:
        for t in tag.split(':'):
            t_obj = get_or_create(db.session, models.Tag, name=t)
            artist.tags.append(t_obj)
            db.session.add(artist)
    else:
        t_obj = get_or_create(db.session, models.Tag, name=tag)
        artist.tags.append(t_obj)

def add_to_db(tag, artist, albums):
    art = get_or_create(db.session, models.Artist, name=artist)
    add_tag(tag, art)
    db.session.add(art)
    for album in albums:
        album_name, album_year = get_album_year(album)
        alb = models.Album(name=album_name,artist=art,year=album_year)
        db.session.add(alb)
    db.session.commit()

def parse_zik(args):
    print "******", args.genre, "*****"
    for item in os.listdir(args.root):
        if os.path.isfile(os.path.join(args.root, item)):
                continue
        print "Artist : ", item
        albums = []
        for album in os.listdir(os.path.join(args.root, item)):
            if os.path.isdir(os.path.join(args.root, item, album)):
                albums.append(album)
                print "Album : ", album
        add_to_db(args.genre, item, albums)
        print ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get artists and albums")
    parser.add_argument("-r", "--root", help="root of file tree", default=".")
    parser.add_argument("-g", "--genre", help="genre parsed - multiple genre separated by ':'", required=True)
    args = parser.parse_args()
    parse_zik(args)
