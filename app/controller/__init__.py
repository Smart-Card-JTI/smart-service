from flask import Blueprint
from flask_restplus import Api, Resource, fields


#import namsespace
from .kantung_parkir_controller import api as kantung_parkir_ns

controller = Blueprint('api',__name__,url_prefix='/api/v1')
api = Api(controller, version='1.0', title='Smart-Parking API', description='API Smart-Parking')

api.add_namespace(kantung_parkir_ns,path='/parkir')