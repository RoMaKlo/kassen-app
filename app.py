import os
import flet as ft

# Preise (in Cent)
PRICES = [600, 850, 350, 300, 250, 200, 1200]


def fmt_eur(c):
    return f"{c/100:.2f} €".replace(".", ",")


def main(page: ft.Page):
    page.title = "Kasse"
    page.padding = 10
    page.theme_mode = ft.ThemeMode.LIGHT

    counts = {p: 0 for p in PRICES}
    subtotal_labels = {}
    total_txt = ft.Text("Gesamt: 0,00 €", size=22, weight=ft.FontWeight.BOLD)

    # --- Berechnung ---
    def update_totals():
        for p in PRICES:
            subtotal = p * counts[p]
            subtotal_labels[p].value = fmt_eur(subtotal)
        total = sum(p * counts[p] for p in PRICES)
        total_txt.value = f"Gesamt: {fmt_eur(total)}"
        page.update()

    # --- Zeilen erzeugen ---
    def make_row(price):
        qty_lbl = ft.Text("0", width=40, text_align=ft.TextAlign.CENTER, size=18)
        subtotal_lbl = ft.Text(
            "0,00 €", width=90, text_align=ft.TextAlign.RIGHT, size=16
        )
        subtotal_labels[price] = subtotal_lbl

        def add(e):
            counts[price] += 1
            qty_lbl.value = str(counts[price])
            update_totals()

        def sub(e):
            if counts[price] > 0:
                counts[price] -= 1
                qty_lbl.value = str(counts[price])
                update_totals()

        return ft.Row(
            [
                ft.Text(fmt_eur(price), width=80, size=18, weight=ft.FontWeight.W_600),
                ft.IconButton(ft.Icons.REMOVE, on_click=sub, icon_color=ft.Colors.RED),
                qty_lbl,
                ft.IconButton(ft.Icons.ADD, on_click=add, icon_color=ft.Colors.GREEN),
                subtotal_lbl,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

    rows = [make_row(p) for p in PRICES]

    # --- Alles löschen ---
    def clear_all(e):
        for p in PRICES:
            counts[p] = 0
            subtotal_labels[p].value = "0,00 €"
        for r in rows:
            r.controls[2].value = "0"
        update_totals()

    clear_btn = ft.ElevatedButton("Alles löschen", on_click=clear_all)

    page.add(
        ft.Column(rows, spacing=10),
        ft.Divider(),
        ft.Row([clear_btn, total_txt], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
    )

    update_totals()


if __name__ == "__main__":
    port = int(os.getenv("FLET_SERVER_PORT", "8000"))
    ft.app(target=main, port=port)
