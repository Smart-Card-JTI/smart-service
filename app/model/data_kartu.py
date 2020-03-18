from app import db

# class DataKartu(db.Model):

#     __tablename__ = 'data_kartu'

#     nim_mahasiswa = db.Column(db.String(10), primary_key=True)
#     uid_kartu = db.Column(db.String(225), nullable=False)
#     tanggal_perso = db.Column(db.Date, nullable=False)
#     userid = db.Column(db.Integer, nullable=False)

#     def __repr(self):
#         return "<DataKartu : {}>".format(self.nim_mahasiswa)

class Mahasiswa(db.Model):

    __tablename__ = "mahasiswa"

    nim = db.Column(db.String(18), primary_key=True)
    nama = db.Column(db.String(25), nullable=False)
    prodi = db.Column(db.String(5), nullable=False)
    jurusan = db.Column(db.String(4), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    hp = db.Column(db.String(13),nullable=False)
    kartu = db.relationship("Kartu", uselist=False, backref="mahasiswa")

    def __repr__(self):
        return "<Mahasiswa : {}>".format(self.nim)


class Kartu(db.Model):

    __tablename__="kartu"

    serial_kartu = db.Column(db.String(12), primary_key=True)
    nopol = db.Column(db.String(12), nullable=False)
    nim = db.Column(db.String(18), db.ForeignKey('mahasiswa.nim'), nullable=False)
    tanggal_perso = db.Column(db.DateTime(), nullable=False)
    expired = db.Column(db.Date(), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return "<Kartu: {}>".format(self.serial_kartu)