#Examples str.format() method usage

print ("Ceci {0} {1} {2} test %s".format("est", "un", "petit")%("de print"))

print ("%(x)s %(x)s %(x)s" % {"x" : "bon"})

print("3a={} 3b={} 3c={} {}".format(*"chut"))
