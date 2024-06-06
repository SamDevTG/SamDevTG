using System;
using System.Drawing;

class Program
{
    static void Main(string[] args)
    {
        // Configurações da imagem
        int width = 800;
        int height = 200;
        string outputPath = "output.png";

        // Cria uma nova imagem
        using (Bitmap bitmap = new Bitmap(width, height))
        {
            using (Graphics graphics = Graphics.FromImage(bitmap))
            {
                // Define a cor de fundo
                graphics.Clear(Color.White);

                // Define as fontes
                Font font = new Font("Arial", 24, FontStyle.Bold);
                Brush brush = Brushes.Black;

                // Adiciona texto na imagem
                string text = "Atualização Automática do README";
                PointF point = new PointF(10, 80);
                graphics.DrawString(text, font, brush, point);

                // Salva a imagem
                bitmap.Save(outputPath);
            }
        }

        Console.WriteLine($"Imagem salva em: {outputPath}");
    }
}
