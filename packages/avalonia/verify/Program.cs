// Verifies the Avalonia package against the real Fluent theme, headlessly:
//   1. every key in VaFluentMap exists in FluentTheme (Dark and Light) with the kind we emit
//   2. under every theme, real controls render the expected token colors
//   3. switching themes live leaves exactly one merged dictionary behind
// Run: dotnet run --project packages/avalonia/verify   (exit code 1 on any failure)
using Avalonia;
using Avalonia.Controls;
using Avalonia.Headless;
using Avalonia.Media;
using Avalonia.Platform;
using Avalonia.Styling;
using Avalonia.Themes.Fluent;
using Avalonia.Threading;
using VisualAssault;

public class App : Application
{
    public override void Initialize() => Styles.Add(new FluentTheme());
}

public static class Program
{
    static int failures;
    static void Fail(string msg) { failures++; Console.WriteLine("FAIL: " + msg); }

    public static int Main()
    {
        AppBuilder.Configure<App>()
            .UseSkia()
            .UseHeadless(new AvaloniaHeadlessPlatformOptions { UseHeadlessDrawing = false })
            .SetupWithoutStarting();
        var app = Application.Current!;
        var fluent = app.Styles.OfType<FluentTheme>().Single();

        // 1. Every mapped key exists in the real Fluent theme and has the matching kind.
        int checkedKeys = 0;
        foreach (var variant in new[] { ThemeVariant.Dark, ThemeVariant.Light })
        {
            foreach (var (key, _) in VaFluentMap.Colors.Concat(VaFluentMap.Brushes))
            {
                if (!((Avalonia.Controls.IResourceNode)fluent).TryGetResource(key, variant, out var v) || v is null)
                { Fail($"[{variant}] Fluent has no resource '{key}'"); continue; }
                bool wantColor = VaFluentMap.Colors.Any(c => c.Key == key);
                if (wantColor && v is not Color) Fail($"[{variant}] '{key}' is {v.GetType().Name}, expected Color");
                if (!wantColor && v is not IBrush) Fail($"[{variant}] '{key}' is {v.GetType().Name}, expected a brush");
                checkedKeys++;
            }
        }
        Console.WriteLine($"key check: {checkedKeys} lookups, {VaFluentMap.Colors.Length + VaFluentMap.Brushes.Length} mapped keys");

        // 2. Render real controls under every theme and compare pixels.
        foreach (var theme in VisualAssaultThemes.All)
        {
            ThemeManager.Apply(theme.Id);
            RenderCheck(theme);
        }
        // 3. Live switching: apply twice, resources must not accumulate.
        ThemeManager.Apply("retrowave"); ThemeManager.Apply("hacker");
        if (app.Resources.MergedDictionaries.Count != 1) Fail($"merged dictionaries = {app.Resources.MergedDictionaries.Count}");

        Console.WriteLine(failures == 0 ? "ALL OK" : $"{failures} FAILURES");
        return failures == 0 ? 0 : 1;
    }

    sealed class WriteableBitmapLike
    {
        public byte[] Data = Array.Empty<byte>(); public int Stride, W, H;
        public (byte, byte, byte) Get(int x, int y) { var i = y * Stride + x * 4; return (Data[i], Data[i + 1], Data[i + 2]); }
    }

    static void RenderCheck(VaTheme theme)
    {
        var plain = new Button { Content = "Plain", Width = 140, Height = 34 };
        var accent = new Button { Content = "Accent", Width = 140, Height = 34 };
        accent.Classes.Add("accent");
        var text = new TextBox { Text = "", Width = 200, Height = 34 };
        var combo = new ComboBox { Width = 200, Height = 34, ItemsSource = new[] { "A", "B" }, SelectedIndex = 0 };
        var list = new ListBox { Width = 200, Height = 80, ItemsSource = new[] { "one", "two", "three" }, SelectedIndex = 0 };
        var check = new CheckBox { Content = "c", IsChecked = true, Width = 100, Height = 34 };
        var toggle = new ToggleSwitch { IsChecked = true, Width = 140, Height = 34 };

        var panel = new StackPanel { Spacing = 6, Margin = new Thickness(10) };
        foreach (var c in new Control[] { plain, accent, text, combo, list, check, toggle }) panel.Children.Add(c);
        var window = new Window { Width = 320, Height = 460, Content = panel };
        window.Show();
        Dispatcher.UIThread.RunJobs();
        var frame = window.CaptureRenderedFrame()!;

        var bmp = new WriteableBitmapLike { W = frame.PixelSize.Width, H = frame.PixelSize.Height };
        bmp.Stride = bmp.W * 4; bmp.Data = new byte[bmp.Stride * bmp.H];
        unsafe { fixed (byte* p = bmp.Data) frame.CopyPixels(new PixelRect(0, 0, bmp.W, bmp.H), (IntPtr)p, bmp.Data.Length, bmp.Stride); }

        void Expect(string what, int x, int y, VaToken token)
        {
            var (r, g, b) = bmp.Get(x, y); var want = theme[token];
            if (Math.Abs(r - want.R) > 2 || Math.Abs(g - want.G) > 2 || Math.Abs(b - want.B) > 2)
                Fail($"{theme.Id}: {what} at ({x},{y}) = #{r:x2}{g:x2}{b:x2}, expected {token} #{want.R:x2}{want.G:x2}{want.B:x2}");
        }
        System.Drawing.Point At(Control c, double dx, double dy)
        { var pt = c.TranslatePoint(new Point(dx, dy), window)!.Value; return new((int)pt.X, (int)pt.Y); }

        Expect("window background", 2, 2, VaToken.Bg);
        var p1 = At(plain, 8, 17); Expect("plain button", p1.X, p1.Y, VaToken.Surface);
        var p2 = At(accent, 8, 17); Expect("accent button", p2.X, p2.Y, VaToken.PrimaryAction);
        var p3 = At(text, 8, 17); Expect("textbox", p3.X, p3.Y, VaToken.Surface);
        var p4 = At(combo, 8, 17); Expect("combobox", p4.X, p4.Y, VaToken.Surface);
        var p5 = At(list, 6, 12); Expect("selected list item", p5.X, p5.Y, VaToken.AccentMuted);
        var p6 = At(check, 4, 10); Expect("checked checkbox", p6.X, p6.Y, VaToken.PrimaryAction);
        window.Close();
    }
}
