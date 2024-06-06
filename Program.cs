using System;
using System.Drawing;

class Program
{
    static void Main(string[] args)
    {
        // Image settings
        int width = 800;
        int height = 200;
        string outputPath = "output.png";

        // Create a new image
        using (Bitmap bitmap = new Bitmap(width, height))
        {
            using (Graphics graphics = Graphics.FromImage(bitmap))
            {
                // Set background color
                graphics.Clear(Color.White);

                // Set fonts
                Font font = new Font("Arial", 24, FontStyle.Bold);
                Brush brush = Brushes.Black;

                // Add text to image
                string text = "Automatic README Update";
                SizeF textSize = graphics.MeasureString(text, font);
                PointF point = new PointF((width - textSize.Width) / 2, (height - textSize.Height) / 2);
                graphics.DrawString(text, font, brush, point);

                // Save the image
                bitmap.Save(outputPath);
            }
        }

        Console.WriteLine($"Image saved at: {outputPath}");
    }
}
