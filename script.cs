using System;
using System.Drawing;

class Program
{
    static void Main()
    {
        int width = 800;
        int height = 200;
        string text = "Olá, sou [Seu Nome] 👋";
        string filePath = "output.png";

        using (Bitmap bitmap = new Bitmap(width, height))
        {
            using (Graphics graphics = Graphics.FromImage(bitmap))
            {
                graphics.Clear(Color.White);
                Font font = new Font("Arial", 40, FontStyle.Bold);
                Brush brush = Brushes.Black;
                PointF point = new PointF(10, 50);

                graphics.DrawString(text, font, brush, point);
            }

            bitmap.Save(filePath);
        }
    }
}
