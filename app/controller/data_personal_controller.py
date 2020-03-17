from flask import request
from flask_restplus import Resource, Namespace, fields,inputs,reqparse


from ..service.data_persolan_service import get_all_data_personal,get_data_personal_byNim,save_new_data_personal,update_data_personal

api = Namespace('datapersonal', 'Endpoints API untuk data personal')
data_personal = api.model('datapersonal',{
    'nim_mahasiswa': fields.String(required=True,description='Nim mahasiswa'),
    'uid_kartu':fields.String(required=True, description='Uid dari kartu yang dimiliki mahasiswa'),
    'tanggal_perso': fields.Date(required=True, description='Coba date type string di convert'),
    'userid':fields.Integer(required=True, description='ID dari setiap user')
})

parser = reqparse.RequestParser()
parser.add_argument('nim_mahasiswa', type=str, required=True)

@api.route('/')
class DataPersonalList(Resource):
    @api.doc('Daftar Keseluruhan data personal')
    @api.marshal_list_with(data_personal,envelope='data')
    def get(self):
        return get_all_data_personal()

    @api.response(201,'Data personal berhasil ditambahkan')
    @api.doc('Menambahkan data personal')
    @api.expect(data_personal,validate=True)
    def post(self):
        data = request.json
        return save_new_data_personal(data)