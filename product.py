import flet as ft

def Product(manger, prix, page):
        total = 0 
        txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)


        def minus_click(e): 
            nonlocal total
            if txt_number.value == "0":
                page.update()
            else :
                txt_number.value = str(int(txt_number.value) - 1) 
                total -= 1
                cout.value = str(total*prix)
                page.update()


        def plus_click(e):
            nonlocal total
            txt_number.value = str(int(txt_number.value) + 1)
            total += 1
            cout.value = str(total*prix)
            page.update()
        cout = ft.Text(total, total*prix)
        
        
        return(ft.Row(
            [
                ft.Text(manger, size = 25),
                ft.Text(prix, size = 20),
                cout,
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        )