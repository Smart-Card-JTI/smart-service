from datetime import datetime
from app import db
from app.model.data_persolan import DataPersonal


def save_new_data_personal(data):
    data_personal = DataPersonal.query.filter_by(nim_mahasiswa=data['nim_mahasiswa']).first()
    if not data_personal:
        tanggal = datetime.strptime(data['tanggal_perso'],'%Y-%m-%d').date()
        new_data = DataPersonal(
            nim_mahasiswa = data['nim_mahasiswa'],
            uid_kartu = data['uid_kartu'],
            tanggal_perso = tanggal,
            userid = data['userid'] 
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


def update_data_personal(data):
    data_update = DataPersonal.query.get_or_404(data['nim'])
    if data_update is not None:
        data_update.nim = data['nim']
        data_update.uid_kartu = data['uid_kart']
        data_update.tanggal_perso = datetime.strf(data['tanggal_perso'],'%Y-%m-%d')
        data_update.userid = data['userid']
        db.session.commit()
        response_object = {
            'status':'berhasil',
            'message':'Data personal berhasil di update'
        }
        return response_object
    else:
        response_object = {
            'status':'gagal',
            'message':'Data personal gagal di update'
        }
        return response_object


def get_all_data_personal():
    return DataPersonal.query.all()


def get_data_personal_byNim(nim):
    return DataPersonal.query.filter_by(nim=nim)


def save_to_database(data):
    db.session.add(data)
    db.session.commit()