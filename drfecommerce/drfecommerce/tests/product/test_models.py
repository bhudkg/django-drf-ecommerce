import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        x = category_factory()

        assert x.__str__() == "test_category"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        x = brand_factory()
        assert x.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        x = product_factory()
        assert x.__str__() == "test_product"
