from datetime import datetime
from app import db
from app.model.data_kartu import Kartu
import logging

LOG = logging.getLogger(__name__)

def save_data_kartu(data):
    data_kartu = Kartu.query.filter(Kartu.serial_kartu == data['serial_kartu'] or Kartu.nim == data['nim']).scalar()
    if not data_kartu:
        try:
            new_data = Kartu(
                serial_kartu = data['serial_kartu'],
                nopol = data['nopol'],
                nim = data['nim'],
                tanggal_perso = data['tanggal_perso'],
                expired = data['expired'],
                status = data['status']
            )
            save_to_database(new_data)
            response_object ={
                'status':"Berhasil",
                'message':"Data kartu berhasil disimpan"
            }
            LOG.info('Berhasil menyimpan data kartu :')
            return True,response_object
        except Exception as e:
            db.session.rollback()
            response_object ={
                'status':"Gagal",
                'message':"Terjadi kesalahan saat penyimpanan data"
            }
            LOG.error("Terjadi kesalahan : {}".format(e))
            return False,response_object
    else:
        LOG.info("Data kartu gagal ditambahkan, Serial kartu atau NIM telah terdaftar")
        response_object = {
            'status':"Gagal",
            "message":"Serial kartu : {} atau NIM {} telah terdaftar".format(data['serial_kartu'],data['nim'])
        }
        return False,response_object


def update_data_kartu(id,data):
    data_update = Kartu.query.get_or_404(id)
    if data_update is not None:
        try:
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
            LOG.info("Data kartu : {} Berhasil diperbarui".format(data['serial_kartu']))
            return True,response_object
        except Exception as e:
            db.session.rollback()
            response_object ={
                'status':"Gagal",
                'message':"Terjadi kesalahan saat update data"
            }
            LOG.error("Terjadi kesalahan : {}".format(e))
            return False,response_object
    else:
        response_object = {
            'status':"Gagal",
            'message':"Data tidak ditemukan"
        }
        LOG.info("Data serial kartu {} tidak ditemukan".format(data['serial_kartu']))
        return False,response_object


def get_all_data_kartu():
    return Kartu.query.all()


def get_data_kartu_bySerial(serial):
    return Kartu.query.filter_by(serial_kartu=serial).first()

def save_to_database(data):
    db.session.add(data)
    db.session.commit()
def get_data_kartu_bySerial(serial):
    return Kartu.query.filter_by(serial_kartu=serial).first()


def save_to_database(data):
    db.session.add(data)
    db.session.commit()