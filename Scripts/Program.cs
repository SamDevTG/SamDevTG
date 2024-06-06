using System;
using System.Drawing;
using System.Drawing.Drawing2D;

class Program
{
    static void Main(string[] args)
    {
        // Define as dimensões da imagem
        int width = 800;
        int height = 600;

        // Cria uma nova imagem bitmap com as dimensões especificadas
        using (Bitmap bitmap = new Bitmap(width, height))
        {
            // Cria um objeto Graphics a partir da imagem bitmap
            using (Graphics graphics = Graphics.FromImage(bitmap))
            {
                // Define o fundo da imagem como preto
                graphics.Clear(Color.Black);

                // Define a fonte e as cores
                Font font = new Font("Courier New", 12);
                Brush brush = new SolidBrush(Color.White);
                Pen pen = new Pen(Color.White);

                // Define o terminal fictício
                string[] terminalOutput = {
                    "Welcome to My Terminal",
                    "",
                    "> ls",
                    "output.png   README.md   script.cs",
                    "",
                    "> cat",
                    "   /\\_/\\",
                    "  ( o.o )",
                    "   > ^ <"
                };

                // Desenha o terminal fictício
                float lineHeight = 20;
                float x = 10, y = 10;
                foreach (string line in terminalOutput)
                {
                    graphics.DrawString(line, font, brush, x, y);
                    y += lineHeight;
                }

                // Adiciona suas informações
                string[] personalInfo = {
                    "Name: Seu Nome",
                    "Age: 18",
                    "Interests: Technology, Cats, Programming"
                };
                x = 500;
                y = 10;
                foreach (string info in personalInfo)
                {
                    graphics.DrawString(info, font, brush, x, y);
                    y += lineHeight;
                }

                // Salva a imagem como output.png
                bitmap.Save("output.png", System.Drawing.Imaging.ImageFormat.Png);

                Console.WriteLine("Imagem output.png gerada com sucesso.");
            }
        }
    }
}
