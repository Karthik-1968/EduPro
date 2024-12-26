from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import MissingId,MissingLabel,MissingFieldType,FieldAlreadyExists
from type_form.interactors.storage_interfaces.storage_interface import Fielddto

class CreateFieldInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def create_field(self,form_id:int,label:str,field_type:str,is_required:bool):

        """
            ELP:
                check if input data exists
                check if form exists
                check if field exists
                add field to form
        """
        self.validate_input_data(label = label, field_type = field_type)

        try:
            self.storage.check_if_field_already_exists(label = label,field_type = field_type)
        except FieldAlreadyExists:
            self.presenter.raise_exception_for_field_already_exists()

        if is_required:
            fielddto = Fielddto(label = label,field_type = field_type,is_required = is_required)
        else:
            fielddto = Fielddto(label = label,field_type = field_type)

        field_id=self.storage.create_field(field_dto = field_dto)
        return self.presenter.get_response_for_create_field(id = field_id)

    def validate_input_data(self,label:str,field_type:str):

        try:
            self.storage.valid_label_field(label = label)
        except MissingLabel:
            self.presenter.raise_exception_for_missing_label()

        try:
            self.storage.valid_field_type_field(field_type = field_type)
        except MissingFieldType:
            self.presenter.raise_exception_for_missing_field_type()