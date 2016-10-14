using System;
using CSharpTestbed;

namespace AbstractBase
{
    class Program
    {
        static void Main(string[] args)
        {
            person p = new person();
            p.Initialize();
            Console.WriteLine(p.ToString());
            p.CleanUp();

            accepts a = new accepts();
            Console.WriteLine(a.AcceptsTypes(p));
            Console.ReadLine();
        }
    }
}
