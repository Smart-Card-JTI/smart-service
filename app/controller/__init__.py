from flask import Blueprint
from flask_restplus import Api, Resource, fields


#import namsespace
from .kantung_parkir_controller import api as kantung_parkir_ns
from .data_kartu_controller import api as data_kartu
from .mahasiswa_controler import api as data_mahasiswa
controller = Blueprint('api',__name__,url_prefix='/api/v1')
api = Api(controller, version='1.0', title='Smart-Parking API', description='API Smart-Parking')

api.add_namespace(kantung_parkir_ns,path='/data/parkir')
api.add_namespace(data_kartu,path='/data/kartu')
api.add_namespace(data_mahasiswa,path='/data/mahasiswa')