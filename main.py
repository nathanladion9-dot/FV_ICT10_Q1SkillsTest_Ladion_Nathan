from pyscript import display
from js import document

def create_order(e):
    document.getElementById("output2").innerHTML = ""
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
    subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked
    size = document.querySelector('input[name="size"]:checked')
    size_price = float(size.value)
    grand_total = subtotal + size_price
    display(grand_total, target="output2")