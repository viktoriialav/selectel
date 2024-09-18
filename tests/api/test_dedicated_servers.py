from selectel_tests.schemas.price_plans import ListPricePlans
from selectel_tests.schemas.resource import ListResources, ResourceBillingInfo
from selectel_tests.schemas.resource_tag import ListResourceTags, ResourceTagRequestBody, DeletedResourceTag, \
    CreatedResourceTag, UpdatedResourceTag
from selectel_tests.schemas.service import ListServices, ServiceColocationUuidBillingRequestBody, \
    ServiceColocationUuidBillingModel
from selectel_tests.utils.format_view import json_dumping, bytes_to_dict


class TestResources:
    def test_get_resources(self, api_session):
        response = api_session.request(method='GET',
                                       endpoint='servers/v2/resource')
        print(json_dumping(response.json()))

        assert response.status_code == 200
        model = ListResources.model_validate(response.json())
        assert model.status == 'SUCCESS'
        assert model.result == []

    def test_get_resources_billing_info(self, api_session):
        response = api_session.request(method='GET',
                                       endpoint='servers/v2/resource/billing/info')

        assert response.status_code == 200
        model = ResourceBillingInfo.model_validate(response.json())
        assert model.result.unpaid_sum == 0


class TestResourceTags:
    def test_create_new_user_tag(self, api_session):
        name = 'Hasss12223'
        response = api_session.request(method='POST',
                                       endpoint='servers/v2/resource/tag',
                                       json={'name': name})

        assert response.status_code == 200
        model = CreatedResourceTag.model_validate(response.json())
        assert name == model.result.name
        ResourceTagRequestBody.model_validate(bytes_to_dict(response.request.body))

    def test_get_list_all_user_tags(self, api_session):
        response = api_session.request(method='GET',
                                       endpoint='servers/v2/resource/tag')

        assert response.status_code == 200
        ListResourceTags.model_validate(response.json())
        assert response.request.body is None

    def test_update_user_tag(self, api_session):
        response_to_find_uuid = api_session.request(method='GET',
                                                    endpoint='servers/v2/resource/tag')
        all_tags = response_to_find_uuid.json()['result']
        first_uuid = all_tags[0]['uuid']

        new_name = 'kuku'
        main_response = api_session.request(method='PUT',
                                            endpoint=f'servers/v2/resource/tag/{first_uuid}',
                                            json={'name': new_name})

        assert main_response.status_code == 200
        model = UpdatedResourceTag.model_validate(main_response.json())
        assert model.result.name == new_name
        ResourceTagRequestBody.model_validate(bytes_to_dict(main_response.request.body))

    def test_delete_user_tag(self, api_session):
        response = api_session.request(method='GET',
                                       endpoint='servers/v2/resource/tag')
        uuid = response.json()['result'][0]['uuid']
        response = api_session.request(method='DELETE',
                                       endpoint=f'servers/v2/resource/tag/{uuid}')

        assert response.status_code == 200
        assert response.request.body is None
        model = DeletedResourceTag.model_validate(response.json())
        assert uuid == model.result.uuid


class TestPricePlans:
    def test_get_price_all_price_plans_and_check_all_ones_are_different(self, api_session):
        response = api_session.request(method='GET', endpoint='servers/v2/plan')

        assert response.status_code == 200
        assert response.request.body is None
        model = ListPricePlans.model_validate(response.json())
        assert model.item_count == len(set(elem.name for elem in model.result))

    def test_get_special_price_plan(self, api_session):
        uuid = '74566568-dae2-48e4-97da-0b4a7ef7fff0'
        response = api_session.request(method='GET', endpoint=f'servers/v2/plan/{uuid}')

        assert response.status_code == 200
        assert response.request.body is None
        model = ListPricePlans.model_validate(response.json())
        assert model.result.period == 3 and model.result.type == 'month'


class TestServices:
    def test_get_all_services(self, api_session):
        response = api_session.request(method='GET', endpoint='servers/v2/service')

        print(json_dumping(response.json()))

        assert response.status_code == 200
        assert response.request.body is None
        ListServices.model_validate(response.json())

    def test_get_services_with_specific_model(self, api_session):
        param = 'model'
        model_name = 'firewall'
        response = api_session.request(method='GET', endpoint='servers/v2/service',
                                       params={param: model_name})

        assert response.status_code == 200
        assert response.request.body is None
        assert response.request.url.endswith(f'{param}={model_name}') is True
        model = ListServices.model_validate(response.json())
        assert sum(elem[param] == model_name for elem in response.json()['result']) == len(model.result)

    def test_get_services_colocation_uuid_billing(self, api_session):
        uuid = 'e44c8700-58bc-47aa-b8a7-75a69868e8a6'
        payload = {
            "location_uuid": "bf5647d4-e6b0-44a8-96d2-949ab0d50e30",
            "pay_day": 28,
            "price_plan_uuid": "74566568-dae2-48e4-97da-0b4a7ef7fff0",
            "quantity": 1
        }

        response = api_session.request(method='POST',
                                       endpoint=f'servers/v2/service/colocation/{uuid}/billing',
                                       json=payload)

        assert response.status_code == 200
        ServiceColocationUuidBillingRequestBody.model_validate(bytes_to_dict(response.request.body))
        model = ServiceColocationUuidBillingModel.model_validate(response.json())

        price_info = model.result.price
        period = model.result.current_price_plan.period
        assert int(price_info.plan_price // (100 - price_info.discount) * 100 // period) == 12800
