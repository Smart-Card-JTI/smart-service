from flask_restplus import Resource, Namespace, fields
from flask import request

from ..service.kantung_parkir_service import get_all_kantung_parkir,get_kantung_parkir_byID,save_new_kantung_parkir

api = Namespace('parkir', description='Endpoints API untuk kantung parkir')
tempat_parkir = api.model('parkir', {
    'kode': fields.String(description='Kode tempat parkir'),
    'nama': fields.String(required=True, description='Nama tempat parkir'),
    'alamat':fields.String(required=True, description='Alamat tempat parkir'),
    'kapasitas':fields.Integer(required=True, description='Jumlah kapasistas tempat parkir')
})


@api.route('/')
class KantungParkirList(Resource):
    @api.doc('Daftar keseluruhan tempat parkir')
    @api.marshal_list_with(tempat_parkir,envelope='data')
    def get(self):
        return get_all_kantung_parkir()
    
    @api.response(201, 'Tempat parkir berhasil ditambahkan')
    @api.doc('Menambahkan tempat parkir baru')
    @api.expect(tempat_parkir, validate=True)
    def post(self):
        data = request.json
        return save_new_kantung_parkir(data)


@api.route('/<kode>')
@api.param('kode','Kode tempat parkir')
@api.response(404, 'Tempat parkir tidak ada')
class Parkir(Resource):
    @api.doc('ambil data tempat parkir')
    @api.marshal_with(tempat_parkir)
    def get(self,kode):
        parkir = get_kantung_parkir_byID(kode)
        if not parkir:
            api.abort(404)
        else:
            return parkir