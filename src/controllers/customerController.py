from src.models.customerModel import customerModel
from src.entities.responseEntity import responseEntity
from src.controllers.responseController import responseController
from src.entities.customerEntity import customerEntity

class customerController(responseController):

    def get_customers(self):
        _message = None
        _status = self.interruption
        _data= None
        try:
            _model = customerModel()
            _data = _model.get_customers()
            print(_data)
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
            print('error: '+ str(e))
        return responseEntity(_status,_message,_data).toJSON()

    def add_customer(self,request):
        _message = None
        _status = self.interruption
        _data= None
        try:
            print(1)
            _entity = customerEntity()
            _entity.requestToClass(request)
            print(_entity)
            _model = customerModel()
            _data = _model.add_customer(_entity)
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
        return responseEntity(_status,_message,_data).toJSON()

    def update_customer(self,request):
        _message = None
        _status = self.interruption
        _data= None
        try:
            print(1)
            _entity = customerEntity()
            _entity.requestToClass(request)
            print(_entity)
            _model = customerModel()
            _data = _model.update_customer(_entity)
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
        return responseEntity(_status,_message,_data).toJSON()

    def delete_customer(self,index):
        return ''