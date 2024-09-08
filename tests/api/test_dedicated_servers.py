from selectel_tests.schemas.price_plans import ListPricePlans
from selectel_tests.schemas.resource import ListResources
from selectel_tests.utils.json_file import json_dumping


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
        print(json_dumping(response.json()))

        assert response.status_code == 200
        # model = ListResources.model_validate(response.json())
        # assert model.status == 'SUCCESS'
        # TODO check unpaid_sum

    def test_create_new_user_tag(self, api_session):
        response = api_session.request(method='POST',
                                       endpoint='servers/v2/resource/tag',
                                       json={'name': 'haha'})

        print(json_dumping(response.json()))
        assert response.status_code == 200
        # TODO add schema validation
        # TODO add checking smth in response

    def test_get_list_all_user_tags(self, api_session):
        response = api_session.request(method='GET',
                                       endpoint='servers/v2/resource/tag')

        print(json_dumping(response.json()))
        assert response.status_code == 200
        # TODO add schema validation
        # TODO add checking smth in response

    def test_update_user_tag(self, api_session):
        response = api_session.request(method='GET',
                                       endpoint='servers/v2/resource/tag')
        uuid = response.json()['result'][0]['uuid']
        # TODO Do smth with method or payload
        response = api_session.request(method='PUT',
                                       endpoint=f'servers/v2/resource/tag/{uuid}',
                                       json={'name': 'kuku'})

        print(json_dumping(response.json()))
        assert response.status_code == 200
        # TODO add schema validation
        # TODO add checking smth in response

    def test_delete_user_tag(self, api_session):
        response = api_session.request(method='GET',
                                       endpoint='servers/v2/resource/tag')
        uuid = response.json()['result'][0]['uuid']
        response = api_session.request(method='DELETE',
                                       endpoint=f'servers/v2/resource/tag/{uuid}')

        print(json_dumping(response.json()))
        assert response.status_code == 200
        # TODO add schema validation
        # TODO add checking smth in response


class TestPricePlans:
    def test_get_price_all_price_plans_and_check_all_ones_are_different(self, api_session):
        response = api_session.request(method='GET', endpoint='servers/v2/plan')

        assert response.status_code == 200
        model = ListPricePlans.model_validate(response.json())
        assert model.item_count == len(set(elem.name for elem in model.result))

    def test_get_special_price_plan(self, api_session):
        uuid = '74566568-dae2-48e4-97da-0b4a7ef7fff0'
        response = api_session.request(method='GET', endpoint=f'servers/v2/plan/{uuid}')

        assert response.status_code == 200
        model = ListPricePlans.model_validate(response.json())
        assert model.result.period == 3 and model.result.type == 'month'


class TestServices:
    def test_get_services(self, api_session):
        params = {
            'model': 'firewall'
                  }
        response = api_session.request(method='GET', endpoint='servers/v2/service',
                                       params=params)

        print(json_dumping(response.json()))

        assert response.status_code == 200
        # TODO add schema validation
        # TODO add checking smth in response

    def test_get_services_colocation_uuid(self, api_session):
        uuid = 'e44c8700-58bc-47aa-b8a7-75a69868e8a6'
        response = api_session.request(method='GET',
                                       endpoint=f'servers/v2/service/colocation/{uuid}')

        print(json_dumping(response.json()))

        assert response.status_code == 200
        # TODO add schema validation
        # TODO add checking smth in response

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
        # TODO: Add model validate for payload and for response
        price_info = response.json()['result']['price']
        period = response.json()['result']['current_price_plan']['period']
        assert int(price_info['plan_price'] // (100 - price_info['discount']) * 100 // period) == 12800

