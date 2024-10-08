using System;	// module(Console)

class Program
{
    // Main function
    static void Main(string[] args) // command line arguments convention
    {
        string[] inputs = Console.ReadLine().Split();

        int A = int.Parse(inputs[0]);
        int B = int.Parse(inputs[1]);

        int sum = A + B;

        Console.WriteLine(sum);
    }
}