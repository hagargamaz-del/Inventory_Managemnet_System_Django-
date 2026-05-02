import xml.etree.ElementTree as ET
from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'category']

    def to_xml(self, obj):
        root = ET.Element('response')
        for field_name, value in obj.__dict__.items():
            if not field_name.startswith('_'):
                child = ET.SubElement(root, field_name)
                child.text = str(value)
        return ET.tostring(root, encoding='utf-8', method='xml').decode()

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    staff = serializers.StringRelatedField()  # To serialize the User as a string (username)

    class Meta:
        model = Order
        fields = ['product', 'order_quantity', 'staff', 'date']

    def to_xml(self, obj):
        root = ET.Element('response')
        # Product details
        product = ET.SubElement(root, 'product')
        product_name = ET.SubElement(product, 'name')
        product_name.text = str(obj.product.name)
        product_quantity = ET.SubElement(product, 'quantity')
        product_quantity.text = str(obj.product.quantity)
        # Order details
        order_quantity = ET.SubElement(root, 'order_quantity')
        order_quantity.text = str(obj.order_quantity)
        staff = ET.SubElement(root, 'staff')
        staff.text = str(obj.staff.username if obj.staff else '')
        date = ET.SubElement(root, 'date')
        date.text = str(obj.date)
        return ET.tostring(root, encoding='utf-8', method='xml').decode()