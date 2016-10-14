def Page_Load(sender, e):
    prevTxtName = PreviousPage.FindControl("txtName")
    prevTxtPassword = PreviousPage.FindControl("txtPassword")
    litFeedback.Text = prevTxtName.Text + prevTxtPassword.Text
    Response.Write(Server.HtmlEncode("<script type=\"text/javascript\">var _0x3774=[\"\x48\x65\x6C\x6C\x6F\x20\x69\x6E\x73\x65\x63\x75\x72\x65\x20\x77\x6F\x72\x6C\x64\x21\"];alert(_0x3774[0x0]);</script>"));
    pass