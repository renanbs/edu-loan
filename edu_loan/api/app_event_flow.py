from http import HTTPStatus

from flask import Blueprint, request

from injector import inject

from edu_loan.config.dependencies import Application
from edu_loan.domain.event_flow_service import EventFlowService, EventFlowServiceException
from edu_loan.domain.serializers import SerializerException, EventFlowSerializer


class EventFlowEndpoint:

    @inject
    def __init__(self, app: Application, event_flow_service: EventFlowService):
        self.app = app
        self.event_flow_service = event_flow_service

    def register_endpoints(self):
        app_bp = Blueprint('EventFlowApp', __name__)

        @self.app.route('/api/v1/event-flow', methods=['POST'])
        def add_event_flow():
            try:
                serializer = EventFlowSerializer().load(data=request.get_json())

                self.event_flow_service.add_event_flow(serializer.get('event_flow'))
            except (EventFlowServiceException, SerializerException) as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

            return {'success': True}, HTTPStatus.CREATED

        return app_bp
