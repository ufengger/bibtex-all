import os
import fitz
from pdfCropMargins import crop

filename = '~/Sync/sci-tech/Boyd_convex_2004.pdf'
outname = 'convex_func.pdf'

chap_start = 81
chap_end = 139

# intermediate
locfile = 'haha.pdf'
xmpdf = 'xm.pdf'
xmcpdf = 'xmc.pdf'

cmd = 'cp ' + filename + ' ' + locfile
os.system(cmd)
doc = fitz.open(locfile)

doc.delete_pages(chap_end, -1)
doc.delete_pages(0, chap_start - 2)

# repeat every page three times
for origin_pagenum in range(len(doc)):
    pagenum = origin_pagenum * 3
    doc.fullcopy_page(pagenum, pagenum)
    pagenum = pagenum + 1
    doc.fullcopy_page(pagenum, pagenum)

doc.save(xmpdf)
doc.close()

# crop each page
crop(["-ap", "10", "-p", "5", xmpdf, "-o", xmcpdf])

xmdoc = fitz.open(xmpdf)
xmcdoc = fitz.open(xmcpdf)

for pagenum in range(0, len(xmdoc), 3):
    xmpage = xmdoc.load_page(pagenum)
    X0 = xmpage.mediabox.x0
    Y0 = xmpage.mediabox.y0
    X1 = xmpage.mediabox.x1
    Y1 = xmpage.mediabox.y1
    xmcpage = xmcdoc.load_page(pagenum)
    x0 = xmcpage.mediabox.x0
    y0 = xmcpage.mediabox.y0
    x1 = xmcpage.mediabox.x1
    y1 = xmcpage.mediabox.y1

    left_crop = x0
    bott_crop = Y1 - y1
    righ_crop = X1 - x1
    topp_crop = y0

    width = x1 - x0
    height = y1 - y0

    # upper part
    R = fitz.Rect(x0, y0, x1, y0 + 0.75 * width)
    print(pagenum)
    xmpage.set_cropbox(R)

    # middle part
    xmpage = xmdoc.load_page(pagenum + 1)
    R = fitz.Rect(x0, y0 + 0.5 * (height - 0.75 * width), x1, y0 + 0.5 * height + 0.375 * width)
    print(pagenum+1)
    xmpage.set_cropbox(R)

    # bottom part
    xmpage = xmdoc.load_page(pagenum + 2)
    R = fitz.Rect(x0, y1 - 0.75 * width, x1, y1)
    print(pagenum+2)
    xmpage.set_cropbox(R)

xmdoc.save(outname)
xmdoc.close()

cmd = 'rm ' + xmpdf + ' ' + xmcpdf + ' ' + locfile
os.system(cmd)

# crop(["-ap4", str(left_crop), str(pu_bott_crop), str(righ_crop),
#       str(topp_crop), "-g", str(pagenum + 1), "-p", "100", xmpdf, "-o", xmpdf])
