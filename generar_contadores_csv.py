#!/usr/bin/env python3
"""
Genera archivos .csv y .pdf de ejemplo para excel_contadores
"""

from pathlib import Path
import csv, random

BASE = Path(r"C:\Users\alexg\OneDrive\Alex_2026\libros epub")
DEST = BASE / "excel_contadores" / "codigos"
DEST.mkdir(parents=True, exist_ok=True)

# CSV 1: Catalogo de Cuentas completo
def csv_catalogo():
    path = DEST / "catalogo_pcge.csv"
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["Codigo", "Descripcion", "Nivel", "Tipo", "Grupo"])
        cuentas = [
            ["1", "Activo", 1, "Activo", "Balance"],
            ["1.1", "Activo Corriente", 2, "Activo", "Balance"],
            ["1.1.1", "Efectivo y Equivalentes", 3, "Activo", "Balance"],
            ["1.1.1.1", "Caja", 4, "Activo", "Balance"],
            ["1.1.1.1.01", "Caja General Soles", 5, "Activo", "Balance"],
            ["1.1.1.1.02", "Caja General Dolares", 5, "Activo", "Balance"],
            ["1.1.1.2", "Banco", 4, "Activo", "Balance"],
            ["1.1.1.2.01", "BCP Cta Cte Soles", 5, "Activo", "Balance"],
            ["1.1.1.2.02", "Scotiabank Cta Cte Dolares", 5, "Activo", "Balance"],
            ["1.1.2", "Inversiones Financieras", 3, "Activo", "Balance"],
            ["1.1.3", "Cuentas por Cobrar", 3, "Activo", "Balance"],
            ["1.1.3.1", "Facturas por Cobrar", 4, "Activo", "Balance"],
            ["1.1.3.2", "Letras por Cobrar", 4, "Activo", "Balance"],
            ["1.1.4", "Existencias", 3, "Activo", "Balance"],
            ["1.1.4.1", "Mercaderias", 4, "Activo", "Balance"],
            ["1.1.4.1.01", "Mercaderias Manufacturadas", 5, "Activo", "Balance"],
            ["1.1.4.1.02", "Mercaderias en Transito", 5, "Activo", "Balance"],
            ["1.1.4.2", "Materias Primas", 4, "Activo", "Balance"],
            ["1.2", "Activo No Corriente", 2, "Activo", "Balance"],
            ["1.2.1", "Inmuebles", 3, "Activo", "Balance"],
            ["1.2.1.1", "Terrenos", 4, "Activo", "Balance"],
            ["1.2.1.2", "Edificios", 4, "Activo", "Balance"],
            ["1.2.2", "Maquinaria y Equipo", 3, "Activo", "Balance"],
            ["1.2.3", "Depreciacion Acumulada", 3, "Activo", "Balance"],
            ["2", "Pasivo", 1, "Pasivo", "Balance"],
            ["2.1", "Pasivo Corriente", 2, "Pasivo", "Balance"],
            ["2.1.1", "Proveedores", 3, "Pasivo", "Balance"],
            ["2.1.2", "Tributos por Pagar", 3, "Pasivo", "Balance"],
            ["2.1.3", "Remuneraciones por Pagar", 3, "Pasivo", "Balance"],
            ["2.1.4", "Prestamos Bancarios CP", 3, "Pasivo", "Balance"],
            ["2.2", "Pasivo No Corriente", 2, "Pasivo", "Balance"],
            ["2.2.1", "Prestamos Bancarios LP", 3, "Pasivo", "Balance"],
            ["3", "Patrimonio", 1, "Patrimonio", "Balance"],
            ["3.1", "Capital", 2, "Patrimonio", "Balance"],
            ["3.1.1", "Capital Social", 3, "Patrimonio", "Balance"],
            ["3.2", "Reservas", 2, "Patrimonio", "Balance"],
            ["3.2.1", "Reserva Legal", 3, "Patrimonio", "Balance"],
            ["3.3", "Resultados", 2, "Patrimonio", "Balance"],
            ["3.3.1", "Resultados Acumulados", 3, "Patrimonio", "Balance"],
            ["3.3.2", "Resultado del Ejercicio", 3, "Patrimonio", "Balance"],
            ["4", "Ingresos", 1, "Ingreso", "PyG"],
            ["4.1", "Ventas", 2, "Ingreso", "PyG"],
            ["4.1.1", "Ventas Mercaderias", 3, "Ingreso", "PyG"],
            ["4.1.2", "Prestacion Servicios", 3, "Ingreso", "PyG"],
            ["4.2", "Otros Ingresos", 2, "Ingreso", "PyG"],
            ["5", "Gastos", 1, "Gasto", "PyG"],
            ["5.1", "Gastos Operativos", 2, "Gasto", "PyG"],
            ["5.1.1", "Compras", 3, "Gasto", "PyG"],
            ["5.1.2", "Servicios Publicos", 3, "Gasto", "PyG"],
            ["5.2", "Gastos Administrativos", 2, "Gasto", "PyG"],
            ["5.2.1", "Sueldos y Salarios", 3, "Gasto", "PyG"],
            ["5.2.2", "Alquileres", 3, "Gasto", "PyG"],
            ["5.3", "Gastos Financieros", 2, "Gasto", "PyG"],
            ["5.3.1", "Intereses Prestamos", 3, "Gasto", "PyG"],
            ["6", "Costos", 1, "Gasto", "PyG"],
            ["6.1", "Costo de Ventas", 2, "Gasto", "PyG"],
            ["6.1.1", "Costo Mercaderias Vendidas", 3, "Gasto", "PyG"],
        ]
        w.writerows(cuentas)
    print(f"  OK {path.name}")


# CSV 2: Transacciones mensuales
def csv_transacciones():
    path = DEST / "transacciones_mensuales.csv"
    cuentas = [
        "10.01.01.01", "10.01.02.01", "12.01.01.01", "14.01.01.01",
        "20.01.02.01", "40.01.01.01", "40.01.03.01", "42.01.01.01",
        "60.01.01.01", "70.01.01.01", "80.01.01.01", "80.01.02.01"
    ]
    glosas = [
        "Venta al contado", "Compra mercaderias", "Pago proveedor",
        "Cobranza factura", "Pago sueldos", "Pago alquiler",
        "Deposito bancario", "Transferencia", "Pago servicios",
        "Venta al credito", "Depreciacion mensual", "Pago tributos"
    ]
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["Fecha", "Comprobante", "Glosa", "Cuenta", "Debe", "Haber"])
        random.seed(2025)
        for i in range(1, 201):
            fecha = f"{random.randint(1,28):02d}/{random.randint(1,12):02d}/2025"
            comp = f"CP-{i:04d}"
            glosa = random.choice(glosas)
            cuenta = random.choice(cuentas)
            debe = round(random.uniform(100, 50000), 2)
            haber = round(random.uniform(100, 50000), 2)
            if random.random() < 0.5:
                debe, haber = 0, debe
            else:
                debe, haber = haber, 0
            w.writerow([fecha, comp, glosa, cuenta, debe, haber])
    print(f"  OK {path.name}")


# CSV 3: Proveedores
def csv_proveedores():
    path = DEST / "proveedores.csv"
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["RUC", "Razon Social", "Direccion", "Telefono", "Email", "Plazo Credito"])
        proveedores = [
            ["20123456789", "Maderas Perez S.A.C.", "Av. Industrial 450, Lima", "999-111-222", "ventas@maderasperez.pe", 30],
            ["20134567890", "Pinturas Unidas S.A.", "Jr. Colores 123, Lima", "999-222-333", "info@pinturasunidas.pe", 15],
            ["20145678901", "Ferreteria El Tornillo E.I.R.L.", "Calle Hierro 55, Arequipa", "999-333-444", "tornillo@ferreteria.pe", 7],
            ["20156789012", "Logistica Total S.A.C.", "Av. Transporte 789, Callao", "999-444-555", "ops@logisticatotal.pe", 30],
            ["20167890123", "Pacifico Seguros S.A.", "Av. La Paz 200, Lima", "999-555-666", "reclamos@pacifico.pe", 15],
            ["20178901234", "Luz del Sur S.A.A.", "Av. Electricidad 500, Lima", "999-666-777", "facturacion@luzdelsur.pe", 7],
            ["20189012345", "Sedapal S.A.", "Jr. Agua 300, Lima", "999-777-888", "comercial@sedapal.pe", 7],
            ["20190123456", "Interbank S.A.", "Av. Finanzas 100, Lima", "999-888-999", "empresas@interbank.pe", 0],
            ["20201234567", "Agencia Creativa S.A.C.", "Av. Publicidad 250, Lima", "999-999-000", "contacto@agenciacreativa.pe", 15],
            ["20212345678", "SUNAT", "Av. Tributos 1, Lima", "0-800-1-0100", "mesadepartes@sunat.gob.pe", 0],
        ]
        w.writerows(proveedores)
    print(f"  OK {path.name}")


# CSV 4: Tipos de cambio
def csv_tc():
    path = DEST / "tipos_cambio.csv"
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["Fecha", "USD", "EUR"])
        from datetime import datetime, timedelta
        d = datetime(2025, 1, 2)
        end = datetime(2025, 12, 31)
        while d <= end:
            if d.weekday() < 5:
                usd = round(3.75 + random.uniform(-0.05, 0.05), 3)
                eur = round(4.10 + random.uniform(-0.08, 0.08), 3)
                w.writerow([d.strftime("%d/%m/%Y"), usd, eur])
            d += timedelta(days=1)
    print(f"  OK {path.name}")


# CSV 5: Estados financieros ejemplo
def csv_eeff():
    path = DEST / "estados_financieros.csv"
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["Cuenta", "Tipo", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"])
        data = [
            ["Ventas Netas", "PyG", 180000, 195000, 172000, 210000, 225000, 198000],
            ["Costo Ventas", "PyG", -108000, -117000, -103200, -126000, -135000, -118800],
            ["Utilidad Bruta", "PyG", 72000, 78000, 68800, 84000, 90000, 79200],
            ["Gastos Operativos", "PyG", -28000, -30000, -26000, -32000, -34000, -29000],
            ["Gastos Admin", "PyG", -15000, -16000, -14000, -17000, -18000, -15500],
            ["Utilidad Operativa", "PyG", 29000, 32000, 28800, 35000, 38000, 34700],
            ["Gastos Financieros", "PyG", -3500, -3500, -3800, -3500, -4000, -3800],
            ["Utilidad Neta", "PyG", 25500, 28500, 25000, 31500, 34000, 30900],
            ["Activo Corriente", "Balance", 450000, 468000, 472000, 510000, 535000, 520000],
            ["Activo No Corriente", "Balance", 350000, 350000, 380000, 380000, 380000, 410000],
            ["Total Activo", "Balance", 800000, 818000, 852000, 890000, 915000, 930000],
            ["Pasivo Corriente", "Balance", 210000, 225000, 230000, 248000, 255000, 250000],
            ["Pasivo No Corriente", "Balance", 180000, 175000, 185000, 190000, 192000, 188000],
            ["Total Pasivo", "Balance", 390000, 400000, 415000, 438000, 447000, 438000],
            ["Patrimonio Neto", "Balance", 410000, 418000, 437000, 452000, 468000, 492000],
        ]
        w.writerows(data)
    print(f"  OK {path.name}")


def main():
    print("Generando CSV para excel_contadores...")
    csv_catalogo()
    csv_transacciones()
    csv_proveedores()
    csv_tc()
    csv_eeff()
    print(f"\nOK - Archivos CSV en: {DEST}")

if __name__ == "__main__":
    main()
