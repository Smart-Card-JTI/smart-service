from app import db

class DataPersonal(db.Model):

    __tablename__ = 'data_personal'

    nim_mahasiswa = db.Column(db.String(10), primary_key=True)
    uid_kartu = db.Column(db.String(225), nullable=False)
    tanggal_perso = db.Column(db.Date, nullable=False)
    userid = db.Column(db.Integer, nullable=False)

    def __repr(self):
        return "<DataPersonal : {}>".format(self.nim_mahasiswa)