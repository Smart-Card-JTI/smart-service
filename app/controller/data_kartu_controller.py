from flask import request
from flask_restplus import Resource, Namespace, fields
from werkzeug.exceptions import NotFound
import logging

from ..service.data_kartu_service import save_data_kartu,get_all_data_kartu, get_data_kartu_bySerial, update_data_kartu

LOG = logging.getLogger(__name__)


api = Namespace('datakartu', 'Endpoints API untuk data kartu')
data_kartu = api.model('datakartu',{
    'serial_kartu': fields.String(required=True, description="Data serial Kartu"),
    'nopol': fields.String(required=True, description="Plat Nomor kendaraan mahasiswa"),
    'nim': fields.String(required=True,description='Data nim mahasiswa yang memiliki kartu'),
    'tanggal_perso': fields.DateTime(required=True, dt_format='iso8601'),
    'expired': fields.Date(required=True, description="Tanggal expired kartu yang dimiliki oleh mahasiswa"),
    'status': fields.Boolean(required=True,description="Status apakah kartu masih aktif atau tidak")
})

@api.route('/')
class DataPersonal(Resource):
    @api.doc(responses={200:'OK',404:'Not Found'},description="Mengambil seluruh data personal kartu")
    @api.marshal_list_with(data_kartu,envelope='data')
    def get(self):
        try:
            LOG.info('Berhasil mengambil data personal')
            return get_all_data_kartu()
        except Exception as e:
            LOG.error(e)
            api.abort(404)

    @api.doc(responses={200:'OK',400:'Bad Request'}, description="Endpoint untuk menambahkan data personal kartu")
    @api.expect(data_kartu)
    def post(self):
        try:
            data_personal = request.json
            status,message = save_data_kartu(data_personal)
        except Exception as e:
            LOG.error(e)
            api.abort(400,e.__doc__)
        else:
            if status:
                return message
            else:
                return message


@api.route('/<serial>')
class DataPersonalBySerial(Resource):
    @api.doc(responses={200:'OK',404:'Not Found'}, description="Mengambil data Kartu by serial kartu")
    @api.marshal_with(data_kartu)
    def get(self,serial):
        data_kartu_byserial = get_data_kartu_bySerial(serial)
        if not data_kartu_byserial:
            LOG.info("Data serial {}".format(serial))
            raise NotFound('data tidak ditemukan')
        else:
            LOG.info("Berhasil mengambil data serial : {}".format(serial))
            return data_kartu_byserial
    
    @api.doc(responses={200:'OK',400:'Bad Request'},description="Endpoint untuk update data kartu")
    @api.expect(data_kartu)
    def put(self,serial):
        try:
            status,message = update_data_kartu(serial,api.payload)
        except Exception as e:
            LOG.error(e)
            api.abort(400,e.__doc__)
        else:
            if status:
                return message
            else:
                return message