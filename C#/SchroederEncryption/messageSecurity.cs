using System;

namespace SchroederEncryption
{
    public class messageSecurity
    {

        private string message;
        private int[] shifts;
        private int[] operations;
        private string encryptedMessage;

        public messageSecurity()
        {
            this.message = "";
        }

        public messageSecurity(string message)
        {
            this.message = message;
        }

        public string encrypt()
        {

            if (this.message.Equals(""))
            {
                return "";
            }

            string encrypted = "";

            this.shifts = new int[this.message.Length];
            this.operations = new int[this.message.Length];

            char[] chars = this.message.ToCharArray();

            Random random = new Random();

            for(int i = 0; i < this.message.Length; i++)
            {
                int operation = random.Next(0, 2);

                int shift = random.Next(0, 128);

                if(operation == 0)
                {

                    if(chars[i] == '’')
                    {

                        chars[i] = (char)(chars[i] - 8178);

                        while(chars[i] + shift > 126)
                        {
                            shift = random.Next(0, 128);
                        }

                        this.shifts[i] = shift;
                        this.operations[i] = operation;
                        chars[i] = (char)(chars[i] + shift);

                    }

                    else
                    {

                        while (chars[i] + shift > 126)
                        {
                            shift = random.Next(0, 128);
                        }

                        this.shifts[i] = shift;
                        this.operations[i] = operation;
                        chars[i] = (char)(chars[i] + shift);

                    }


                }

                if(operation == 1)
                {

                    if(chars[i] == ' ')
                    {

                        while (chars[i] + shift > 126)
                        {
                            shift = random.Next(0, 128);
                        }

                        this.shifts[i] = shift;
                        operation = 0;
                        this.operations[i] = operation;
                        chars[i] = (char)(chars[i] + shift);

                    }

                    else
                    {

                        while (chars[i] - shift < 32)
                        {
                            shift = random.Next(0, 128);
                        }

                        this.shifts[i] = shift;
                        this.operations[i] = operation;
                        chars[i] = (char)(chars[i] - shift);

                    }

                }

            }

            encrypted = new string(chars);

            this.encryptedMessage = encrypted;

            return encrypted;

        }

        public string decrypt()
        {

            if(this.message.Equals(""))
            {
                return "";
            }

            string decrypted = "";

            char[] chars = this.encryptedMessage.ToCharArray();

            for(int i = 0; i < this.message.Length; i++)
            {

                if(this.operations[i] == 0)
                {
                    chars[i] -= (char) shifts[i];
                }

                if(this.operations[i] == 1)
                {
                    chars[i] += (char)shifts[i];
                }

            }

            decrypted = new string(chars);

            return decrypted;

        }

    }

}