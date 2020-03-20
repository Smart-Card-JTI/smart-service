from flask import request
from flask_restplus import Resource,Namespace,fields

from ..service.mahasiswa_service import get_mhs_byNim

api = Namespace('datamahasiswa','Endpoint untuk mengambil data mahasiswa')
data_mhs = api.model('datamahasiswa',{
    'nim': fields.String(readonly=True),
    'nama': fields.String(readonly=True),
    'prodi': fields.String(readonly=True),
    'jurusan': fields.String(readonly=True),
    'email': fields.String(readonly=True),
    'hp': fields.String(readonly=True),
})

@api.route('/<nim>')
@api.param('nim','NIM mahasiswa yang akan di ambil datanya')
@api.response(404,'NIM Tidak ditemukan')
class Mahasiswa_By_NIM(Resource):
    @api.doc('Mengambil data mahasiswa berdasarkan NIM')
    @api.marshal_with(data_mhs)
    def get(self,nim):
        data_mahasiswa = get_mhs_byNim(nim)
        if not data_mahasiswa:
            api.abort(404)
        else:
            return data_mahasiswa