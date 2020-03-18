from flask import request
from flask_restplus import Resource, Namespace, fields,inputs,reqparse


from ..service.data_kartu_service import save_data_kartu,get_all_data_kartu, get_data_kartu_bySerial, update_data_kartu




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
class DataPersonalList(Resource):
    @api.doc('Daftar Keseluruhan data personal')
    @api.marshal_list_with(data_kartu,envelope='data')
    def get(self):
        return get_all_data_kartu()

    @api.response(201,'Data personal berhasil ditambahkan')
    @api.doc('Menambahkan data personal')
    @api.expect(data_kartu,validate=True)
    def post(self):
        data = request.json
        return save_data_kartu(data)


@api.route('/<serial>')
@api.param('serial', 'Nomor Serial kartu parkir')
@api.response(404,'Data Kartu tidak ditemukan')
class Kartu_by_serial(Resource):
    @api.doc('ambil data kartu berdasarkan serial kartu')
    @api.marshal_with(data_kartu)
    def get(self,serial):
        data_kartu_byserial = get_data_kartu_bySerial(serial)
        if not data_kartu_byserial:
            api.abort(404)
        else:
            return data_kartu_byserial
    
    @api.doc("update data kartu berdasarkan serial kartu")
    @api.expect(data_kartu,validate=True)
    def put(self,serial):
        return update_data_kartu(serial,api.payload)