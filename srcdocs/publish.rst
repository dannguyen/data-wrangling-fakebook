*****************************
Publishing into other formats
*****************************


PDF
===

- https://www.quora.com/How-to-create-a-PDF-out-of-Sphinx-documentation-tool

- https://github.com/rst2pdf/rst2pdf/issues

- http://rst2pdf.ralsina.me/handbook.html

- rst2pdf can only build on Python 2.x
- Edit conf.py to include:

    extensions = ['rst2pdf.pdfbuilder']

    pdf_documents = [('index',
        'output-docname',
        'Output Title',
        'Author Name'),]



