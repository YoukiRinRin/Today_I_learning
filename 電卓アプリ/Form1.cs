using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 電卓アプリ
{
    public partial class 電卓アプリ : Form
    {
        double  num1;
        double  num2;
        double result;
        //"*","-","÷","*"が入る
        string state;

        int point = 1;
        int flg_point = 0; 
        
        public 電卓アプリ()
        {
            InitializeComponent();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            input_num(5);
        }

        private void bt_1_Click(object sender, EventArgs e)
        {
            input_num(1);
        }

        private void bt_2_Click(object sender, EventArgs e)
        {
            input_num(2);
        }
        

        private void bt_3_Click(object sender, EventArgs e)
        {
            input_num(3);
        }

        private void bt_4_Click(object sender, EventArgs e)
        {
            input_num(4);
        }

        private void bt_6_Click(object sender, EventArgs e)
        {
            input_num(6);
        }

        private void bt_7_Click(object sender, EventArgs e)
        {
            input_num(7);
        }

        private void bt_8_Click(object sender, EventArgs e)
        {
            input_num(8);
        }

        private void bt_9_Click(object sender, EventArgs e)
        {
            input_num(9);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            add_symblebutton("+");
        }

        private void btn_division_Click(object sender, EventArgs e)
        {
            add_symblebutton("÷");
        }

        private void btn_times_Click(object sender, EventArgs e)
        {
            add_symblebutton("×");
        }

        private void btn_minus_Click(object sender, EventArgs e)
        {
            add_symblebutton("-");
        }

        private void btn_equal_Click(object sender, EventArgs e)
        {
            switch (state)
            {
                case "+":
                    result = num2 + num1;
                    break;
                case "-":
                    result = num2 - num1;
                    break;
                   
                case "÷":
                    result = num2 / num1;
                    break;
                case "×":
                    result = num2 * num1;
                    break;
            }
            lbl_show_num_bf.Text = "";
            lbl_show_num_now.Text = result.ToString();
        }
        public int input_num(int x)
        {
            double au = 0;
            switch (flg_point)
            {
                case 0:
                    num1 = (num1 * 10) + x;
                    break;
                case 1:
                                       
                    point = point * 10;
                    au = x / point;
                    num1 = num1 + au;
                    break;
            }
            MessageBox.Show(au.ToString());
            MessageBox.Show(num1.ToString());
            lbl_show_num_now.Text = num1.ToString();
            return 0;
        }

        public int add_symblebutton(string x)
        {
            state = x;
            lbl_show_num_now.Text = "";
            lbl_symbole.Text = state;
            num2 = num1;
            num1 = 0;
            lbl_show_num_bf.Text = num2.ToString();

            return 0;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            num1 = num1 * -1;
        }

        private void btn_0_Click(object sender, EventArgs e)
        {
            input_num(0);
        }

        private void button20_Click(object sender, EventArgs e)
        {
            num1 = 0;
        }

        private void bt_AC_Click(object sender, EventArgs e)
        {
            num1 = 0;
            num2 = 0;
            state = "";
            flg_point = 0;
        }

        private void btn_point_Click(object sender, EventArgs e)
        {
            flg_point = 1;
            MessageBox.Show(flg_point.ToString());
        }
    }
}
