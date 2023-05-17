namespace mal
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            pbMain = new PictureBox();
            tbN = new TrackBar();
            lblInfo = new Label();
            ((System.ComponentModel.ISupportInitialize)pbMain).BeginInit();
            ((System.ComponentModel.ISupportInitialize)tbN).BeginInit();
            SuspendLayout();
            // 
            // pbMain
            // 
            pbMain.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            pbMain.Location = new Point(0, 0);
            pbMain.Margin = new Padding(0);
            pbMain.Name = "pbMain";
            pbMain.Size = new Size(937, 570);
            pbMain.TabIndex = 0;
            pbMain.TabStop = false;
            pbMain.SizeChanged += pbMain_SizeChanged;
            pbMain.MouseClick += pbMain_MouseClick;
            pbMain.MouseMove += pbMain_MouseMove;
            // 
            // tbN
            // 
            tbN.Anchor = AnchorStyles.Bottom | AnchorStyles.Left;
            tbN.Location = new Point(0, 584);
            tbN.Maximum = 500;
            tbN.Minimum = 1;
            tbN.Name = "tbN";
            tbN.Size = new Size(494, 45);
            tbN.TabIndex = 1;
            tbN.Value = 50;
            tbN.Scroll += tbN_Scroll;
            // 
            // lblInfo
            // 
            lblInfo.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
            lblInfo.Location = new Point(688, 584);
            lblInfo.Name = "lblInfo";
            lblInfo.Size = new Size(250, 45);
            lblInfo.TabIndex = 2;
            lblInfo.TextAlign = ContentAlignment.MiddleRight;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.SteelBlue;
            ClientSize = new Size(937, 628);
            Controls.Add(lblInfo);
            Controls.Add(tbN);
            Controls.Add(pbMain);
            Name = "Form1";
            Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)pbMain).EndInit();
            ((System.ComponentModel.ISupportInitialize)tbN).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private PictureBox pbMain;
        private TrackBar tbN;
        private Label lblInfo;
    }
}