from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
import uuid
from type_form.exceptions.custom_exceptions MissingId,AlreadyAccepted,InvalidInvitation

class ActivateInvitationInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def activate_invitation(self,id:int):
        """
        ELP:
            check if input data exists
            check if invitation exists
            check if invitaion already accepted
            accept the invitation
        """
        try:
            self.storage.valid_id_field(id = id)
        except MissingId:
            self.presenter.raise_exception_for_missing_invite_id()

        try:
            self.storage.check_invitation(id = id)
        except InvalidInvitation:
            self.presenter.raise_exception_for_invalid_invite()

        try:
            self.storage.check_if_invitation_already_accepted(id = id)
        except AlreadyAccepted:
            self.presenter.raise_exception_for_invitation_already_accepted()

        self.storage.accept_invitation(id = id)
        return self.presenter.get_response_for_accept_invitation()