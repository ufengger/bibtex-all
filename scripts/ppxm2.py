import os
import fitz
from pdfCropMargins import crop

filename = '~/Sync/sci-tech/Boyd_convex_2004.pdf'
outname = 'boyd_ch1_bipa.pdf'

chap_start = 81
chap_end = 90

# intermediate
locfile = 'haha.pdf'
xmpdf = 'xm.pdf'
xmcpdf = 'xmc.pdf'

cmd = 'cp ' + filename + ' ' + locfile
os.system(cmd)
doc = fitz.open(locfile)

doc.delete_pages(chap_end, -1)
doc.delete_pages(0, chap_start - 2)

# repeat every page two times
for origin_pagenum in range(len(doc)):
    pagenum = origin_pagenum * 2
    doc.fullcopy_page(pagenum, pagenum)

doc.save(xmpdf)
doc.close()

# crop each page
crop(["-b", "c", "-ap", "30", "-p", "5", xmpdf, "-o", xmcpdf])

xmdoc = fitz.open(xmpdf)
xmcdoc = fitz.open(xmcpdf)

for pagenum in range(0, len(xmdoc), 2):
    xmpage = xmdoc.load_page(pagenum)
    X0 = xmpage.cropbox.x0
    Y0 = xmpage.cropbox.y0
    X1 = xmpage.cropbox.x1
    Y1 = xmpage.cropbox.y1
    xmcpage = xmcdoc.load_page(pagenum)
    x0 = xmcpage.cropbox.x0
    y0 = xmcpage.cropbox.y0
    x1 = xmcpage.cropbox.x1
    y1 = xmcpage.cropbox.y1

    width = x1 - x0
    height = y1 - y0

    if height <= (1.4 * width):
        # upper part
        R = fitz.Rect(x0, y0, x1, y0 + 0.75 * width)
        print("height less than 1.5w")
        print(pagenum)
        xmpage.set_cropbox(R)

        # bottom part
        xmpage = xmdoc.load_page(pagenum + 1)
        R = fitz.Rect(x0, y1 - 0.75 * width, x1, y1)
        print("height less than 1.5w")
        print(pagenum+1)
        xmpage.set_cropbox(R)
    else:
        # upper part
        R = fitz.Rect(x0, y0, x0 + 0.55 * 4 / 3 * height, y0 + 0.55 * height)
        print("height greater than 1.5w")
        print(pagenum)
        xmpage.set_cropbox(R)

        # bottom part
        xmpage = xmdoc.load_page(pagenum + 1)
        R = fitz.Rect(x0, y1 - 0.55 * height, x0 + 0.55 * 4 / 3 * height, y1)
        print("height greater than 1.5w")
        print(pagenum+1)
        xmpage.set_cropbox(R)

xmdoc.save(outname)
xmdoc.close()

cmd = 'rm ' + xmpdf + ' ' + xmcpdf + ' ' + locfile
os.system(cmd)
