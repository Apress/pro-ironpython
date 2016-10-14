import System

def Page_Load(sender, e):
    for i in Request.ServerVariables:
	    Response.Write(i + "<br/>")