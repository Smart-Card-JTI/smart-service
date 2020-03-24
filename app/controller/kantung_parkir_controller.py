from flask_restplus import Resource, Namespace, fields
from werkzeug.exceptions import NotFound
from flask import request
import logging

#local import
from ..service.kantung_parkir_service import get_all_kantung_parkir,get_kantung_parkir_byID,save_new_kantung_parkir

LOG = logging.getLogger(__name__)

api = Namespace('parkir', description='Endpoints API untuk kantung parkir')
tempat_parkir = api.model('kantung_parkir', {
    'id': fields.String(readonly=True),
    'nama': fields.String(required=True, description='Nama tempat parkir'),
    'keterangan':fields.String(required=True, description='Alamat tempat parkir'),
    'kapasitas':fields.Integer(required=True, description='Jumlah kapasistas tempat parkir')
})


@api.route('/')
class KantungParkir(Resource):
    @api.doc(responses={200:'OK',500:'Internal Server Error'},description='Daftar Keseluruhan Tempat Parkir Di Polinema')
    @api.marshal_list_with(tempat_parkir,envelope='data')
    def get(self):
        try:
            LOG.info('Mengambil Data Parkir')
            return get_all_kantung_parkir()
        except Exception as e:
            LOG.error("Internal Server Error")
            api.abort(500,e.__doc__,status='Tidak dapat mengambil data')
    
    @api.doc(responses={200:'OK',400:'Bad Request'},description="Endpoint untuk menambahkan Kantung Parkir")
    @api.expect(tempat_parkir)
    def post(self):
        try:
            data = request.json
            status,message_object = save_new_kantung_parkir(data)
        except Exception as e:
            LOG.error('Gaga; menerima data dari client')
            api.abort(400,e.__doc__)
        else:
            if status:
                return message_object
            else:
                return message_object


@api.route('/<id>')
class ParkirByID(Resource):
    @api.doc(responses={200:'OK',404:'Not Found'},description="Mengambil data kantung parkir berdasarkan ID kantung parkir")
    @api.marshal_with(tempat_parkir)
    def get(self,id):
        data_by_id = get_kantung_parkir_byID(id)
        if not data_by_id:
            LOG.error("Data tidak ditemukan di databae")
            api.abort(404)
        else:
            return data_by_id