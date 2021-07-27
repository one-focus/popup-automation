values = {'generated_email':'asdfasdf_email', 'order_id': '1558'}
query = 'Ваш заказ order_id'

for value in values:
    if value in query:
        query = query.replace(value, values[value])

