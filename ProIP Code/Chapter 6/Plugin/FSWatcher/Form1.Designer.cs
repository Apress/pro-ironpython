namespace FSWatcher
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.txtUpdates = new System.Windows.Forms.TextBox();
            this.p1WatcherEnabled = new System.Windows.Forms.CheckBox();
            this.p2WatcherEnabled = new System.Windows.Forms.CheckBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.p2WatcherEnabled);
            this.groupBox1.Controls.Add(this.p1WatcherEnabled);
            this.groupBox1.Controls.Add(this.txtUpdates);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(592, 230);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "File System Watcher";
            // 
            // txtUpdates
            // 
            this.txtUpdates.Location = new System.Drawing.Point(3, 16);
            this.txtUpdates.Multiline = true;
            this.txtUpdates.Name = "txtUpdates";
            this.txtUpdates.ReadOnly = true;
            this.txtUpdates.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtUpdates.Size = new System.Drawing.Size(401, 208);
            this.txtUpdates.TabIndex = 0;
            // 
            // p1WatcherEnabled
            // 
            this.p1WatcherEnabled.AutoSize = true;
            this.p1WatcherEnabled.Location = new System.Drawing.Point(410, 19);
            this.p1WatcherEnabled.Name = "p1WatcherEnabled";
            this.p1WatcherEnabled.Size = new System.Drawing.Size(97, 17);
            this.p1WatcherEnabled.TabIndex = 1;
            this.p1WatcherEnabled.Text = "Watch .p1 files";
            this.p1WatcherEnabled.UseVisualStyleBackColor = true;
            // 
            // p2WatcherEnabled
            // 
            this.p2WatcherEnabled.AutoSize = true;
            this.p2WatcherEnabled.Location = new System.Drawing.Point(410, 42);
            this.p2WatcherEnabled.Name = "p2WatcherEnabled";
            this.p2WatcherEnabled.Size = new System.Drawing.Size(97, 17);
            this.p2WatcherEnabled.TabIndex = 2;
            this.p2WatcherEnabled.Text = "Watch .p2 files";
            this.p2WatcherEnabled.UseVisualStyleBackColor = true;
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 500;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(616, 257);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "FSWatcher";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox txtUpdates;
        private System.Windows.Forms.CheckBox p2WatcherEnabled;
        private System.Windows.Forms.CheckBox p1WatcherEnabled;
        private System.Windows.Forms.Timer timer1;

    }
}

