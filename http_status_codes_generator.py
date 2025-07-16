
from fpdf import FPDF

class PDFWithColors(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Códigos de Estado HTTP/1.1", ln=True, align='C')
        self.ln(5)

    def add_table_header(self, headers, col_widths):
        self.set_font("Arial", "B", 12)
        self.set_fill_color(200, 220, 255)
        for i in range(len(headers)):
            self.cell(col_widths[i], 10, headers[i], border=1, align='C', fill=True)
        self.ln()

pdf = PDFWithColors()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

headers = ["Código", "Nombre", "Notas"]
col_widths = [30, 60, 90]

color_map = {
    "1": (200, 230, 255),
    "2": (220, 255, 220),
    "3": (255, 255, 200),
    "4": (255, 230, 200),
    "5": (255, 200, 200),
}

data = [
    ("100", "Continuar", "Todo va bien, continúa."),
    ("101", "Cambio de protocolos", "Se está cambiando de protocolo."),
    ("200", "OK", "Todo está bien."),
    ("201", "Creado", "Se ha creado un nuevo recurso."),
    ("202", "Aceptado", "La solicitud ha sido aceptada para su procesamiento."),
    ("203", "Información no autoritativa", "Información devuelta, pero de una fuente no original."),
    ("204", "Sin contenido", "Éxito, pero sin datos que devolver."),
    ("205", "Restablecer contenido", "Restablece la vista del formulario que envió datos."),
    ("206", "Contenido parcial", "Solo se está devolviendo parte del recurso solicitado."),
    ("300", "Múltiples opciones", "Hay varias respuestas posibles."),
    ("301", "Movido permanentemente", "Actualiza tu URL, el recurso se ha movido para siempre."),
    ("302", "Encontrado", "Redirección temporal."),
    ("303", "Ver otro", "Usa otra URL para obtener el recurso."),
    ("304", "No modificado", "El recurso no ha cambiado desde la última solicitud."),
    ("305", "Usar proxy", "El recurso debe accederse a través de un proxy."),
    ("306", "No usado", "Código reservado, ya no se usa."),
    ("307", "Redirección temporal", "Redirección temporal, no actualices tus marcadores."),
    ("400", "Solicitud incorrecta", "El servidor no entendió la solicitud enviada."),
    ("401", "No autorizado", "Debes estar autenticado."),
    ("402", "Pago requerido", "(Reservado para uso futuro)."),
    ("403", "Prohibido", "El servidor rechaza entregarte el recurso, incluso autenticado."),
    ("404", "No encontrado", "El recurso solicitado no existe en esa dirección."),
    ("405", "Método no permitido", "El método usado no está permitido para ese recurso."),
    ("406", "No aceptable", "El recurso no puede generar contenido aceptable."),
    ("407", "Requiere autenticación proxy", "Se necesita autenticarse con el proxy."),
    ("408", "Tiempo de espera agotado", "El navegador tardó demasiado en enviar la solicitud."),
    ("409", "Conflicto", "Hay un conflicto con el estado actual del recurso."),
    ("410", "Eliminado", "El recurso fue eliminado permanentemente."),
    ("411", "Longitud requerida", "Falta especificar la longitud de la solicitud."),
    ("412", "Falló la precondición", "Alguna condición previa no se cumplió."),
    ("413", "Entidad de solicitud muy grande", "La solicitud es demasiado grande para ser procesada."),
    ("414", "URI demasiado largo", "La URL es demasiado larga."),
    ("415", "Tipo de medio no soportado", "El formato del archivo no es soportado por el servidor."),
    ("416", "Rango no satisfactorio", "El rango solicitado no puede ser satisfecho."),
    ("417", "Falló la expectativa", "El servidor no puede cumplir con los requisitos del encabezado."),
    ("500", "Error interno del servidor", "Algo en el servidor falló."),
    ("501", "No implementado", "El servidor no reconoce o no puede cumplir la solicitud."),
    ("502", "Puerta de enlace incorrecta", "Error al recibir una respuesta válida del servidor upstream."),
    ("503", "Servicio no disponible", "El servidor está ocupado o en mantenimiento."),
    ("504", "Tiempo de espera de la puerta de enlace", "El servidor gateway no recibió respuesta a tiempo."),
    ("505", "Versión HTTP no soportada", "El servidor no soporta la versión HTTP usada.")
]

pdf.add_table_header(headers, col_widths)
pdf.set_font("Arial", size=12)
for row in data:
    first_digit = row[0][0]
    color = color_map.get(first_digit, (255, 255, 255))
    pdf.set_fill_color(*color)
    pdf.cell(col_widths[0], 10, row[0], border=1, align='C', fill=True)
    pdf.cell(col_widths[1], 10, row[1], border=1, align='L', fill=True)
    pdf.cell(col_widths[2], 10, row[2], border=1, align='L', fill=True)
    pdf.ln()

pdf.output("HTTP_status_codes_colored.pdf")
