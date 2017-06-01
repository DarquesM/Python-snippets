#Examples str.format() method usage

print ("Ceci {0} {1} {2} test %s".format("est", "un", "petit")%("de print"))
# output : Ceci est un petit test de print

print ("%(x)s %(x)s %(x)s" % {"x" : "bon"})
# output : bon bon bon

print("3a={} 3b={} 3c={} {}".format(*"chut"))
# output : 3a=c 3b=h 3c=u t

