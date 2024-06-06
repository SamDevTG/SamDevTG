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
                Console.BackgroundColor = pixelColor;
                Console.Write(" ");
                Console.ResetColor();
            }
            Console.WriteLine();
        }
    }

    static void Main(string[] args)
    {
        Console.Clear();  // Limpar o terminal
        PrintSlow("Welcome to My Terminal!\n\n");  // Mensagem de boas-vindas

        // Carregar e imprimir imagem da bandeira trans
        Bitmap flagImage = LoadFlagImage();
        PrintImage(flagImage);

        // Imprimir informações pessoais
        Console.WriteLine("\n\nName: Your Name");
        Console.WriteLine("Age: 18 years old");
        Console.WriteLine("Pronouns: she/her");
        Console.WriteLine("Company: Winestone");
        Console.WriteLine("Position: Intern");

        // Aguardar para que o usuário possa ver a saída antes de fechar o terminal
        Console.WriteLine("\nPress any key to exit...");
        Console.ReadKey();
    }
}
