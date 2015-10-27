from github3 import login
from creds import username, token
g = login(username, token=token)

#www.nt41.com www.nt41.us www.nt-41.us
names = """www.intros5r.com www.bugreportr.com www.claudettedupont.com www.du-pont.us www.dupont.website www.grokurl.com www.locateselect.com  www.4lph4b37.com www.4lph4b37.xyz www.agnos.xyz www.agnost.xyz www.saltopen.com www.i10r.xyz www.i11n.xyz www.introspection.xyz www.introspector.xyz www.refuelapp.xyz""".split(" ")
for name in names:
             r = g.create_repository("website-"+name,
                                 description='Website for ' + name,
                                 homepage=name,
                                 private=False,
                                 has_issues=True,
                                 has_wiki=False,
                                 auto_init=False,
                                 gitignore_template='')
