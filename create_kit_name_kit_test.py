import sender_stand_request
"""
Prueba 1: Se asegura de que la peticion maneje correctamente un nombre con un solo carácter, resultado esperado:
Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

"""
def test_create_kit_1_letter_in_name_get_success_response():
    sender_stand_request.positive_assert("a")
"""
Prueba 2: Se asegura de que la peticion maneje correctamente un nombre con un solo carácter, resultado esperado:
Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud

"""
def test_create_kit_511_letters_in_name_get_success_response():
    sender_stand_request.positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
"""
Prueba 3: Se asegura de que la peticion maneje correctamente un nombre con un solo carácter, resultado esperado:
Código de respuesta: 400

"""
def test_create_kit_0_letters_in_name_get_negative_response():
    sender_stand_request.negative_assert("")
"""
Prueba 4: Se asegura de que la peticion maneje correctamente un nombre con un solo carácter, resultado esperado:
Código de respuesta: 400

"""
def test_create_kit_512_letters_in_name_get_negative_response():
    sender_stand_request.negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
"""
Prueba 5: Se asegura de que la peticion maneje correctamente un nombre con un solo carácter, resultado esperado:
Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

"""
def test_create_kit_with_special_characters():
    sender_stand_request.positive_assert('"№%@",')
"""
Prueba 6: Se asegura de que la peticion maneje correctamente un nombre con un solo carácter, resultado esperado:
Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

"""
def test_create_kit_with_spaces():
    sender_stand_request.positive_assert(" A Aaa")
"""
Prueba 7: Se asegura de que la peticion maneje correctamente un nombre con un solo carácter, resultado esperado:
Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

"""
def test_create_kit_with_numbers():
    sender_stand_request.positive_assert("123")
"""
Prueba 8: Se asegura de que la peticion maneje correctamente un nombre con un solo carácter, resultado esperado:
Código de respuesta: 400

"""

def test_create_kit_without_body():
    sender_stand_request.negative_assert_no_body()
"""
Prueba 9: Se asegura de que la peticion maneje correctamente un nombre con un solo carácter, resultado esperado:
Código de respuesta: 400

"""
def test_create_kit_with_different_data_type():
    sender_stand_request.negative_assert(123)
