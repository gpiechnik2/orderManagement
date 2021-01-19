from rest_framework import serializers
from .models import Product, Contractor, Order

class OrderSpecifiedNIPSerializer(serializers.Serializer):
    nip = serializers.CharField()

class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = [
            'id',
            'name',
            'nip',
            'address',
        ]

class ProductSerializer(serializers.ModelSerializer):

    order_id = serializers.RelatedField(source = 'order', queryset = Order.objects.all(), required = False)
    full_price = serializers.DecimalField(read_only = True, max_digits = 30, decimal_places = 2)
    price = serializers.DecimalField(max_digits = 30, decimal_places = 2)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'quantity',
            'price',
            'full_price',
            'order_id',
            'product_id',
            'full_price',
        ]

    def validate_quantity(self, validated_data):

        if validated_data <= 0:
            raise serializers.ValidationError('Quantity must be greater than zero.')

        return validated_data

class OrderSerializer(serializers.ModelSerializer):

    contractor_id = ContractorSerializer(many = False)
    implementation_date = serializers.DateTimeField(format = '%d-%m-%Y %H:%M', input_formats = ['%d-%m-%Y %H:%M'])
    data_of_placing_the_order = serializers.DateTimeField(format = '%d-%m-%Y %H:%M', input_formats = ['%d-%m-%Y %H:%M'])
    products = ProductSerializer(many = True)
    order_value = serializers.DecimalField(read_only = True, max_digits = 30, decimal_places = 2)

    class Meta:
        model = Order
        fields = [
            'id',
            'contractor_id',
            'implementation_date',
            'data_of_placing_the_order',
            'status',
            'products',
            'order_value',
        ]

    def create(self, validated_data):

        #get products values, and remove them from validated_data
        products = validated_data.pop('products')

        #order_value
        order_value = 0
        for product in products:
            full_price = product['price'] * product['quantity']
            order_value += full_price

        #check if contractor exists, if not, create new
        contractor_info = validated_data.pop('contractor_id')
        contractor_qr = Contractor.objects.filter(**contractor_info)

        if not contractor_qr:
            contractor = Contractor.objects.create(**contractor_info)
        else:
            contractor = Contractor.objects.filter(**contractor_info)[0]

        #create new order
        new_order = Order.objects.create(**validated_data, order_value = order_value, contractor_id = contractor)

        #add all the products to database
        for product in products:

            #check if product already exists in the database, if exists, change quantity of it
            product_query = Product.objects.filter(
                product_id = product['product_id'],
                price = product['price'],
                name = product['name'],
                order_id = new_order)

            if product_query:
                product_query[0].quantity += product['quantity']
                product_query[0].full_price += product['price'] * product['quantity']
                product_query[0].save()
            else:
                full_price = product['price'] * product['quantity']
                Product.objects.create(**product, full_price = full_price, order_id = new_order)

        return new_order

    def update(self, instance, validated_data):

        #get products values, and remove them from validated_data
        products = validated_data.pop('products')

        #order_value
        order_value = 0
        for product in products:
            full_price = product['price'] * product['quantity']
            order_value += full_price

        #remove old data
        Product.objects.filter(order_id = instance).delete()

        #check if contractor exists, if not, create new and change current
        contractor_info = validated_data.pop('contractor_id')
        contractor_qr = Contractor.objects.filter(**contractor_info)

        if not contractor_qr:
            instance.contractor_id = Contractor.objects.create(**contractor_info)
        else:
            instance.contractor_id = Contractor.objects.filter(**contractor_info)[0]

        #add all the products to database
        for product in products:

            #check if product already exists in the database, if exists, change quantity of it
            product_query = Product.objects.filter(
                product_id = product['product_id'],
                price = product['price'],
                name = product['name'],
                order_id = instance)

            if product_query:
                product_query[0].quantity += product['quantity']
                product_query[0].full_price += product['price'] * product['quantity']
                product_query[0].save()
            else:
                full_price = product['price'] * product['quantity']
                Product.objects.create(**product, full_price = full_price, order_id = instance)

        #update another info
        instance.implementation_date = validated_data.get('implementation_date', instance.implementation_date)
        instance.data_of_placing_the_order = validated_data.get('data_of_placing_the_order', instance.data_of_placing_the_order)
        instance.status = validated_data.get('status', instance.status)
        instance.order_value = order_value

        #save new info
        instance.save()

        return instance

    def validate_order_value(self, validated_data):

        if validated_data <= 0:
            raise serializers.ValidationError('Order value must be greater than zero.')

        return validated_data
