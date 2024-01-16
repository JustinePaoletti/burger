import flet as ft

def Product(mange, prix, page):

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)


    def minus_click(e): 
        if txt_number.value == "0":
            page.update()
        else :
            txt_number.value = str(int(txt_number.value) - 1) 
            page.update()
            

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    
    

    return(ft.Row(
        [
            ft.Text(mange, size = 25),
            ft.Text(prix, size = 20),
            txt_number,
            ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    )
