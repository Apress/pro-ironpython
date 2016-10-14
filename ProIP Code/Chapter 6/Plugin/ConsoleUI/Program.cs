using System;
using IPEngine;

namespace ConsoleUI
{
    class Program
    {
        static void Main(string[] args)
        {
            var t = new TestPlugin();
            t.ConfigurePlugin("test", "pluginTest", "HelloPlugin", @"C:\Python\Plugin\pluginTest.py");
            Console.WriteLine(t.ExecutePlugin<string>());

            var p = new TestPlugin();
            p.ConfigurePlugin("params", "pluginParameters", "tryParams", @"C:\Python\Plugin\pluginParameters.py");
            string[] parameters = {"Alan", "24"};
            Console.WriteLine(p.ExecutePlugin<string>(parameters));

            var e = new EngineManager();
            e.Initialize(@"C:\Python\Plugin\pluginTest.py");
            Console.WriteLine(e.Execute<string>("pluginTest", "HelloPlugin"));
            Console.Read();
        }
    }
}
