using System;
using System.Reflection;
using System.Text;

namespace CSharpTestbed
{
    class person : humanBeing
    {
        public override void Initialize()
        {
            SetName("Alan Harris");
            SetDateOfBirth(Convert.ToDateTime("1/1/2009"));
        }

        public override string ToString()
        {
            PropertyInfo[] p = GetType().GetProperties();
            StringBuilder sb = new StringBuilder();

            foreach (PropertyInfo pi in p)
            {
                sb.Append(pi.Name);
                sb.Append(": ");
                sb.Append(pi.GetValue(this, null));
                sb.Append("\r\n");
            }

            return sb.ToString();
        }

        public override void CleanUp()
        {
            // perform any cleanup tasks here...
        }
    }
}
