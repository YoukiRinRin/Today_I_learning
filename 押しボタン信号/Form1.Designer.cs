namespace 押しボタン信号
{
    partial class oshibutton
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージド リソースを破棄する場合は true を指定し、その他の場合は false を指定します。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.btn = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // btn
            // 
            this.btn.BackColor = System.Drawing.Color.Transparent;
            this.btn.FlatAppearance.BorderSize = 0;
            this.btn.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Transparent;
            this.btn.FlatAppearance.MouseOverBackColor = System.Drawing.Color.Transparent;
            this.btn.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btn.ForeColor = System.Drawing.Color.Black;
            this.btn.Location = new System.Drawing.Point(136, 177);
            this.btn.Name = "btn";
            this.btn.Size = new System.Drawing.Size(113, 118);
            this.btn.TabIndex = 1;
            this.btn.Text = "button1";
            this.btn.UseVisualStyleBackColor = false;
            this.btn.Click += new System.EventHandler(this.btn_Click);
            // 
            // timer1
            // 
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // oshibutton
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::押しボタン信号.Properties.Resources.hokousyayou_button_oshite;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(387, 452);
            this.Controls.Add(this.btn);
            this.DoubleBuffered = true;
            this.Name = "oshibutton";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.Button btn;
        private System.Windows.Forms.Timer timer1;
    }
}

