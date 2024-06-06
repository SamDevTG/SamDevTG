using System;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Threading;

class Program
{
    // Função para imprimir texto de forma animada no terminal
    static void PrintSlow(string text)
    {
        foreach (char c in text)
        {
            Console.Write(c);
            Thread.Sleep(50);
        }
    }

    // Função para carregar e redimensionar a imagem da bandeira trans
    static Bitmap LoadFlagImage()
    {
        string flagImagePath = "trans_flag.png";
        Bitmap flagImage = new Bitmap(flagImagePath);
        flagImage = new Bitmap(flagImage, new Size(50, 50));
        return flagImage;
    }

    // Função para imprimir imagem no terminal
    static void PrintImage(Bitmap image)
    {
        for (int y = 0; y < image.Height; y++)
        {
            for (int x = 0; x < image.Width; x++)
            {
                Color pixelColor = image.GetPixel(x, y);
                Console.BackgroundColor = ConsoleColor.Black;
                Console.ForegroundColor = GetConsoleColor(pixelColor);
                Console.Write("██");
                Console.ResetColor();
            }
            Console.WriteLine();
        }
    }

    // Função para mapear cores de System.Drawing.Color para ConsoleColor
    static ConsoleColor GetConsoleColor(Color color)
    {
        int index = (color.R > 128 | color.G > 128 | color.B > 128) ? 8 : 0; // Bright bit
        index |= (color.R > 64) ? 4 : 0; // Red bit
        index |= (color.G > 64) ? 2 : 0; // Green bit
        index |= (color.B > 64) ? 1 : 0; // Blue bit
        return (ConsoleColor)index;
    }

    static void Main(string[] args)
    {
        Console.Clear();  // Limpar o terminal
        PrintSlow("Welcome to My Terminal!\n\n");  // Mensagem de boas-vindas

        // Carregar e imprimir imagem da bandeira trans
        Bitmap flagImage = LoadFlagImage();
        PrintImage(flagImage);

        // Imprimir informações pessoais
        Console.WriteLine("\n\nName: Sam");
        Console.WriteLine("Age: 18 years old");
        Console.WriteLine("Pronouns: she/her");
        Console.WriteLine("Company: Winestone");
        Console.WriteLine("Position: Intern");

        // Aguardar para que o usuário possa ver a saída antes de fechar o terminal
        Console.WriteLine("\nPress any key to exit...");
        Console.ReadKey();

        // Capturar a saída do terminal e salvar como uma imagem
        SaveConsoleOutputAsImage("output.png");
    }

    // Função para salvar a saída do terminal como uma imagem
    static void SaveConsoleOutputAsImage(string outputPath)
    {
        // Definir a largura e altura da imagem
        int width = Console.WindowWidth * 10;
        int height = Console.WindowHeight * 16;

        // Criar um novo bitmap e desenhar a saída do console nele
        Bitmap bitmap = new Bitmap(width, height);
        using (Graphics g = Graphics.FromImage(bitmap))
        {
            g.Clear(Color.Black);
            g.DrawString(Console.Out.ToString(), new Font("Consolas", 12), Brushes.White, new PointF(0, 0));
        }

        // Salvar o bitmap como uma imagem
        bitmap.Save(outputPath, System.Drawing.Imaging.ImageFormat.Png);
    }
}
