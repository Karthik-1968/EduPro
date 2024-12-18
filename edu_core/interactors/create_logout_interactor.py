from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
import uuid
from ib_users.interfaces.service_interface import ServiceInterface

class LogoutInteractor:
    """
    ELP:
        -logout the user
    """

    def __init__(self,presenter:PresenterInterface):
        self.presenter=presenter

    def logout(self,user_id:uuid):
        service_interface = ServiceInterface()
        service_interface.logout_in_all_devices(user_id)
        return self.presenter.get_logout_response()
