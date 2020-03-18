from datetime import datetime
from app import db
from app.model.data_kartu import Kartu


def save_data_kartu(data):
    data_kartu = Kartu.query.filter_by(serial_kartu=data['serial_kartu']).first()
    if not data_kartu:
        new_data = Kartu(
            serial_kartu = data['serial_kartu'],
            nopol = data['nopol'],
            nim = data['nim'],
            tanggal_perso = data['tanggal_perso'],
            expired = data['expired'],
            status = data['status']
        )
        save_to_database(new_data)
        response_object = {
            'status':'berhasil',
            'message':'Data personal berhasil ditambahkan'
        }
        return response_object
    else:
        response_object = {
            'status':'gagal',
            'message':'Data personal gagal ditambahkan',
        }
        return response_object


def update_data_kartu(id,data):
    data_update = Kartu.query.get_or_404(id)
    if data_update is not None:
        data_update.serial_kartu = data['serial_kartu']
        data_update.nopol = data['nopol']
        data_update.nim = data['nim']
        data_update.tanggal_perso = data['tanggal_perso']
        data_update.expired = data['expired']
        data_update.status = data['status']
        db.session.commit()
        response_object = {
            'status':'berhasil',
            'message':'Data kartu berhasil di update'
        }
        return response_object
    else:
        response_object = {
            'status':'gagal',
            'message':'Data kartu gagal di update'
        }  


def get_all_data_kartu():
    return Kartu.query.all()


def get_data_kartu_bySerial(serial):
    return Kartu.query.filter_by(serial_kartu=serial).first()


def save_to_database(data):
    db.session.add(data)
    db.session.commit()