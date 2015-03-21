from patchwords.models import *
from patchwords.queries import *

p = Paragraph.objects.filter(parent=None)[5]

print "for", p._print_subtree()

print getMostPopularSubtree(p)
    #print tup
