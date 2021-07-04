from app import db

class KantungParkir(db.Model):

    __tablename__ = 'kantung_parkir'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(15), nullable=False)
    keterangan = db.Column(db.String(25), nullable=False)
    kapasitas = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return "<KantungParkir: {}>".format(self.id)