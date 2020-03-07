from app import db

class KantungParkir(db.Model):

    __tablename__ = 'kantung_parkir'

    kode = db.Column(db.String(10), primary_key=True)
    nama = db.Column(db.String(15), nullable=False)
    alamat = db.Column(db.String(50), nullable=False)
    kapasitas = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<KantungParkir: {}>".format(self.kode)