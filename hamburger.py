import flet as ft 
def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def minus_click_factory(txt_field):    
        def minus_click(e):
            txt_field.value = str(int(txt_field.value) - 1)
            page.update()
        return minus_click

    def plus_click_factory(txt_field) : 
        def plus_click(e):
            txt_field.value = str(int(txt_field.value) + 1)
            page.update()
        return plus_click

    for i in range(4) :
        txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)    
        page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click_factory(txt_number)),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click_factory(txt_number)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)


