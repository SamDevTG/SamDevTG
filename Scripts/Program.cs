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
        int frames = 30; // Número de frames para a animação
        int frameDelay = 100; // Atraso entre cada frame em milissegundos

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

                // Loop para criar os frames da animação
                for (int i = 0; i < frames; i++)
                {
                    // Limpa a tela a cada frame
                    graphics.Clear(Color.Black);

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

                    // Salva o frame atual
                    bitmap.Save($"frame_{i}.png", System.Drawing.Imaging.ImageFormat.Png);

                    // Aguarda o atraso antes de passar para o próximo frame
                    System.Threading.Thread.Sleep(frameDelay);
                }
            }
        }

        // Converte os frames em um arquivo GIF animado
        using (ImageMagick.MagickImageCollection collection = new ImageMagick.MagickImageCollection())
        {
            for (int i = 0; i < frames; i++)
            {
                // Adiciona cada frame à coleção
                collection.Add($"frame_{i}.png");
            }

            // Salva a coleção como um arquivo GIF animado
            collection.Write("output.gif", ImageMagick.MagickFormat.Gif);
        }

        // Limpa os arquivos temporários
        for (int i = 0; i < frames; i++)
        {
            System.IO.File.Delete($"frame_{i}.png");
        }

        Console.WriteLine("Animação output.gif gerada com sucesso.");
    }
}
