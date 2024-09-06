from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import View
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class GeneratePdf:
     def open_pdf(self,proveedores):


        pdf_filename = "archivo_ejemplo.pdf"
        self.generar_pdf(pdf_filename, proveedores)
        with open(pdf_filename, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="' + pdf_filename + '"'
        return response

     def generar_pdf(self, nombre_archivo, proveedores):
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        width, height = letter

        text = c.beginText(100, height - 100)
        text.setFont("Helvetica", 20)


        for idx, proveedor in enumerate(proveedores):
            if idx % 2 == 0:  # Cada vez que el índice es par, agregamos una nueva página
                if idx > 0:
                    c.showPage()  # Mostrar la página actual antes de agregar una nueva

            # Posición Y del primer elemento de cada proveedor
            pos_y = height - 50 - (idx % 2) * 400

            c.drawString(100, pos_y-20, f"Proveedor: {proveedor['nombre']}")
            c.drawString(420, pos_y - 20, f"fecha: {proveedor['fecha']}")
            c.drawString(420, pos_y- 40, f"fecha final: {proveedor['fecha_final']}")
            c.drawString(100, pos_y - 40, f"Factura: {proveedor['factura']}")
            c.drawString(100, pos_y - 60, f"Litros: {proveedor['litros']}")
            c.drawString(190, pos_y - 60, f"ruta: {proveedor['ruta']}")

            c.drawString(420, pos_y - 180, f"Valor litro: {proveedor['valor_litro']}")
            c.drawString(420, pos_y - 230, f"adelantos: {proveedor['adelantos']}")
            c.drawString(420, pos_y - 250, f"valor total pagar: {proveedor['valor_total_pagar']}")
            c.drawString(420, pos_y - 200, f"Valor a pagar: {proveedor['Total_pagar']}")
            c.drawString(420, pos_y - 220, f"deuda: {proveedor['deuda']}")

            max_width = 500  # Ancho máximo del rectángulo
            num_columns = 16 # Número de columnas que deseas mostrar
            max_dia_length = max([len(str(d)) for d in proveedor['dia']])
            max_dia_leche_length = max([len(str(l)) for l in proveedor['dia_leche']])

            # Calcular el ancho máximo para cada columna
            max_column_width = max_width / (max_dia_length + max_dia_leche_length + 6)

            # Definir las posiciones iniciales
            dia_pos_x = 100
            dia_pos_y = pos_y - 90

            # Dibujar los valores de "dia" y "dia_leche" en columnas
            for i in range(len(proveedor['dia'])):
                dia_text = f"Día {proveedor['dia'][i]}:"
                dia_leche_text = f"{proveedor['dia_leche'][i]} litros"
                combined_text = f"{dia_text:<{max_dia_length + 2}} {dia_leche_text:<{max_dia_leche_length}}"

                # Calcular la posición X para cada columna
                column_x = dia_pos_x + (i % 2) * (max_column_width * (max_dia_length + 1))

                # Calcular la posición Y para cada fila
                if i % num_columns == 0 and i > 0:
                    dia_pos_y -= 20

                c.drawString(column_x, dia_pos_y - ((i // 2) * 20), combined_text)

            # Agregar un rectángulo transparente en blanco para cada proveedor
            rect_x = 30  # Posición X del rectángulo (ligeramente más a la izquierda que el texto)
            rect_y = pos_y - 300 # Posición Y del rectángulo
            rect_width = 550  # Ancho del rectángulo
            rect_height = 340  # Altura del rectángulo
            c.rect(rect_x, rect_y, rect_width, rect_height, fill=0)  # fill=1 para rellenar el rectángulo

            #image_path = "Apps/base/static/img/avatar.png"

            #c.drawImage(image_path, rect_x, rect_y, width=rect_width, height=rect_height, mask='auto')


        # Agregar una nueva página si el número total de proveedores es impar
        if len(proveedores) % 2 != 0:
            c.showPage()

        c.save()

     def open_pdf_trasporte(self,proveedores):


        pdf_filename = "archivo_ejemplo.pdf"
        self.generar_pdf_trasporte(pdf_filename, proveedores)
        with open(pdf_filename, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="' + pdf_filename + '"'
        return response

     def generar_pdf_trasporte(self, nombre_archivo, proveedores):
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        width, height = letter

        text = c.beginText(100, height - 100)
        text.setFont("Helvetica", 20)


        for idx, proveedor in enumerate(proveedores):
            if idx % 2 == 0:  # Cada vez que el índice es par, agregamos una nueva página
                if idx > 0:
                    c.showPage()  # Mostrar la página actual antes de agregar una nueva

            # Posición Y del primer elemento de cada proveedor
            pos_y = height - 50 - (idx % 2) * 400

            c.drawString(100, pos_y-20, f"Proveedor: {proveedor['nombre']}")
            c.drawString(300, pos_y-20, f"Fecha: {proveedor['fecha incio']}")
            c.drawString(400, pos_y-20, f"-{proveedor['fecha final']}")


            c.drawString(100, pos_y - 40, f"Factura: {proveedor['factura']}")

            c.drawString(190, pos_y - 60, f"ruta: {proveedor['ruta']}")
            c.drawString(190, pos_y - 100, f"Valor por litro: {proveedor['Valor por litro']}")
            c.drawString(190, pos_y - 130, f"Total de litros trasportados: {proveedor['Total de litros trasportados']}")
            c.drawString(190, pos_y - 150, f"litros que no llegaron: {proveedor['litros que no llegaron']}")
            c.drawString(350, pos_y - 150, f"Valor litro provedor: {proveedor['Valor litro provedor']}")
            c.drawString(190, pos_y - 250, f"total ha pagar: {proveedor['total ha pagar']}")
            c.drawString(190, pos_y - 200, f"total a pagar sin adelantos: {proveedor['total a pagar sin adelantos']}")
            c.drawString(190, pos_y - 190, f"adelantos: {proveedor['adelantos']}")

            dia_pos_x = 70
            dia_pos_y = pos_y - 100


            for dia, total_litros in enumerate(proveedor["litros_por_dia"], start=1):
                dia_text = f"Día {dia}:"
                litros_text = f"{total_litros} litros"
                combined_text = f"{dia_text:<10} {litros_text}"

                # Incrementar la posición Y para cada nuevo día
                dia_pos_y -= 20

                # Dibujar el texto en el lienzo del PDF
                c.drawString(dia_pos_x, dia_pos_y, combined_text)







            # Agregar un rectángulo transparente en blanco para cada proveedor
            rect_x = 30  # Posición X del rectángulo (ligeramente más a la izquierda que el texto)
            rect_y = pos_y - 300 # Posición Y del rectángulo
            rect_width = 550  # Ancho del rectángulo
            rect_height = 340  # Altura del rectángulo
            c.rect(rect_x, rect_y, rect_width, rect_height, fill=0)  # fill=1 para rellenar el rectángulo

            #image_path = "Apps/base/static/img/avatar.png"

            #c.drawImage(image_path, rect_x, rect_y, width=rect_width, height=rect_height, mask='auto')


        # Agregar una nueva página si el número total de proveedores es impar
        if len(proveedores) % 2 != 0:
            c.showPage()

        c.save()
