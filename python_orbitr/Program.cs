using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace python_orbitr
{
    class Program
    {
        //static string path_to_python = "C:\\Users\\deneg\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe";
        
        static string path_to_python;
        static bool player = false;
        static bool allOk = true;
        static void Main(string[] args)
        {
            path_to_python = PythonSearcher();
            if (path_to_python == "ERROR")
            {
                Console.WriteLine("Интерпретатор питона не обнаружен на этом компьютере! Убедитесь что путь к python.exe указан в переменной среде PATH");
                Console.ReadLine();
                return;
            }
            int count_round = 30;
            int p1 = 0;
            int p2 = 0;
            for (int i = 0; i < count_round; i++)
            {
                //string nachstr = "This_is_start_string";
                //string nachstr = Console.ReadLine().Replace(" ", "_");
                string nachstr = generator_string();
                Console.WriteLine("СГЕНЕРИРОВАННАЯ СТРОКА: |" + nachstr + "| Длина:" + nachstr.Length);

                Console.WriteLine("-----------------------------------------");
                while (nachstr != "")
                {
                    var symb = run_cmd(choise(), nachstr);
                    nachstr = execute(nachstr, symb);
                    Console.WriteLine(nachstr);
                    //Thread.Sleep(100);
                }
                Console.WriteLine("-----------------------------------------");

                if (player)
                {
                    Console.WriteLine("Победил игрок №1");
                    p1++;
                }
                else
                {
                    Console.WriteLine("Победил игрок №2");
                    p2++;
                }
                Console.WriteLine("Счет: {0}|{1} (Партия №{2}/{3})", p1, p2, i + 1, count_round);
                player = false;
                Thread.Sleep(700);
                Console.WriteLine("=========================================");
            }
            if (p1 == p2)
                Console.WriteLine("Победила дружба!");
            else
            if (p1 > p2)
                Console.WriteLine("Первый игрок умнее второго");
            else
                Console.WriteLine("Второй игрок умнее первого");
            Console.ReadLine();

        }
        private static Random random = new Random((int)DateTime.Now.Ticks);
        static string generator_string()
        {
            var az = Enumerable.Range('a', 'z' - 'a' + 1).Select(i => (Char)i).ToList();
            az.AddRange(Enumerable.Range('A', 'Z' - 'A' + 1).Select(i => (Char)i).ToList());
            az.AddRange(Enumerable.Range('1', '9' - '1' + 1).Select(i => (Char)i).ToList());
            //az.AddRange(Enumerable.Range('а', 'я' - 'а' + 1).Select(i => (Char)i).ToList());
            //az.AddRange(Enumerable.Range('А', 'Я' - 'А' + 1).Select(i => (Char)i).ToList());
            az.Add('_');



            StringBuilder sb = new StringBuilder();
            for(int i=0; i<random.Next(80)+20; i++)
            {
                sb.Append(az[random.Next(az.Count)]);
            }
            return sb.ToString();
        }
        static string choise()
        {
            if(allOk)
                player = !player;
            if (player)
            {
                Console.Write("PLAYER 1: ");
                return "program1.py";
            }
            else
            {
                Console.Write("PLAYER 2: ");
                return "program2.py";
            }

        }
        static string execute(string ishod, string command)
        {
            allOk = true;
            if (command.Contains("SYMBOL"))
            {
                if (ishod.Contains(command.Split()[0]))
                    return ishod.Remove(ishod.IndexOf(command.Split()[0]), 1);
                else
                {
                    allOk = false;
                    return ishod;
                }
            }
            else
            {
                if (ishod.Contains(command.Split()[0]))
                    return ishod.Replace(command.Split()[0], "");
                else
                {
                    allOk = false;
                    return ishod;
                }
            }
        }

        static string PythonSearcher()
        {
            string[] value = System.Environment.GetEnvironmentVariable("path").Split(';');
            foreach(string path in value)
            {
                if (File.Exists(path + "\\python.exe"))
                    return path + "\\python.exe";
            }
            return "ERROR";

        }

        static private string run_cmd(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = path_to_python;
            start.Arguments = string.Format("{0} {1}", cmd, args);
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    return result;
                }
            }
            return "ERROR";
        }
    }
}
