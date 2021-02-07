import os

# input parameters
filename = "~/Sync/sci-tech/Boyd_convex_2004.pdf"
original_size = [8.5, 11.0]
pages = [81, 139]
margins_x = [1.37, 1.0, 1.87, 1.0]
margins_y = [2.12, 1.0, 1.12, 1.0]
crop_size = [5.26, 9.0]

# compute duokan size
vertical_size = round(0.75 * crop_size[0], 2)
xm_size = [crop_size[0], vertical_size]
margins_x_up = [margins_x[0], original_size[1] - margins_x[3] - vertical_size,\
                margins_x[2], margins_x[3]]
margins_x_md = [margins_x[0], (original_size[1] - vertical_size) / 2,\
                margins_x[2], (original_size[1] - vertical_size) / 2]
margins_x_lo = [margins_x[0], margins_x[1], margins_x[2],\
                original_size[1] - margins_x[1] - vertical_size]
margins_y_up = [margins_y[0], original_size[1] - margins_y[3] - vertical_size,\
                margins_y[2], margins_y[3]]
margins_y_md = [margins_y[0], (original_size[1] - vertical_size) / 2,\
                margins_y[2], (original_size[1] - vertical_size) / 2]
margins_y_lo = [margins_y[0], margins_y[1], margins_y[2],\
                original_size[1] - margins_y[1] - vertical_size]

# options for pdfjam
options_x = "--papersize '{" + str(xm_size[0]) + "in," + str(xm_size[1]) + "in}'"\
    + " --trim '" + str(margins_x[0]) + 'in ' + str(margins_x[1]) + 'in '\
    + str(margins_x[2]) + "in " + str(margins_x[3]) + "in' --clip true"

options_y = "--papersize '{" + str(xm_size[0]) + "in," + str(xm_size[1]) + "in}'"\
    + " --trim '" + str(margins_y[0]) + 'in ' + str(margins_y[1]) + 'in '\
    + str(margins_y[2]) + "in " + str(margins_y[3]) + "in' --clip true"

# original papersize is 8.5in x 11.0in
# left margin is 1.37in, right margin is 1.87in
# upper/lower margins are 1.0in
options_odd = "--papersize '{5.26in,9.0in}' --trim '1.37in 1.0in 1.87in 1.0in' --clip true "
options_even = "--papersize '{5.26in,9.0in}' --trim '2.12in 1.0in 1.12in 1.0in' --clip true "
pages_odd = " '81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139' "
pages_even = " '82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138' "
outfile_odd = "boyd_ch3_odd.pdf"
outfile_even = "boyd_ch3_even.pdf"
cmd = "pdfjam " + options_odd + filename + pages_odd + "-o " + outfile_odd
os.system(cmd)
cmd = "pdfjam " + options_even + filename + pages_even + "-o " + outfile_even
os.system(cmd)

options = "--papersize '{6.125in,3in}' --trim '0in 5.375in 0in 0in' --clip true "
cmd = "pdfjam " + options + outfile + " -o upper.pdf"

os.system(cmd)

options = "--papersize '{6.125in,3in}' --trim '0in 2.68in 0in 2.68in' --clip true "
cmd = "pdfjam " + options + outfile + " -o middle.pdf"

os.system(cmd)

options = "--papersize '{6.125in,3in}' --trim '0in 0in 0in 5.375in' --clip true "
cmd = "pdfjam " + options + outfile + " -o bottom.pdf"

os.system(cmd)

inputfiles = ""
for k in range(1, 39):
    inputfiles = inputfiles + " upper.pdf '" + str(k) + "' middle.pdf '" + str(k) + "' bottom.pdf '" + str(k) + "'"

options = "--papersize '{6.125in,3in}'"
cmd = "pdfjam " + options + inputfiles + " -o pml_ch3_xm.pdf"

os.system(cmd)
