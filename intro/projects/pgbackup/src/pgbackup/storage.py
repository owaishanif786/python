def local(inflie, outfile):
    outfile.write(inflie.read())
    outfile.close()
    inflie.close()