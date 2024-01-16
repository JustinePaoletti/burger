import flet as ft 

class Item:
    def __init__(self, text, price):
        self.text = text
        self.price = price 

burger = Item(text = "🍔", price = 5.95)
fries = Item(text = "🍟", price = 3.60)
salad = Item(text = "🥗", price = 8.30)
drink = Item(text = "🍹", price = 2.60)

def main(page: ft.Page):
    page.title = "I Can Has Cheezburger ?"
    page.window_height = 430
    page.window_width = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def row(item):

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
        
        
        page.add(
            ft.Row(
                [
                    ft.Text(item.text, size = 25),
                    ft.Text(item.price, size = 20),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        
    
    row(burger)
    row(fries)
    row(salad)
    row(drink)
 


ft.app(target=main)
