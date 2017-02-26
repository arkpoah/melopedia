from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(Artist, db.session))
admin.add_view(ModelView(Album, db.session))
admin.add_view(ModelView(Tag, db.session))
