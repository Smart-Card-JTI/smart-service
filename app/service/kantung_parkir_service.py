from uuid import uuid4
from app import db
from app.model.kantung_parkir import KantungParkir


def save_new_kantung_parkir(data):
    parkir = KantungParkir.query.filter_by(nama=data['nama']).first()
    if not parkir:
        new_parkir = KantungParkir(
            nama = data['nama'],
            keterangan = data['keterangan'],
            kapasitas = data['kapasitas']
        )
        save_to_database(new_parkir)
        response_object = {
            'status':'berhasil',
            'message':'Kantung Parkir Berhasil Ditambah kan'
        }
        return response_object
    else:
        response_object = {
            'status':'gagal',
            'message':'Kantung Parkir Gagal Ditambah kan'
        }
        return response_object


def get_all_kantung_parkir():
    return KantungParkir.query.all()


def get_kantung_parkir_byID(id):
    return KantungParkir.query.filter_by(id=int(id)).first()


def save_to_database(data):
    db.session.add(data)
    db.session.commit()
