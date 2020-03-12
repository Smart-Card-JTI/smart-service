from flask import Blueprint
from flask_restplus import Api, Resource, fields


#import namsespace
from .kantung_parkir_controller import api as kantung_parkir_ns
from .data_persolan_controller import api as data_personal_ns

controller = Blueprint('api',__name__,url_prefix='/api/v1')
api = Api(controller, version='1.0', title='Smart-Parking API', description='API Smart-Parking')

api.add_namespace(kantung_parkir_ns,path='/parkir')
api.add_namespace(data_personal_ns,path='/data')