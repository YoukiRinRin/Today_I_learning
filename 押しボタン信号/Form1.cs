using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 押しボタン信号
{
    public partial class oshibutton : Form
    {
        public oshibutton()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
            btn.SetBounds(btn.Left, btn.Top, 301, 301,
                    BoundsSpecified.Size);
            System.Drawing.Drawing2D.GraphicsPath path =
                new System.Drawing.Drawing2D.GraphicsPath();
            //丸を描く
            path.AddEllipse(new Rectangle(5,10,100, 100));
            btn.Region = new Region(path);

        }

        private void btn_Click(object sender, EventArgs e)
        {
            this.BackgroundImage = Properties.Resources.hokousyayou_button_omachi;
            MessageBox.Show("ボタンが押されました。30秒お待ちください");

            //if (this.BackgroundImage == Properties.Resources.hokousyayou_button_omachi){
            //var sw = new System.Diagnostics.Stopwatch();

            //sw.Start();

            //System.Threading.Thread.Sleep(30000);

            //sw.Stop();

            //sw.Reset();


            //}
            System.Threading.Thread.Sleep(30000);
            MessageBox.Show("青になりました");

            this.BackgroundImage = Properties.Resources.hokousyayou_button_oshite;


        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            
        }
    }
}
