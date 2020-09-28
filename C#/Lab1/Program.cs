using System;
using static System.Math;

namespace Lab1
{
    class Program
    {
        static void Main(string[] args)
        {
            // This code outputs the solution to this equation.
            //                      x^2.8                               x
            //      y= —————————————————————————————————  - arctg(——————————————)^5
            //         ( cos( x^3 - 3.7 )^4 + |3x|^0.5 )             lg(|x|)
            // 

            Console.WriteLine("Введите x для вычисления значения y=f(x): ");

            string string_x = Console.ReadLine().Replace(".", ",");
            double x = Convert.ToDouble(string_x);

            double y =                      Pow(x, 2.8) /
            //         ——————————————————————————————————————————————————
                       (Pow(Cos(Pow(x, 3) - 3.7), 4) + Pow(Abs(3 * x), 0.5))

                       -

                       Pow(Atan(x / Log10(Abs(x))), 5)
            ;
            y = Round(y, 4);


            Console.WriteLine($"Выходное значение y: {y}");
            Console.ReadLine();
        }
    }
}
