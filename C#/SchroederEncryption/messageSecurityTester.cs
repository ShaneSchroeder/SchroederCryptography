using System;
using System.Collections.Generic;
using System.Text;

namespace SchroederEncryption
{
    public class messageSecurityTester
    {
        public static void Main(string[] args)
        {

            Console.WriteLine("Please enter a word to be encrypted");
            string user = Console.ReadLine();

            messageSecurity message = new messageSecurity(user);

            Console.WriteLine();

            Console.WriteLine("Encrypted Message: ");

            string encrypted = message.encrypt();

            Console.WriteLine(encrypted);
            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine("Decrypted Message: ");

            string decrypted = message.decrypt();

            Console.WriteLine(decrypted);

            Console.WriteLine();

        }

    }
}
