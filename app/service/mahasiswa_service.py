from app import db
from app.model.data_kartu import Mahasiswa


def get_mhs_byNim(nim):
    return Mahasiswa.query.filter_by(nim=nim).first()