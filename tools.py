from functions import *

products_tools = [
    {
        "type": "function",
        "function": {
            "name": "product_list",
            "description": "Lista cierta cantidad de productos disponibles, ordenados alfabeticamente.",
            "parameters": {
                "type": "object",
                "properties": {
                    "quantity": {
                        "type": "string",
                        "description": "Número de productos a listar.",
                    },
                },
                "required": ["quantity"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "product_list_price",
            "description": "Lista cierta cantidad de productos disponibles, ordenados de mayor precio a menor precio.",
        },
    },
    {
        "type": "function",
        "function": {
            "name": "product_detail",
            "description": "Busca un producto por su nombre y muestra su información",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Nombre del producto a buscar",
                    },
                },
                "required": ["product_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "top_product",
            "description": "Consulta el producto más vendido en un rango de fechas.",
            "parameters": {
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "Fecha inicial del rango a consultar",
                    },
                    "end_date": {
                        "type": "string",
                        "description": "Fecha final del rango a consultar",
                    },
                },
                "required": ["start_date", "end_date"],
            },
        },
    },
]

user_tools = [
    *products_tools,
    { 
        "type": "function",
        "function": {
            "name": "devoluciones",
            "description": "Realiza la devolución de un pedido.",
            "parameters": {
                "type": "object",
                "properties": {
                    "pedido": {
                        "type": "string",
                        "description": "Nombre del pedido a devolver.",
                    },
                    "motivo": {
                        "type": "string",
                        "description": "Motivo de la devolución",
                        "enum": ["fallo", "no lo quiero"],
                    },
                },
                "required": ["pedido", "motivo"],
            },
        },
    },
    { 
        "type": "function",
        "function": {
            "name": "repuestos",
            "description": "Solicita repuesto para un producto.",
            "parameters": {
                "type": "object",
                "properties": {
                    "tipo_producto": {
                        "type": "string",
                        "description": "Tipo de producto del que se necesita repuesto",
                    },
                    "modelo": {
                        "type": "string",
                        "description": "modelo del producto que se necesita repuesto",
                    },
                },
                "required": ["modelo", "tipo_producto"],
            },
        },
    },
    { 
        "type": "function",
        "function": {
            "name": "compatibilidades",
            "description": "Consulta las compatibilidades de un producto",
            "parameters": {
                "type": "object",
                "properties": {
                    "tipo_producto": {
                        "type": "string",
                        "description": "Tipo de producto del que se necesita saber sus compatibilidades",
                    },
                    "producto": {
                        "type": "string",
                        "description": "Nombre del producto sobre el que se necesita saber sus compatibilidades",
                    },
                },
                "required": ["producto", "tipo_producto"],
            },
        },
    },
    { 
        "type": "function",
        "function": {
            "name": "software",
            "description": "Consulta los software de un producto",
            "parameters": {
                "type": "object",
                "properties": {
                    "tipo_producto": {
                        "type": "string",
                        "description": "Tipo de producto del que se necesita saber su software",
                    },
                    "producto": {
                        "type": "string",
                        "description": "Nombre del producto sobre el que se necesita saber su software",
                    },
                },
                "required": ["producto", "tipo_producto"],
            },
        },
    },
    { 
        "type": "function",
        "function": {
            "name": "sales_order",
            "description": "Consulta el estado, importe y fecha de un pedido.",
            "parameters": {
                "type": "object",
                "properties": {
                    "pedido": {
                        "type": "string",
                        "description": "Nombre del pedido",
                    },
                },
                "required": ["pedido"],
            },
        },
    },
    { 
        "type": "function",
        "function": {
            "name": "create_ticket",
            "description": "Crea un ticket de soporte en odoo que reporte alguna queja o sugerencia de un cliente.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nombre del ticket. No se le pregunta al usuario, se decide a interpretación del asistente",
                    },
                    "description": {
                        "type": "string",
                        "description": "Descripción del ticket",
                    },
                    "priority": {
                        "type": "string",
                        "description": "Nivel de prioridad del ticket. No se le pregunta al usuario, se decide a interpretación del asistente. Las prioridades son: 1-Alta, 2-Media, 3-Baja",
                        "enum": ["1", "2", "3"],
                    },
                    "email_cc": {
                        "type": "string",
                        "description": "email del cliente",
                    },
                    "closed_date": {
                        "type": "string",
                        "description": "Fecha límite para resolver el ticket",
                    },
                },
                "required": ["name", "description", "priority"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "clear_chat",
            "description": "Elimina el historial de la conversación y comienza una nueva.",
        },
    },
    {
        "type": "function",
        "function": {
            "name": "available_actions",
            "description": "Lista las acciones que puedes realizar.",
        },
    },
]

user_available_functions = {
    "sales_order": sales_order,
    "devoluciones": devoluciones,
    "repuestos": repuestos,
    "compatibilidades": compatibilidades,
    "software": software,
    #productos
    "product_list": product_list,
    "product_list_price": product_list_price,
    "product_detail": product_detail,
    "top_product": top_product,
    #extras
    "clear_chat": clear_chat,
    "available_actions": user_actions,
    "create_ticket": create_ticket,
}
