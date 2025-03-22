
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import response, request, HttpResponse
from .models import Sale, Return
from .serializers import SaleSerializer



# générer un reçu de paiement après chaque vente sous format pdf

def generate_facture(sale_id):
    sale= Sale.objects.get(id=sale_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachement; filename="facture.pdf"'
    
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response, pagesize=letter)
    p.setTitle("MURDOC SALES")
    # fontfamily
    p.setFont(psfontname='Helvetica', size=12)
    p.setFillColorRGB(r=0.2, g=0.2, b=0.2)
    p.setDash([1, 1], 0)    
    # titre du ticket
    p.drawString(x=100.0, y=750.0, text="FACTURE D'ACHAT")
    p.drawString(100.0, 730.0, f"Employéé : {sale.employee.username}")
    p.drawString(100, 710, f"Date :{sale.date_sales.strftime("%d%m%Y")}")
    
    # tableau pour le produit
    p.drawString(100, 700, "Article")
    p.drawString(300, 700, "Quantité")
    p.drawString(400, 700, "Prix unitaire")
    p.drawString(310, 600, "Total") 
    
    # les produits vendus  
    y = 400
    product= sale.product
    
    p.drawString(100, y, product.name)
    p.drawString(250, y, str(sale.quantity_sales))
    p.drawString(350, y, f"{product.price_unit} FCFA")
    p.drawString(450,y, f"{sale.total_sales}FCFA")
    
    # decalage
    y -=30
    
    p.drawString(100, y, "Total")
    p.drawString(350, y, f"{sale.total_sales }FCFA")
    
    p.showPage()
    p.save()
    return response