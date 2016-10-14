using System;
using System.IO;
using System.Windows.Forms;
using IPEngine;

namespace FSWatcher
{
    public partial class Form1 : Form
    {
        private static string updateText = String.Empty;
        private FileSystemWatcher fp1;
        private FileSystemWatcher fp2;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            fp1 = InitializeP1Watcher(@"C:\Python", "*.p1");
            fp2 = InitializeP2Watcher(@"C:\Python", "*.p2");
        }

        public FileSystemWatcher InitializeP1Watcher(string path, string filter)
        {
            var f = new FileSystemWatcher { Path = path, Filter = filter, EnableRaisingEvents = true };
            f.Deleted += OnP1Deleted;
            return f;
        }

        public FileSystemWatcher InitializeP2Watcher(string path, string filter)
        {
            var f = new FileSystemWatcher { Path = path, Filter = filter, EnableRaisingEvents = true };
            f.Created += OnP2Created;
            return f;
        }

        private static void OnP1Deleted(object sender, FileSystemEventArgs e)
        {
            var p = new TestPlugin();
            p.ConfigurePlugin("test", "p1Handler", "NotifyCaller", @"C:\Python\Plugin\p1Handler.py");
            string[] parameters = { e.FullPath };
            updateText += p.ExecutePlugin<string>(parameters);
            updateText += "\r\n";
        }

        private static void OnP2Created(object sender, FileSystemEventArgs e)
        {
            var p = new TestPlugin();
            p.ConfigurePlugin("test", "p1Handler", "NotifyCaller", @"C:\Python\Plugin\p2Handler.py");
            string[] parameters = { e.FullPath };
            updateText += p.ExecutePlugin<string>(parameters);
            updateText += "\r\n";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            txtUpdates.Text = updateText;
            switch (p1WatcherEnabled.Checked)
            {
                case false:
                    fp1.Deleted -= OnP1Deleted;
                    break;
                default:
                    fp1.Deleted += OnP1Deleted;
                    break;
            }
            switch (p2WatcherEnabled.Checked)
            {
                case false:
                    fp2.Created -= OnP2Created;
                    break;
                default:
                    fp2.Created += OnP2Created;
                    break;
            }
        }
    }
}
