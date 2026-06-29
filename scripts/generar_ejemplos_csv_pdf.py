"""
Genera archivos .csv y .pdf de ejemplo para los libros de Excel
(basico, intermedio, avanzado) siguiendo el patrón de codigo_de_olas.
"""

import csv, os
from pathlib import Path
from fpdf import FPDF

BASE = Path(r"C:\Users\alexg\OneDrive\Alex_2026\libros epub")

FONT_DIR = r"C:\Windows\Fonts"


def write_csv(path, headers, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(rows)
    print(f"  CSV {path.name}")


# ── PDF helper ────────────────────────────────────────────────────────
class SimplePDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 8, "Mendoza & Hijos - Carpinteria Fina", align="L")

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Pagina {self.page_no()}/{{nb}}", align="C")


def write_pdf(path, title, lines):
    path.parent.mkdir(parents=True, exist_ok=True)
    pdf = SimplePDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 15, title, ln=True, align="C")
    pdf.ln(5)
    pdf.set_font("Helvetica", "", 11)
    for line in lines:
        pdf.cell(0, 7, line, ln=True)
    pdf.output(str(path))
    print(f"  PDF {path.name}")


# ═══════════════════════════════════════════════════════════════════════
#  EXCEL BASICO
# ═══════════════════════════════════════════════════════════════════════
BASICO = BASE / "excel_basico" / "codigos"
INTER = BASE / "excel_intermedio" / "codigos"
AVANZ = BASE / "excel_avanzado" / "codigos"

def basico_csv():
    # inventario.csv
    write_csv(BASICO / "inventario.csv",
        ["Producto", "Cantidad", "Unidad", "Precio Unit.", "Proveedor"],
        [
            ["Madera Cedro", 50, "tablas", 45.00, "Maderas Perez"],
            ["Madera Roble", 30, "tablas", 62.00, "Maderas Perez"],
            ["Madera Pino", 100, "tablas", 22.00, "El Maderero"],
            ["Triplay", 40, "planchas", 35.00, "Maderas Perez"],
            ["Barniz mate", 10, "galones", 28.00, "Pinturas Unidas"],
            ["Tornillos #10", 500, "unidades", 0.50, "Ferreteria El Tornillo"],
            ["Lija fina", 200, "hojas", 1.20, "Ferreteria El Tornillo"],
        ])

    # ventas.csv
    write_csv(BASICO / "ventas.csv",
        ["Fecha", "Producto", "Cliente", "Cantidad", "P.Unit", "Total"],
        [
            ["01/06/2026", "Silla cedro", "Sr. Garcia", 2, 150, 300],
            ["02/06/2026", "Mesa roble", "Sra. Lopez", 1, 350, 350],
            ["03/06/2026", "Estante triplay", "Hotel Miraflores", 5, 180, 900],
            ["05/06/2026", "Silla cedro", "Rest. El Buen Sabor", 4, 150, 600],
            ["07/06/2026", "Cama queen", "Sra. Maria", 1, 450, 450],
            ["10/06/2026", "Mesa roble", "Colegio San Jose", 3, 350, 1050],
            ["12/06/2026", "Ropero", "Sr. Gomez", 1, 890, 890],
            ["15/06/2026", "Sillón", "Sra. Fernanda", 2, 520, 1040],
        ])

    # catalogo.csv
    write_csv(BASICO / "catalogo.csv",
        ["Codigo", "Producto", "Precio", "Calidad", "Categoria"],
        [
            ["CAT-001", "Banquito", 80, "B", "Accesorios"],
            ["CAT-002", "Cama king", 680, "A", "Dormitorio"],
            ["CAT-003", "Cama queen", 450, "A", "Dormitorio"],
            ["CAT-004", "Comoda", 420, "A", "Dormitorio"],
            ["CAT-005", "Escritorio", 280, "B", "Sala"],
            ["CAT-006", "Estante", 180, "C", "Sala"],
            ["CAT-007", "Mesa centro", 250, "B", "Sala"],
            ["CAT-008", "Mesa noche", 120, "B", "Dormitorio"],
            ["CAT-009", "Mesa comedor", 520, "A", "Comedor"],
            ["CAT-010", "Ropero", 890, "A", "Dormitorio"],
        ])


def basico_pdf():
    # presupuesto_ejemplo.pdf
    write_pdf(BASICO / "presupuesto_ejemplo.pdf",
        "PRESUPUESTO - Mendoza & Hijos",
        [
            "",
            "Cliente: Sra. Maria Fernanda",
            "Fecha: 15/06/2026",
            "Validez: 15 dias",
            "",
            "-" * 50,
            "  Codigo  |  Producto         |  Cant.  |  P.Unit  |  Total",
            "-" * 50,
            "  DORM-01 | Cama king cedro   |    2    | S/ 680   | S/ 1,224",
            "  DORM-02 | Mesa de noche     |    4    | S/ 120   | S/   432",
            "  DORM-03 | Comoda            |    2    | S/ 420   | S/   756",
            "  SALA-01 | Sillon            |    3    | S/ 520   | S/ 1,482",
            "  COMED-01| Mesa comedor      |    1    | S/ 520   | S/   520",
            "  COMED-02| Silla comedor     |    8    | S/ 150   | S/ 1,200",
            "-" * 50,
            "                           TOTAL GENERAL: S/ 5,614.00",
            "",
            "Nota: Incluye IGV. Descuentos aplicados por volumen.",
        ])

    # informe_mensual.pdf
    write_pdf(BASICO / "informe_mensual.pdf",
        "INFORME MENSUAL - Junio 2026",
        [
            "",
            "RESUMEN EJECUTIVO",
            "-" * 40,
            "Ventas del mes:      S/ 28,450.00",
            "Costos totales:      S/ 18,200.00",
            "Ganancia neta:       S/ 10,250.00",
            "Margen:              36.0%",
            "Pedidos pendientes:  8",
            "Clientes activos:    12",
            "",
            "PRODUCTO MAS VENDIDO: Silla cedro (S/ 7,800 en el semestre)",
            "",
            "TENDENCIA: Crecimiento sostenido del 13.8% vs. meta mensual.",
        ])


# ═══════════════════════════════════════════════════════════════════════
#  EXCEL INTERMEDIO
# ═══════════════════════════════════════════════════════════════════════
def intermedio_csv():
    # transacciones.csv
    write_csv(INTER / "transacciones.csv",
        ["Fecha", "Producto", "Categoria", "Cantidad", "Venta", "Cliente"],
        [
            ["01/01/2026", "Silla cedro", "Comedor", 2, 300, "Sr. Garcia"],
            ["03/01/2026", "Mesa roble", "Comedor", 1, 350, "Hotel Lima"],
            ["05/01/2026", "Estante triplay", "Sala", 3, 540, "Sra. Lopez"],
            ["08/01/2026", "Cama queen", "Dormitorio", 2, 900, "Clinica San Pablo"],
            ["10/01/2026", "Ropero", "Dormitorio", 1, 890, "Sr. Gomez"],
            ["12/01/2026", "Banquito pino", "Accesorios", 6, 480, "Restaurante"],
            ["15/01/2026", "Silla cedro", "Comedor", 4, 600, "Hotel Miraflores"],
            ["18/01/2026", "Mesa centro", "Sala", 2, 500, "Sra. Maria"],
            ["20/01/2026", "Escritorio", "Sala", 1, 280, "Oficina Legal"],
            ["22/01/2026", "Comoda", "Dormitorio", 1, 420, "Sra. Fernanda"],
            ["25/01/2026", "Sillón", "Sala", 2, 1040, "Hotel Lima"],
            ["28/01/2026", "Cama king", "Dormitorio", 1, 680, "Clinica San Pablo"],
            ["30/01/2026", "Mesa comedor", "Comedor", 1, 520, "Restaurante"],
        ])

    # clientes.csv
    write_csv(INTER / "clientes.csv",
        ["Nombre", "Email", "Telefono", "Ciudad", "Tipo"],
        [
            ["Sofia Mendoza", "sofia.mendoza@email.com", "999-888-777", "Lima", "VIP"],
            ["Carlos Perez", "carlos.perez@email.com", "999-888-776", "Lima", "Regular"],
            ["SOFIA MENDOZA", "sofia.mendoza@email.com", "999-888-777", "LIMA", "VIP"],
            ["Maria Garcia", "maria.garcia@email.com", "999-888-775", "Arequipa", "Regular"],
            ["Pedro Huaman", "pedro.h@email.com", "999-888-774", "Cusco", "Regular"],
            ["sofia mendoza", "sofia.mendoza@email.com", "999-888-777", "lima", "VIP"],
            ["Ana Torres", "ana.torres@email.com", "999-888-773", "Lima", "VIP"],
            ["Luis Vega", "luis.vega@email.com", "999-888-772", "Trujillo", "Regular"],
        ])

    # productos.csv
    write_csv(INTER / "productos.csv",
        ["ID", "Producto", "Precio", "Categoria", "Stock Min", "Stock Actual"],
        [
            [101, "Silla cedro", 150, "Comedor", 10, 25],
            [102, "Mesa roble", 350, "Comedor", 5, 12],
            [103, "Banquito pino", 80, "Accesorios", 15, 40],
            [104, "Estante triplay", 180, "Sala", 8, 18],
            [105, "Cama queen", 450, "Dormitorio", 3, 8],
            [106, "Ropero", 890, "Dormitorio", 2, 5],
            [107, "Cama king", 680, "Dormitorio", 2, 4],
            [108, "Mesa centro", 250, "Sala", 5, 10],
            [109, "Sillón", 520, "Sala", 3, 7],
            [110, "Comoda", 420, "Dormitorio", 3, 6],
        ])

    # ventas_mensuales.csv
    write_csv(INTER / "ventas_mensuales.csv",
        ["Mes", "Silla", "Mesa", "Estante", "Ropero", "Total"],
        [
            ["Ene", 1200, 800, 450, 600, 3050],
            ["Feb", 1350, 750, 500, 580, 3180],
            ["Mar", 1100, 900, 480, 620, 3100],
            ["Abr", 1400, 850, 520, 640, 3410],
            ["May", 1300, 780, 490, 590, 3160],
            ["Jun", 1450, 920, 510, 610, 3490],
        ])


def intermedio_pdf():
    write_pdf(INTER / "dashboard_ejemplo.pdf",
        "DASHBOARD - Mendoza & Hijos",
        [
            "",
            "INDICADORES CLAVE (KPIs) - Junio 2026",
            "-" * 45,
            "Ventas totales:         S/ 28,450",
            "Costo total:            S/ 18,200",
            "Ganancia neta:          S/ 10,250",
            "Margen:                 36.0%",
            "Pedidos pendientes:     8",
            "Clientes nuevos mes:    3",
            "Satisfaccion:           4.8 / 5.0",
            "",
            "ANALISIS DE VENTAS",
            "-" * 45,
            "Silla:    S/ 7,800  (40%)  << Producto estrella",
            "Mesa:     S/ 5,000  (26%)",
            "Ropero:   S/ 3,640  (19%)",
            "Estante:  S/ 2,950  (15%)",
            "",
            "TENDENCIA: Crecimiento sostenido ultimos 3 meses.",
            "RIESGO: Dependencia excesiva en sillas (40% de ventas).",
        ])


# ═══════════════════════════════════════════════════════════════════════
#  EXCEL AVANZADO
# ═══════════════════════════════════════════════════════════════════════
def avanzado_csv():
    # datos_bancarios.csv
    write_csv(AVANZ / "datos_bancarios.csv",
        ["Fecha", "Cuenta", "Descripcion", "Monto", "Tipo", "Saldo"],
        [
            ["01/01/2026", "Cta. 1001", "Deposito nomina", 5000, "Ingreso", 15000],
            ["03/01/2026", "Cta. 1001", "Retiro ATM", -500, "Egreso", 14500],
            ["05/01/2026", "Cta. 1002", "Transferencia recibida", 3000, "Ingreso", 8000],
            ["07/01/2026", "Cta. 1001", "Pago electricidad", -250, "Egreso", 14250],
            ["10/01/2026", "Cta. 1002", "Deposito efectivo", 2000, "Ingreso", 10000],
            ["12/01/2026", "Cta. 1001", "Compra supermercado", -180, "Egreso", 14070],
            ["15/01/2026", "Cta. 1003", "Transferencia saliente", -1000, "Egreso", 5000],
            ["20/01/2026", "Cta. 1001", "Deposito cliente", 4500, "Ingreso", 18570],
            ["25/01/2026", "Cta. 1002", "Pago servicio", -320, "Egreso", 9680],
        ])

    # transacciones_historicas.csv
    write_csv(AVANZ / "transacciones_historicas.csv",
        ["TransID", "Fecha", "Producto", "Cantidad", "Precio", "ClienteID", "Sucursal"],
        [
            [10001, "05/01/2025", "Silla cedro", 10, 150, "C001", "Lima Centro"],
            [10002, "05/01/2025", "Mesa roble", 3, 350, "C002", "Lima Centro"],
            [10003, "12/01/2025", "Cama queen", 5, 450, "C003", "Miraflores"],
            [10004, "20/01/2025", "Estante triplay", 8, 180, "C001", "Lima Centro"],
            [10005, "03/02/2025", "Silla cedro", 15, 150, "C004", "San Isidro"],
            [10006, "10/02/2025", "Ropero", 2, 890, "C003", "Miraflores"],
            [10007, "15/02/2025", "Mesa roble", 5, 350, "C005", "Lima Centro"],
            [10008, "01/03/2025", "Sillón", 3, 520, "C002", "Miraflores"],
            [10009, "10/03/2025", "Cama king", 2, 680, "C004", "San Isidro"],
            [10010, "22/03/2025", "Silla cedro", 20, 150, "C005", "Lima Centro"],
        ])

    # ventas_por_canal.csv
    write_csv(AVANZ / "ventas_por_canal.csv",
        ["Anio", "Trimestre", "Producto", "Canal", "Ventas"],
        [
            [2025, "Q1", "Silla cedro", "Online", 35000],
            [2025, "Q1", "Mesa roble", "Online", 28000],
            [2025, "Q2", "Silla cedro", "Tienda", 42000],
            [2025, "Q2", "Mesa roble", "Online", 31000],
            [2025, "Q3", "Silla cedro", "Tienda", 38000],
            [2025, "Q3", "Mesa roble", "Tienda", 29000],
            [2025, "Q4", "Silla cedro", "Online", 45000],
            [2025, "Q4", "Mesa roble", "Tienda", 33000],
            [2026, "Q1", "Silla cedro", "Online", 48000],
            [2026, "Q1", "Mesa roble", "Online", 35000],
            [2026, "Q2", "Silla cedro", "Tienda", 52000],
            [2026, "Q2", "Mesa roble", "Tienda", 37000],
        ])


def avanzado_pdf():
    write_pdf(AVANZ / "analisis_financiero.pdf",
        "ANALISIS FINANCIERO - Power BI",
        [
            "",
            "RESUMEN EJECUTIVO - Primer Semestre 2026",
            "-" * 45,
            "Ingresos totales:       S/ 284,500",
            "Costo de ventas:        S/ 182,000",
            "Ganancia bruta:         S/ 102,500",
            "Margen bruto:           36.0%",
            "Gastos operativos:      S/  45,000",
            "Ganancia neta:          S/  57,500",
            "Margen neto:            20.2%",
            "",
            "COMPARATIVA vs 2025",
            "-" * 45,
            "Crecimiento ingresos:   +15.3%",
            "Crecimiento clientes:   +22.0%",
            "Reduccion costos:        -3.2%",
            "",
            "CANALES DE VENTA",
            "-" * 45,
            "Tienda fisica:          52%  (S/ 148,500)",
            "Online:                 48%  (S/ 136,000)",
            "",
            "PRODUCTO ESTRELLA: Silla cedro (38% de ingresos totales)",
        ])

    write_pdf(AVANZ / "dashboard_ejecutivo.pdf",
        "DASHBOARD EJECUTIVO",
        [
            "",
            "PANEL DE CONTROL - Mendoza & Hijos",
            "-" * 45,
            "",
            "KPI                        VALOR        META",
            "-" * 45,
            "Ingresos                 S/ 284,500   S/ 250,000",
            "Costos                   S/ 182,000   S/ 175,000",
            "Margen %                      36%          30%",
            "Clientes activos               48           40",
            "Pedidos pendientes              8            5",
            "Satisfaccion (1-5)             4.8          4.5",
            "",
            "PRINCIPALES HALLAZGOS",
            "-" * 45,
            "1. Crecimiento sostenido en ingresos (15.3% YoY)",
            "2. Producto estrella: Silla cedro (38% de ventas)",
            "3. Canal online creciendo, ya representa 48%",
            "4. Oportunidad: reducir dependencia en sillas",
            "5. Riesgo: costos de materia prima subiendo 5% anual",
        ])


# ═══════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════

def main():
    print("=== excel_basico ===")
    basico_csv()
    basico_pdf()

    print("\n=== excel_intermedio ===")
    intermedio_csv()
    intermedio_pdf()

    print("\n=== excel_avanzado ===")
    avanzado_csv()
    avanzado_pdf()

    print("\nOK - Todos los archivos CSV y PDF generados.")


if __name__ == "__main__":
    main()
