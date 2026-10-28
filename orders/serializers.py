from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "product_name", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "username", "status", "shipping_address", "total", "items", "created_at"]
        read_only_fields = ["total"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        total = 0
        for item in items_data:
            product = item["product"]
            OrderItem.objects.create(order=order, **item)
            product.stock = product.stock - item["quantity"]
            product.save()
            total += item["price"] * item["quantity"]
        order.total = total
        order.save()
        return order
