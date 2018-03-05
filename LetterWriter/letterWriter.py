# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:42:36 2018

@author: rjr
"""

# Creating a PDF writer
# FPDF Docs: https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
from tkinter import *
from tkinter import StringVar
from fpdf import FPDF
import uuid
import datetime
import os
import os.path as op
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
from email import encoders

def retrieveInput(string=""):
    if string == "Standard":
        # Creating unique identifier for the letter for tracking/accounting
        # And setting up the datetime for the letter header
        uniqueLetterID = str(uuid.uuid4())
        dt = str(datetime.datetime.now().date())
        fileFormat = ".pdf"
        uniqueLetterFormat = uniqueLetterID + fileFormat
        
        global filename
        filename = uniqueLetterFormat
        # Creating the PDF
        pdf = FPDF()
        pdf.add_page()
        
        headers = ["Powerful Python", "A Python Productivity Blog", 
                   "555 Fake Street", "Wilmington, DE", "555-555-5555",
                   "PowerfulPython@fakeaddress.com"]
        
        
        # Header Section
        # This is more direct than the fpdf header/footer class, because
        # that class has to be overridden, this is more explict/readable
        # fpdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
        # fpdf.line(x1, y1, x2, y2)
        pdf.set_font("Arial", "B", 16)
        pdf.set_x(180)
        pdf.image("pythonLogo.png", w = 20, h = 25, type = "PNG")
        pdf.set_x(0)
        pdf.set_y(0)
        pdf.cell(40, 10, headers[0], 0, 2, "L")
        pdf.set_font("Arial", "", 16)
        
        pdf.cell(40, 10, headers[1], 0, 2, "L")
        pdf.cell(40, 10, headers[2], 0, 2, "L")
        pdf.cell(90, 10, headers[3], 0, 2, "L") 
        pdf.cell(100, 10, headers[4], 0, 2, "L")
        pdf.cell(40, 10, dt, 0, 2, "L")    
        pdf.line(10,70,190,70)
    
        # Main Body Section
        pdf.set_font("Arial", "", 16)
        inputValue = textArea.get("1.0", "end-1c")
        pdf.cell(40, 10, " ", 0, 2, "L")
        pdf.multi_cell(180, 10, inputValue)
        
        # Salutation/signoff
        pdf.set_y(250)
        pdf.cell(40, 5, "Regards,", 0, 2, "L")
        pdf.cell(40, 5, "The powerful Python Team", 0, 2, "L")
        
        # Footer Section
        pdf.line(10,270,190,270)
        
        # Output all of the above to PDF
        pdf.output(uniqueLetterFormat, "f")
        
        return uniqueLetterFormat
    else:
        # Creating unique identifier for the letter for tracking/accounting
        # And setting up the datetime for the letter header
        uniqueLetterID = str(uuid.uuid4())
        dt = str(datetime.datetime.now().date())
        fileFormat = ".pdf"
        uniqueLetterFormat = uniqueLetterID + fileFormat
        
        filename = uniqueLetterFormat
        # Creating the PDF
        pdf = FPDF()
        pdf.add_page()
        
        headers = ["Powerful Python", "A Python Productivity Blog", 
                   "555 Fake Street", "Wilmington, DE 66604", "555-555-5555",
                   "PowerfulPython@fakeaddress.com"]
        
        
        # Header Section
        # This is more direct than the fpdf header/footer class, because
        # that class has to be overridden, this is more explict/readable
        # fpdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
        # fpdf.line(x1, y1, x2, y2)
        pdf.set_font("Arial", "B", 16)
        pdf.set_x(180)
        pdf.image("pythonLogo.png", w = 20, h = 25, type = "PNG")
        pdf.set_x(0)
        pdf.set_y(0)
        pdf.cell(40, 10, headers[0], 0, 2, "L")
        pdf.set_font("Arial", "", 16)
        # pdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
        
        pdf.cell(40, 10, headers[1], 0, 2, "L")
        pdf.cell(40, 10, headers[2], 0, 2, "L")
        pdf.cell(90, 10, headers[3], 0, 2, "L") 
        pdf.cell(100, 10, headers[4], 0, 2, "L")
        pdf.cell(40, 10, dt, 0, 2, "L")    
        pdf.line(10,70,190,70)
    
        # Main Body Section
        pdf.image("BillingInvoice.jpg",x = 50, y = 80, w = 100, h = 140, type = "JPG")
        
        # Salutation/signoff
        pdf.set_y(250)
        pdf.cell(40, 5, "Regards,", 0, 2, "L")
        pdf.cell(40, 5, "The powerful Python Team", 0, 2, "L")
        
        # Footer Section
        pdf.line(10,270,190,270)
        
        # Output all of the above to PDF
        pdf.output(uniqueLetterFormat, "f")
        
        return uniqueLetterFormat
    
def previewLetter():
    global path
    path  = filename
    os.startfile(path)
    
# Create a button for the forms that are generated
def letterOrEmailDropdownMenu(*args):
    
    if letterOrEmail.get() == "Email":

        top = Toplevel() 
        top.title("Enter Email Address")
        
        msg = Message(top, text="Email")
        
        emailField = Entry(top)            
        emailField.pack()
        
        confirmButton = Button(top, text = "Confirm input", command = lambda: getEmail(emailField))
        confirmButton.pack()
        
        msg.pack()
        
        
    else:
        top = Toplevel()
        top.title("Letter")
        msg = Message(top, text="Address Info")

        e = Entry(top)
        f = Entry(top)
        g = Entry(top)
        h = Entry(top)
        i = Entry(top)
        
        e.insert(END, "Address Field 1(Street address, P.O. Box, etc...")
        f.insert(END, "Address Field 2(APT #, etc...")
        g.insert(END, "City")
        h.insert(END, "State")
        i.insert(END, "ZIP")
        
        e.pack()
        f.pack()
        g.pack()
        h.pack()
        i.pack()
        confirmButton = Button(top, text = "Confirm input")
        confirmButton.pack()
        msg.pack()
        
        
def getEmail(email):
    global emailData
    emailData = email.get()

    
def letterFormatDropdownMenu(*args):
    if letterFormat.get() == "Billing Invoice":
        global billingInvoice
        billingInvoice = "Invoice"
        textArea.insert("1.0", """Billing invoice to be added/filled out upon preview""")
        retrieveInput("Invoice")
    elif letterFormat.get() == "Introduction":
        billingInvoice = "Standard"
        textArea.insert("1.0", """    On behalf of the entire Powerful Python staff, we'd like to take this opportunity to welcome you as a new customer. We are thrilled to have you with us.\n\n"""

"""    At Powerful Python, we pride ourselves on offering our customers responsive, competent, and excellent service. Our customers are the most important part of our business and we work tirelessly to ensure your complete satisfaction, now and for as long as you are a customer.\n\n"""

"""    Thank you again for entrusting Powerful Python with your most important business needs. We are happy to be at your service.\n\n""")
    else:
        textArea.insert("1.0", """As this is a custom letter, fill it out as is appropriate""")
        billingInvoice = "Standard"
        
def sendLetterOrEmail(*args):
    if letterOrEmail.get() == "Email":
        # Setting to/from and subject
        fromaddy = "WHERE THE EMAIL WILL BE SENT FROM(EMAIL ADDRESS)"
        toaddy = "WHERE THE EMAIL WILL BE SENT TO(EMAIL ADDRESS)"
                
        msg = MIMEMultipart()
        msg["From"] = fromaddy
        msg["To"] = toaddy
        msg["Subject"] = "An email from Powerful Python"
        
        
        text = MIMEText("""Please see the attached PDF.
                        
        
Thank you for your business!""")
        
        
        part = MIMEBase("application", "octet-stream")
        with open(path, "rb") as file:
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", 'attachement; filename="{}"'.format(op.basename(path)))
            msg.attach(part)
        
        msg.attach(text)
                
        # Mail send
        mailer = smtplib.SMTP("smtp.gmail.com:587")
        mailer.ehlo()
        mailer.starttls()
        mailer.login("INSERT LOGIN USERNAME HERE", "INSERT LOGIN PASSWORD HERE")
        mailer.sendmail(msg['From'], msg['To'], msg.as_string())
        mailer.quit()
        
        top = Toplevel()
        
        top.title("Email Sent!")
        
        notification = Message(top, text="Email Sent!")
        notification.pack()
    else:
        top = Toplevel()
        
        top.title("Letter Sent!")
        
        msg = Message(top, text="Letter Sent!")
        msg.pack()
        
# Creating the general Tkinter window and text area
root = Tk()
root.minsize(20, 20)
title = root.title("Letter/Email Generation Tool")

textArea = Text(root, height=25, width=170)

# Letter or Email choice/dropdown menu
letterOrEmail = StringVar(root)
letterOrEmail.set("Make a selection(Letter/Email)") # default value
dropdown1 = OptionMenu(root, letterOrEmail, "Email", "Letter")
z = letterOrEmail.trace("w", letterOrEmailDropdownMenu)

# What type of letter will be sent out choice/dropdown menu
letterFormat = StringVar(root)
letterFormat.set("Make a selection(Letter format)") # default value
dropdown2 = OptionMenu(root, letterFormat, "Introduction", "Billing Invoice",
                       "Custom")
x = letterFormat.trace("w", letterFormatDropdownMenu)

# Preview letter button
previewButton = Button(root, height = 3, width = 10, text = "Preview", 
                       command = lambda: previewLetter())

# Creating the letter/email
copyButton = Button(root, height = 3, width = 10, text = "Generate letter/email",
                    command = lambda: retrieveInput(billingInvoice))

sendButton = Button(root, height = 3, width = 10, text = "Send letter/email",
                    command = lambda: sendLetterOrEmail(letterOrEmailDropdownMenu))

# Generating the buttons/window and sizing the window so that buttons 
# don't dissapear 
root.update()
dropdown1.pack(side="top", fill="both", expand=True, padx=2, pady=2)
dropdown2.pack(side="top", fill="both", expand=True, padx=2, pady=2)


textArea.pack()
sendButton.pack(side="bottom", fill="both", expand=True, padx=2, pady=2)
copyButton.pack(side="bottom", fill="both", expand=True, padx=2, pady=2)
previewButton.pack(side="bottom", fill="both", expand=True, padx=2, pady=2)

root.geometry()
root.update()
root.geometry() 
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()


